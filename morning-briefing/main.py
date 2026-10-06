"""Compose the morning briefing and optionally deliver it."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.briefing import (
    TRANSLATION_NOTE,
    Runtime,
    append_fx,
    append_news_links,
    build_briefing,
    build_system_prompt,
    collect_user_prompt,
    correct_city_word,
)
from core.config import apply_provider_override, load_config, validate_config
from core.loader import load_symbol
from core.redact import collect_secrets, configure_logging, drop_blank_secrets, scrub

logger = logging.getLogger("morning")


class _FailedSource:
    def fetch(self, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("initialization failed")


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="morning-briefing", description="დილის ბრიფინგი")
    parser.add_argument("--config", default=str(ROOT / "config.yaml"), help="config.yaml-ის გზა")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="ბრიფინგი დაიბეჭდება და არ გაიგზავნება",
    )
    parser.add_argument(
        "--provider",
        default=None,
        help="ერთი მოდელის იძულებითი არჩევა, მაგალითად კონფიგში ჩაწერილი იდენტიფიკატორი",
    )
    return parser.parse_args(argv)


def build_runtime(config: Mapping[str, Any], env: Mapping[str, str], *, dry_run: bool) -> Runtime:
    llm_enabled = _llm_enabled(config)
    llm = load_symbol(str(config["llm"]["provider"])).from_config(config, env) if llm_enabled else None
    mail_enabled = bool(config["mail"]["enabled"])
    calendar_enabled = bool(config["calendar"]["enabled"])
    weather_enabled = bool(config["weather"]["enabled"])
    quote_block = config.get("daily_quote") if isinstance(config.get("daily_quote"), Mapping) else {}
    quote_enabled = bool(quote_block.get("enabled", False))
    fx_block = config.get("fx") if isinstance(config.get("fx"), Mapping) else {}
    fx_enabled = bool(fx_block.get("enabled", False))
    news_block = config.get("news") if isinstance(config.get("news"), Mapping) else {}
    news_enabled = bool(news_block.get("enabled", False))
    notifier = None
    if not dry_run:
        channel = str(config["delivery"]["channel"])
        notifier = load_symbol(str(config["notifiers"][channel])).from_config(config, env)
    return Runtime(
        config=dict(config),
        llm=llm,
        mail=_optional_source(config, env, "mail") if mail_enabled else None,
        mail_enabled=mail_enabled,
        calendar=_optional_source(config, env, "calendar") if calendar_enabled else None,
        calendar_enabled=calendar_enabled,
        weather=_optional_source(config, env, "weather") if weather_enabled else None,
        weather_enabled=weather_enabled,
        daily_quote=_optional_source(config, env, "daily_quote") if quote_enabled else None,
        daily_quote_enabled=quote_enabled,
        fx=_optional_source(config, env, "fx") if fx_enabled else None,
        fx_enabled=fx_enabled,
        news=_optional_source(config, env, "news") if news_enabled else None,
        news_enabled=news_enabled,
        notifier=notifier,
    )


def _llm_enabled(config: Mapping[str, Any]) -> bool:
    llm = config.get("llm")
    if not isinstance(llm, Mapping):
        return True
    return bool(llm.get("enabled", True))


def _optional_source(config: Mapping[str, Any], env: Mapping[str, str], section: str) -> Any:
    try:
        return load_symbol(str(config[section]["source"])).from_config(config, env)
    except Exception as exc:
        logger.warning("Could not initialize %s (%s)", section, type(exc).__name__)
        logger.debug("Init failed for %s", section, exc_info=True)
        return _FailedSource()


def execute(runtime: Runtime, *, dry_run: bool, today: date | None = None) -> int:
    if today is None:
        today = datetime.now(ZoneInfo(str(runtime.config["timezone"]))).date()
    logger.info("Context ready")
    try:
        if _llm_enabled(runtime.config):
            text = _with_model(runtime, today)
        else:
            text = build_briefing(runtime)
    except Exception as exc:
        logger.error("Briefing was not generated (%s)", type(exc).__name__)
        return 1
    text = correct_city_word(text)
    if dry_run:
        print(text)
        logger.info("Dry run: delivery skipped")
        return 0
    if runtime.notifier is None:
        logger.error("Delivery channel is not configured")
        return 1
    subject = str(runtime.config["briefing"]["subject"])
    try:
        runtime.notifier.send(subject, text)
    except Exception as exc:
        logger.error("Delivery failed (%s)", type(exc).__name__)
        return 1
    logger.info("Briefing delivered")
    return 0


def _with_model(runtime: Runtime, today: date) -> str:
    system_prompt = build_system_prompt(runtime.config)
    user_prompt = collect_user_prompt(runtime, today)
    try:
        written = runtime.llm.complete(system_prompt, user_prompt)
    except Exception as exc:
        return _factual_fallback(runtime, exc)
    written = append_news_links(runtime, written)
    return append_fx(runtime, written)


def _factual_fallback(runtime: Runtime, exc: BaseException) -> str:
    reason = getattr(exc, "reason", None) or type(exc).__name__
    detail = getattr(exc, "detail", None) or str(exc)
    logger.error("Model unavailable (%s): %s", type(exc).__name__, scrub(str(detail)))
    note = f"მოდელი მიუწვდომელია\nმიზეზი: {reason}"
    try:
        body = build_briefing(runtime, quote_note=TRANSLATION_NOTE)
    except Exception as fallback_exc:
        logger.warning("Factual briefing unavailable (%s)", type(fallback_exc).__name__)
        return note
    return body.rstrip() + "\n\n" + note


def _missing_api_key(config: Mapping[str, Any], env: Mapping[str, str]) -> str | None:
    if not _llm_enabled(config):
        return None
    llm = config.get("llm")
    if not isinstance(llm, Mapping):
        return None
    name = llm.get("api_key_env")
    if not isinstance(name, str) or not name.strip():
        return None
    env_name = name.strip()
    if str(env.get(env_name, "")).strip():
        return None
    return f"{env_name} არ არის .env-ში. არაფერი გაიგზავნა."


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if not callable(reconfigure):
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (OSError, ValueError):
            continue


def _logging_level(config: Mapping[str, Any]) -> str:
    logging_block = config.get("logging")
    if isinstance(logging_block, Mapping):
        level = logging_block.get("level", "INFO")
        if isinstance(level, str) and level.strip():
            return level
    return "INFO"


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    drop_blank_secrets(os.environ)
    args = parse_args(argv)
    try:
        config = load_config(Path(args.config))
        config = apply_provider_override(config, args.provider)
        validate_config(config)
        missing = _missing_api_key(config, os.environ)
        if missing:
            print(missing, file=sys.stderr)
            return 2
    except Exception as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 2
    configure_logging(_logging_level(config), collect_secrets(os.environ))
    try:
        runtime = build_runtime(config, os.environ, dry_run=args.dry_run)
    except Exception as exc:
        logger.error("Startup failed (%s)", type(exc).__name__)
        return 1
    return execute(runtime, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())

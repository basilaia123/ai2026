"""Long-polling Telegram bot. The morning cron job stays in main.py."""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.config import load_config, validate_config
from core.redact import collect_secrets, configure_logging, drop_blank_secrets
from main import _configure_stdio, _logging_level, build_runtime
from notifiers.telegram_bot import run_bot

logger = logging.getLogger("morning.bot")


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    import argparse

    from dotenv import load_dotenv

    parser = argparse.ArgumentParser(prog="morning-bot", description="Telegram ბოტი")
    parser.add_argument("--config", default=str(ROOT / "config.yaml"), help="config.yaml-ის გზა")
    args = parser.parse_args(argv)
    load_dotenv(ROOT / ".env")
    drop_blank_secrets(os.environ)
    try:
        config = load_config(Path(args.config))
        validate_config(config)
    except Exception as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 2
    configure_logging(_logging_level(config), collect_secrets(os.environ))
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required", file=sys.stderr)
        return 2
    try:
        runtime = build_runtime(config, os.environ, dry_run=True)
    except Exception as exc:
        logger.error("Startup failed (%s)", type(exc).__name__)
        return 1
    logger.info("Telegram bot starting")
    try:
        run_bot(token, chat_id, runtime)
    except Exception as exc:
        logger.error("Bot stopped (%s)", type(exc).__name__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

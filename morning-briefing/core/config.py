"""Load and check config.yaml. Values stay in the file; this module only reads them."""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def load_config(path: Path) -> dict[str, Any]:
    import yaml

    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("config root must be a mapping")
    return data


def apply_provider_override(config: Mapping[str, Any], provider: str | None) -> dict[str, Any]:
    copied = copy.deepcopy(dict(config))
    if provider is None:
        return copied
    chosen = provider.strip()
    if not chosen:
        raise ValueError("--provider is empty")
    llm = copied.setdefault("llm", {})
    if not isinstance(llm, dict):
        raise ValueError("llm must be a mapping")
    llm["models"] = [chosen]
    llm["enabled"] = True
    return copied


def validate_config(config: Mapping[str, Any]) -> None:
    timezone_name = config.get("timezone")
    if not isinstance(timezone_name, str) or not timezone_name.strip():
        raise ValueError("timezone is required")
    try:
        ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(f"Unknown timezone: {timezone_name}") from exc

    llm = _mapping(config, "llm")
    _nonempty_str(llm, "provider")
    models = llm.get("models")
    if not isinstance(models, list) or not models:
        raise ValueError("llm.models must be a non-empty list")
    if not all(isinstance(item, str) and item.strip() for item in models):
        raise ValueError("llm.models must contain only model strings")

    briefing = _mapping(config, "briefing")
    _nonempty_str(briefing, "system_prompt")
    _nonempty_str(briefing, "subject")
    _positive_int(briefing.get("max_reply_emails"), "briefing.max_reply_emails")
    _positive_int(briefing.get("priority_count"), "briefing.priority_count")

    delivery = _mapping(config, "delivery")
    channel = delivery.get("channel")
    if not isinstance(channel, str) or not channel.strip():
        raise ValueError("delivery.channel is required")
    notifiers = _mapping(config, "notifiers")
    if channel not in notifiers:
        raise ValueError(f"delivery.channel {channel!r} has no entry in notifiers")
    _nonempty_str(notifiers, channel)

    for section in ("mail", "calendar", "weather"):
        block = _mapping(config, section)
        if "enabled" not in block or not isinstance(block["enabled"], bool):
            raise ValueError(f"{section}.enabled must be true or false")
        if block["enabled"]:
            _nonempty_str(block, "source")
    if "daily_quote" in config:
        block = _mapping(config, "daily_quote")
        if "enabled" not in block or not isinstance(block["enabled"], bool):
            raise ValueError("daily_quote.enabled must be true or false")
        if block["enabled"]:
            _nonempty_str(block, "source")
            _nonempty_str(block, "heading")
            _nonempty_str(block, "quote_url")
            _nonempty_str(block, "fact_url")
            _nonempty_str(block, "user_agent")
            timeout = block.get("timeout_seconds")
            if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
                raise ValueError("daily_quote.timeout_seconds must be a positive number")
    if "fx" in config:
        block = _mapping(config, "fx")
        if "enabled" not in block or not isinstance(block["enabled"], bool):
            raise ValueError("fx.enabled must be true or false")
        if block["enabled"]:
            _nonempty_str(block, "source")
            _nonempty_str(block, "user_agent")
            _nonempty_str(block, "nbg_url")
            _nonempty_str(block, "er_url")
            codes = block.get("currencies")
            if not isinstance(codes, list) or not codes or not all(isinstance(item, str) and item.strip() for item in codes):
                raise ValueError("fx.currencies must be a non-empty list of currency codes")
            timeout = block.get("timeout_seconds")
            if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
                raise ValueError("fx.timeout_seconds must be a positive number")
    if "news" in config:
        block = _mapping(config, "news")
        if "enabled" not in block or not isinstance(block["enabled"], bool):
            raise ValueError("news.enabled must be true or false")
        if block["enabled"]:
            _nonempty_str(block, "source")
            _nonempty_str(block, "user_agent")
            feeds = block.get("feeds")
            if not isinstance(feeds, list) or not feeds:
                raise ValueError("news.feeds must be a non-empty list")
            for item in feeds:
                if not isinstance(item, Mapping):
                    raise ValueError("news.feeds entries must have a name and a url")
                if not str(item.get("name") or "").strip() or not str(item.get("url") or "").strip():
                    raise ValueError("news.feeds entries must have a name and a url")
            for key in ("per_feed", "max_items_for_summary", "max_links"):
                value = block.get(key)
                if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                    raise ValueError(f"news.{key} must be a positive integer")
            timeout = block.get("timeout_seconds")
            if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
                raise ValueError("news.timeout_seconds must be a positive number")


def _mapping(config: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = config.get(key)
    if not isinstance(value, Mapping):
        raise ValueError(f"{key} must be a mapping")
    return value


def _nonempty_str(block: Mapping[str, Any], key: str) -> None:
    value = block.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string")


def _positive_int(value: Any, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")

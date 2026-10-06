"""Keep secrets out of log lines."""

from __future__ import annotations

import logging
import os
from typing import Mapping, MutableMapping

_NAME_MARKERS = (
    "PASSWORD",
    "PASSWD",
    "SECRET",
    "TOKEN",
    "API_KEY",
    "_KEY",
    "USERNAME",
    "API_BASE",
    "_URL",
    "CHAT_ID",
)


_ACTIVE_SECRETS: list[str] = []


def is_sensitive_name(name: str) -> bool:
    upper = name.upper()
    return any(marker in upper for marker in _NAME_MARKERS)


def collect_secrets(env: Mapping[str, str], *, min_length: int = 4) -> list[str]:
    found: list[str] = []
    for name, value in env.items():
        if not is_sensitive_name(name):
            continue
        if not isinstance(value, str):
            continue
        text = value.strip()
        if len(text) < min_length:
            continue
        found.append(text)
    unique = sorted(set(found), key=len, reverse=True)
    return unique


def drop_blank_secrets(env: MutableMapping[str, str]) -> None:
    """An empty KEY= line must not look like a configured credential."""
    for name in list(env):
        value = env.get(name, "")
        if is_sensitive_name(name) and isinstance(value, str) and not value.strip():
            env.pop(name, None)


class RedactingFormatter(logging.Formatter):
    def __init__(self, fmt: str, secrets: list[str]) -> None:
        super().__init__(fmt)
        self._secrets = [item for item in secrets if item]

    def format(self, record: logging.LogRecord) -> str:
        text = super().format(record)
        for secret in self._secrets:
            text = text.replace(secret, "***")
        return text


def scrub(text: str) -> str:
    """Hide credential values. Safe to put the result in a log line."""
    redacted = text
    secrets = list(_ACTIVE_SECRETS)
    for name, value in os.environ.items():
        if not is_sensitive_name(name) or not isinstance(value, str):
            continue
        token = value.strip()
        if len(token) >= 4:
            secrets.append(token)
    for secret in sorted(set(secrets), key=len, reverse=True):
        if secret:
            redacted = redacted.replace(secret, "***")
    return redacted


def configure_logging(level_name: str, secrets: list[str]) -> None:
    global _ACTIVE_SECRETS
    _ACTIVE_SECRETS = [item for item in secrets if item]
    level = getattr(logging, str(level_name).upper(), None)
    if not isinstance(level, int):
        level = logging.INFO
    handler = logging.StreamHandler()
    handler._morning_handler = True  # type: ignore[attr-defined]
    handler.setFormatter(
        RedactingFormatter("%(asctime)s %(levelname)s %(name)s: %(message)s", secrets)
    )
    root = logging.getLogger()
    for existing in list(root.handlers):
        if getattr(existing, "_morning_handler", False):
            root.removeHandler(existing)
    root.addHandler(handler)
    root.setLevel(level)
    # Library loggers can echo request URLs. Keep them quiet.
    for name in ("litellm", "httpx", "httpcore", "urllib3", "telegram", "telegram.ext"):
        logging.getLogger(name).setLevel(logging.WARNING)

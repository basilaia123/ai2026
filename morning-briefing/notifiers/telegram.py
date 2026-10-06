"""Deliver the briefing through the Telegram Bot API. Token stays in the environment."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Callable, Mapping

from core.interfaces import Notifier

Opener = Callable[..., Any]


class TelegramNotifier(Notifier):
    def __init__(
        self,
        *,
        token: str,
        chat_id: str,
        timeout: float,
        max_chars: int,
        opener: Opener | None = None,
    ) -> None:
        self._token = token
        self._chat_id = chat_id
        self._timeout = timeout
        self._max_chars = max_chars
        self._opener = opener or urllib.request.urlopen

    def __repr__(self) -> str:
        return "TelegramNotifier(token=***)"

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "TelegramNotifier":
        token = env.get("TELEGRAM_BOT_TOKEN", "").strip()
        chat_id = env.get("TELEGRAM_CHAT_ID", "").strip()
        if not token or not chat_id:
            raise ValueError("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required")
        telegram = config.get("telegram") if isinstance(config.get("telegram"), Mapping) else {}
        return cls(
            token=token,
            chat_id=chat_id,
            timeout=float(telegram.get("timeout_seconds", 20)),
            max_chars=int(telegram.get("max_chars", 3500)),
        )

    def send(self, subject: str, body: str) -> None:
        text = body.rstrip()
        if len(text) > self._max_chars:
            text = text[: self._max_chars].rstrip() + "\n[შეკვეცილია]"
        payload = json.dumps(
            {"chat_id": self._chat_id, "text": f"{subject}\n\n{text}"},
            ensure_ascii=False,
        ).encode("utf-8")
        url = f"https://api.telegram.org/bot{self._token}/sendMessage"
        request = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with self._opener(request, timeout=self._timeout) as response:
                status = getattr(response, "status", None) or response.getcode()
                response.read()
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"Telegram HTTP {exc.code}") from None
        except urllib.error.URLError:
            raise RuntimeError("Telegram HTTP failed") from None
        if status >= 400:
            raise RuntimeError(f"Telegram HTTP {status}")

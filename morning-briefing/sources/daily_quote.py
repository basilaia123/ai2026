"""Daily quote and fact. No API key. Text is copied from the response."""

from __future__ import annotations

import logging
from typing import Any, Mapping

import requests

from core.interfaces import DailyQuote
from core.interfaces import DailyQuoteSource as DailyQuoteSourceBase

logger = logging.getLogger(__name__)


class DailyQuoteSource(DailyQuoteSourceBase):
    def __init__(
        self,
        *,
        quote_url: str,
        fact_url: str,
        timeout: float,
        user_agent: str,
    ) -> None:
        self._quote_url = quote_url
        self._fact_url = fact_url
        self._timeout = timeout
        self._user_agent = user_agent

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "DailyQuoteSource":
        del env
        block = config["daily_quote"]
        return cls(
            quote_url=str(block["quote_url"]),
            fact_url=str(block["fact_url"]),
            timeout=float(block.get("timeout_seconds", 10)),
            user_agent=str(block.get("user_agent", "morning-briefing")),
        )

    def fetch(self) -> DailyQuote:
        quote, author = self._load_quote()
        fact = self._load_fact()
        return DailyQuote(quote=quote, author=author, fact=fact)

    def _load_quote(self) -> tuple[str | None, str]:
        try:
            payload = self._get_json(self._quote_url)
            return quote_from_payload(payload)
        except Exception as exc:
            logger.warning("Quote unavailable (%s)", type(exc).__name__)
            return None, ""

    def _load_fact(self) -> str | None:
        try:
            payload = self._get_json(self._fact_url)
            return fact_from_payload(payload)
        except Exception as exc:
            logger.warning("Fact unavailable (%s)", type(exc).__name__)
            return None

    def _get_json(self, url: str) -> Any:
        try:
            response = requests.get(
                url,
                timeout=self._timeout,
                headers={"User-Agent": self._user_agent, "Accept": "application/json"},
            )
        except requests.Timeout:
            raise RuntimeError("request timed out") from None
        except requests.ConnectionError:
            raise RuntimeError("connection failed") from None
        except requests.RequestException:
            raise RuntimeError("request failed") from None
        if response.status_code >= 400:
            raise RuntimeError(f"HTTP {response.status_code}")
        try:
            return response.json()
        except ValueError:
            raise RuntimeError("payload is not JSON") from None


def quote_from_payload(payload: Any) -> tuple[str, str]:
    if isinstance(payload, list):
        if not payload:
            raise ValueError("quote payload is empty")
        item = payload[0]
    else:
        item = payload
    if not isinstance(item, dict):
        raise ValueError("quote payload is not an object")
    quote = str(item.get("q") or "").strip()
    if not quote:
        raise ValueError("quote text is missing")
    author = str(item.get("a") or "").strip()
    return quote, author


def fact_from_payload(payload: Any) -> str:
    if not isinstance(payload, dict):
        raise ValueError("fact payload is not an object")
    text = str(payload.get("text") or "").strip()
    if not text:
        raise ValueError("fact text is missing")
    return text

"""RSS headlines. Feeds come from config. One failed feed does not stop the others."""

from __future__ import annotations

import logging
from typing import Any, Mapping

import feedparser
import requests

logger = logging.getLogger(__name__)


class NewsSource:
    def __init__(
        self,
        *,
        feeds: list[dict[str, str]],
        per_feed: int,
        timeout: float,
        user_agent: str,
    ) -> None:
        self._feeds = feeds
        self._per_feed = per_feed
        self._timeout = timeout
        self._user_agent = user_agent
        self._cache: list[dict[str, str]] | None = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "NewsSource":
        del env
        block = config["news"]
        feeds = []
        for item in block.get("feeds") or []:
            if not isinstance(item, Mapping):
                continue
            name = str(item.get("name") or "").strip()
            url = str(item.get("url") or "").strip()
            if name and url:
                feeds.append({"name": name, "url": url})
        return cls(
            feeds=feeds,
            per_feed=int(block.get("per_feed", 5)),
            timeout=float(block.get("timeout_seconds", 10)),
            user_agent=str(block.get("user_agent", "morning-briefing/1.0")),
        )

    def fetch(self) -> list[dict[str, str]]:
        if self._cache is None:
            self._cache = fetch_news(
                self._feeds,
                self._per_feed,
                timeout=self._timeout,
                user_agent=self._user_agent,
            )
        return list(self._cache)


def fetch_news(
    feeds: list[Mapping[str, str]],
    per_feed: int,
    *,
    timeout: float = 10,
    user_agent: str = "morning-briefing/1.0",
) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for feed in feeds:
        name = str(feed.get("name") or "").strip()
        url = str(feed.get("url") or "").strip()
        if not name or not url:
            continue
        try:
            batch = _one_feed(name, url, per_feed, timeout, user_agent)
        except Exception as exc:
            logger.warning("News feed failed (%s)", type(exc).__name__)
            continue
        for item in batch:
            if item["link"] in seen:
                continue
            seen.add(item["link"])
            items.append(item)
    return items


def _one_feed(name: str, url: str, per_feed: int, timeout: float, user_agent: str) -> list[dict[str, str]]:
    payload = _get_bytes(url, timeout=timeout, user_agent=user_agent)
    parsed = feedparser.parse(payload)
    entries = getattr(parsed, "entries", None) or []
    if getattr(parsed, "bozo", False) and not entries:
        raise RuntimeError("payload is not XML")
    items: list[dict[str, str]] = []
    for entry in entries:
        if len(items) >= per_feed:
            break
        title = str(getattr(entry, "title", "") or "").strip()
        link = str(getattr(entry, "link", "") or "").strip()
        if not title or not link:
            continue
        items.append({"title": title, "link": link, "source": name})
    return items


def _get_bytes(url: str, *, timeout: float, user_agent: str) -> bytes:
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": user_agent, "Accept": "application/rss+xml, application/xml, text/xml"},
        )
    except requests.Timeout:
        raise RuntimeError("request timed out") from None
    except requests.ConnectionError:
        raise RuntimeError("connection failed") from None
    except requests.RequestException:
        raise RuntimeError("request failed") from None
    if response.status_code >= 400:
        raise RuntimeError(f"HTTP {response.status_code}")
    return response.content or b""


def format_headlines(items: list[Mapping[str, str]], limit: int) -> str:
    lines = ["📰 სიახლეები"]
    shown = 0
    for item in items:
        if shown >= limit:
            break
        title = str(item.get("title") or "").strip()
        link = str(item.get("link") or "").strip()
        source = str(item.get("source") or "").strip()
        if not title or not link:
            continue
        lines.append(f"• {title} ({source})")
        lines.append(link)
        shown += 1
    if shown == 0:
        return "სიახლეები: მიუწვდომელია"
    return "\n".join(lines)

"""Swappable boundaries. A new provider is a new module plus a config path."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Meeting:
    start_label: str
    title: str
    with_whom: str
    sort_key: str


@dataclass(frozen=True)
class MailItem:
    sender: str
    subject: str
    received: str
    excerpt: str


@dataclass(frozen=True)
class WeatherSnapshot:
    text: str


@dataclass(frozen=True)
class DailyQuote:
    quote: str | None
    author: str
    fact: str | None


class LLMProvider(ABC):
    @abstractmethod
    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Return plain text. No tools and no function calls."""


class MailSource(ABC):
    @abstractmethod
    def fetch(self) -> list[MailItem]:
        """Read recent messages. Must not change mailbox state."""


class CalendarSource(ABC):
    @abstractmethod
    def fetch(self, day: date) -> list[Meeting]:
        """Read events for one local day. Must not create or edit events."""


class WeatherSource(ABC):
    @abstractmethod
    def fetch(self) -> WeatherSnapshot:
        """Return factual weather lines."""


class DailyQuoteSource(ABC):
    @abstractmethod
    def fetch(self) -> DailyQuote:
        """Return today's quote and fact. A missing part is None, not invented text."""


class FxSource(ABC):
    @abstractmethod
    def fetch(self) -> dict | None:
        """Official rates, or None when every source failed. Do not invent a rate."""


class Notifier(ABC):
    @abstractmethod
    def send(self, subject: str, body: str) -> None:
        """Deliver an already written briefing."""

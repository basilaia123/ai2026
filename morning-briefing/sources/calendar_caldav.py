"""Read-only CalDAV. Only principal, calendar list, and search are used."""

from __future__ import annotations

import logging
from datetime import date, datetime, time, timedelta
from typing import Any, Callable, Mapping
from zoneinfo import ZoneInfo

from core.interfaces import CalendarSource, Meeting
from sources.calendar_ics import dedupe_meetings, events_from_ical

logger = logging.getLogger(__name__)

ClientFactory = Callable[[], Any]


class CalDAVCalendarSource(CalendarSource):
    def __init__(
        self,
        *,
        url: str,
        username: str,
        password: str,
        timezone_name: str,
        timeout: float,
        client_factory: ClientFactory | None = None,
    ) -> None:
        self._url = url
        self._username = username
        self._password = password
        self._timezone_name = timezone_name
        self._timeout = timeout
        self._client_factory = client_factory or self._default_client

    def __repr__(self) -> str:
        return "CalDAVCalendarSource(url=***)"

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "CalDAVCalendarSource":
        calendar = config["calendar"]
        url = str(env.get("CALDAV_URL") or calendar.get("url") or "").strip()
        username = str(env.get("CALDAV_USERNAME") or "").strip()
        password = str(env.get("CALDAV_PASSWORD") or "")
        if not url or not username or not password:
            raise ValueError("CALDAV_URL, CALDAV_USERNAME and CALDAV_PASSWORD are required")
        return cls(
            url=url,
            username=username,
            password=password,
            timezone_name=str(config["timezone"]),
            timeout=float(calendar.get("timeout_seconds", 20)),
        )

    def fetch(self, day: date) -> list[Meeting]:
        client = self._client_factory()
        try:
            principal = client.principal()
            calendars = principal.calendars()
            tz = ZoneInfo(self._timezone_name)
            window_start = datetime.combine(day, time.min, tzinfo=tz)
            window_end = window_start + timedelta(days=1)
            meetings: list[Meeting] = []
            for calendar in calendars:
                found = calendar.search(
                    start=window_start,
                    end=window_end,
                    event=True,
                    expand=True,
                )
                for event in found:
                    meetings.extend(events_from_ical(event.data, day, self._timezone_name))
            logger.info("Calendar events read: %s", len(meetings))
            return dedupe_meetings(meetings)
        finally:
            close = getattr(client, "close", None)
            if callable(close):
                try:
                    close()
                except Exception:
                    logger.debug("CalDAV close failed", exc_info=True)

    def _default_client(self) -> Any:
        import caldav

        return caldav.DAVClient(
            url=self._url,
            username=self._username,
            password=self._password,
            timeout=self._timeout,
        )

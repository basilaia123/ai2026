"""Calendar helpers for ICS bytes. Read-only: this module never writes events."""

from __future__ import annotations

import logging
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta
from typing import Any, Mapping
from zoneinfo import ZoneInfo

from core.interfaces import CalendarSource, Meeting

logger = logging.getLogger(__name__)


def events_from_ical(raw: bytes | str, day: date, tz_name: str) -> list[Meeting]:
    from icalendar import Calendar

    if isinstance(raw, str):
        raw = raw.encode("utf-8")
    calendar = Calendar.from_ical(raw)
    tz = ZoneInfo(tz_name)
    components = list(calendar.walk("VEVENT"))
    recurring = any(component.get("RRULE") or component.get("RDATE") for component in components)
    if recurring:
        instances = _expand(calendar, components, day, tz)
    else:
        instances = [component for component in components if _overlaps(component, day, tz)]
    meetings: list[Meeting] = []
    for component in instances:
        try:
            meetings.append(_to_meeting(component, tz))
        except Exception as exc:
            logger.warning("Skipped calendar event (%s)", type(exc).__name__)
            logger.debug("Calendar event parse failed", exc_info=True)
    return dedupe_meetings(meetings)


def dedupe_meetings(meetings: list[Meeting]) -> list[Meeting]:
    seen: set[tuple[str, str, str]] = set()
    unique: list[Meeting] = []
    for item in sorted(meetings, key=lambda meeting: (meeting.sort_key, meeting.title)):
        key = (item.sort_key, item.title, item.with_whom)
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def _expand(calendar: Any, components: list[Any], day: date, tz: ZoneInfo) -> list[Any]:
    try:
        import recurring_ical_events
    except ImportError:
        logger.warning("recurring-ical-events is not installed; recurring events are skipped")
        return [component for component in components if not component.get("RRULE") and _overlaps(component, day, tz)]
    start = datetime.combine(day, time.min, tzinfo=tz)
    end = start + timedelta(days=1)
    try:
        return list(recurring_ical_events.of(calendar).between(start, end))
    except Exception as exc:
        logger.warning("Recurrence expansion failed (%s)", type(exc).__name__)
        logger.debug("Recurrence expansion failed", exc_info=True)
        return [component for component in components if not component.get("RRULE") and _overlaps(component, day, tz)]


def _overlaps(component: Any, day: date, tz: ZoneInfo) -> bool:
    start, end = _span(component, tz)
    window_start = datetime.combine(day, time.min, tzinfo=tz)
    window_end = window_start + timedelta(days=1)
    return start < window_end and end > window_start


def _span(component: Any, tz: ZoneInfo) -> tuple[datetime, datetime]:
    start_prop = component.get("DTSTART")
    if start_prop is None:
        raise ValueError("event has no DTSTART")
    start, _all_day = _to_local(start_prop.dt, tz)
    end_prop = component.get("DTEND")
    if end_prop is not None:
        end, _ = _to_local(end_prop.dt, tz)
        return start, end
    duration = component.get("DURATION")
    if duration is not None:
        return start, start + duration.dt
    if _all_day:
        return start, start + timedelta(days=1)
    return start, start


def _to_meeting(component: Any, tz: ZoneInfo) -> Meeting:
    start, end = _span(component, tz)
    start_local = start.astimezone(tz)
    end_local = end.astimezone(tz)
    start_prop = component.get("DTSTART")
    clock_start = start_prop is not None and isinstance(start_prop.dt, datetime)
    spans_full_days = (
        start_local.hour == 0
        and start_local.minute == 0
        and end_local.hour == 0
        and end_local.minute == 0
        and end_local - start_local >= timedelta(days=1)
    )
    if not clock_start or spans_full_days:
        label = "მთელი დღე"
    else:
        label = start_local.strftime("%H:%M")
        end_prop = component.get("DTEND")
        end_is_clock = end_prop is not None and isinstance(end_prop.dt, datetime)
        end_label = end_local.strftime("%H:%M")
        if end_is_clock and end_label != label:
            label = f"{label}-{end_label}"
    summary = component.get("SUMMARY")
    title = " ".join(str(summary).split()) if summary else "უსათაურო"
    people = _people(component)
    return Meeting(
        start_label=label,
        title=title or "უსათაურო",
        with_whom=people,
        sort_key=start.isoformat(),
    )


def _to_local(value: Any, tz: ZoneInfo) -> tuple[datetime, bool]:
    if isinstance(value, datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=tz), False
        return value.astimezone(tz), False
    if isinstance(value, date):
        return datetime.combine(value, time.min, tzinfo=tz), True
    raise TypeError("unsupported date value")


def _people(component: Any) -> str:
    names: list[str] = []
    organizer = component.get("ORGANIZER")
    if organizer is not None:
        names.append(_person(organizer))
    for attendee in _properties(component, "ATTENDEE"):
        names.append(_person(attendee))
    unique: list[str] = []
    for name in names:
        cleaned = " ".join(name.split())
        if cleaned and cleaned not in unique:
            unique.append(cleaned)
    if not unique:
        return "მითითებული არ არის"
    return ", ".join(unique[:8])


def _properties(component: Any, name: str) -> list[Any]:
    found: list[Any] = []
    try:
        pairs = list(component.property_items())
    except Exception:
        pairs = []
    for key, value in pairs:
        if str(key).upper() != name:
            continue
        if isinstance(value, list):
            found.extend(value)
        else:
            found.append(value)
    if found:
        return found
    value = component.get(name)
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _person(value: Any) -> str:
    params = getattr(value, "params", None)
    if params is not None and params.get("CN"):
        return str(params.get("CN"))
    text = str(value)
    if text.lower().startswith("mailto:"):
        text = text[7:]
    return text


class IcsCalendarSource(CalendarSource):
    """Read-only HTTPS/HTTP fetch of an ICS feed."""

    def __init__(
        self,
        *,
        url: str,
        timezone_name: str,
        timeout: float,
        max_bytes: int,
        opener: Any = None,
    ) -> None:
        self._url = url
        self._timezone_name = timezone_name
        self._timeout = timeout
        self._max_bytes = max_bytes
        self._opener = opener or urllib.request.urlopen

    def __repr__(self) -> str:
        return "IcsCalendarSource(url=***)"

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "IcsCalendarSource":
        calendar = config["calendar"]
        url = str(env.get("ICS_URL") or calendar.get("url") or "").strip()
        if not url:
            raise ValueError("ICS_URL is required")
        return cls(
            url=url,
            timezone_name=str(config["timezone"]),
            timeout=float(calendar.get("timeout_seconds", 20)),
            max_bytes=int(calendar.get("max_bytes", 5_000_000)),
        )

    def fetch(self, day: date) -> list[Meeting]:
        request = urllib.request.Request(self._url, headers={"User-Agent": "morning-briefing"})
        try:
            with self._opener(request, timeout=self._timeout) as response:
                raw = response.read(self._max_bytes + 1)
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"Calendar HTTP {exc.code}") from None
        except urllib.error.URLError:
            raise RuntimeError("Calendar HTTP failed") from None
        if len(raw) > self._max_bytes:
            raise RuntimeError("Calendar feed is too large")
        meetings = events_from_ical(raw, day, self._timezone_name)
        logger.info("Calendar events read: %s", len(meetings))
        return meetings

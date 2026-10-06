"""Calendar parsing and the read-only CalDAV/ICS adapters."""

import urllib.error
from datetime import date
from pathlib import Path

import pytest

from sources.calendar_caldav import CalDAVCalendarSource
from sources.calendar_ics import IcsCalendarSource, events_from_ical

ROOT = Path(__file__).resolve().parents[1]
DAY = date(2026, 10, 6)

ICS = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//morning-briefing//test//EN
BEGIN:VEVENT
UID:meet-1@example.test
DTSTART:20261006T060000Z
DTEND:20261006T070000Z
SUMMARY:გეგმარება
ORGANIZER;CN=ანა:mailto:ana@example.com
ATTENDEE;CN=გიორგი:mailto:giorgi@example.com
ATTENDEE;CN=ნინო:mailto:nino@example.com
END:VEVENT
BEGIN:VEVENT
UID:tomorrow@example.test
DTSTART:20261007T060000Z
DTEND:20261007T070000Z
SUMMARY:ხვალინდელი
END:VEVENT
BEGIN:VEVENT
UID:all-day@example.test
DTSTART;VALUE=DATE:20261006
DTEND;VALUE=DATE:20261007
SUMMARY:კონფერენცია
END:VEVENT
END:VCALENDAR
"""

WEEKLY = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//morning-briefing//test//EN
BEGIN:VEVENT
UID:weekly@example.test
DTSTART:20260929T060000Z
DTEND:20260929T070000Z
RRULE:FREQ=WEEKLY
SUMMARY:ყოველკვირეული
END:VEVENT
END:VCALENDAR
"""


def test_ics_keeps_today_and_names_people():
    meetings = events_from_ical(ICS, DAY, "Asia/Tbilisi")
    titles = [item.title for item in meetings]
    assert titles == ["კონფერენცია", "გეგმარება"]
    assert meetings[0].start_label == "მთელი დღე"
    planning = meetings[1]
    assert planning.start_label == "10:00-11:00"
    assert "ანა" in planning.with_whom
    assert "გიორგი" in planning.with_whom
    assert "ნინო" in planning.with_whom
    assert "ხვალინდელი" not in titles


def test_weekly_event_is_included_on_the_next_occurrence():
    pytest.importorskip("recurring_ical_events")
    meetings = events_from_ical(WEEKLY, DAY, "Asia/Tbilisi")
    assert [item.title for item in meetings] == ["ყოველკვირეული"]
    assert meetings[0].start_label == "10:00-11:00"


class _Event:
    def __init__(self, data: str):
        self.data = data


class _Calendar:
    def __init__(self):
        self.kwargs = None

    def search(self, **kwargs):
        self.kwargs = kwargs
        return [_Event(ICS)]

    def save_event(self, *args, **kwargs):
        raise AssertionError("save_event is a write")


class _Principal:
    def __init__(self, calendar):
        self._calendar = calendar

    def calendars(self):
        return [self._calendar]


class _Client:
    def __init__(self, calendar):
        self._calendar = calendar
        self.closed = False

    def principal(self):
        return _Principal(self._calendar)

    def close(self):
        self.closed = True


def test_caldav_search_is_read_only():
    calendar = _Calendar()
    client = _Client(calendar)
    source = CalDAVCalendarSource(
        url="https://cal.example.test/user",
        username="user",
        password="secret-password",
        timezone_name="Asia/Tbilisi",
        timeout=5,
        client_factory=lambda: client,
    )
    meetings = source.fetch(DAY)
    assert client.closed is True
    assert calendar.kwargs["event"] is True
    assert calendar.kwargs["expand"] is True
    assert [item.title for item in meetings] == ["კონფერენცია", "გეგმარება"]
    assert "secret-password" not in repr(source)


def test_ics_http_error_does_not_include_the_url():
    token = "super-secret-token"

    def opener(request, timeout=0):
        raise urllib.error.URLError(token)

    source = IcsCalendarSource(
        url=f"https://example.test/secret.ics?token={token}",
        timezone_name="Asia/Tbilisi",
        timeout=5,
        max_bytes=1000,
        opener=opener,
    )
    with pytest.raises(RuntimeError) as caught:
        source.fetch(DAY)
    assert token not in str(caught.value)
    assert caught.value.__suppress_context__ is True


def test_calendar_modules_have_no_write_calls():
    for name in ("calendar_ics.py", "calendar_caldav.py"):
        text = (ROOT / "sources" / name).read_text(encoding="utf-8")
        for banned in ("save_event", "add_event", ".delete(", ".save("):
            assert banned not in text

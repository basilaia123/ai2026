"""Read-only IMAP behaviour, with a fake server."""

from datetime import date
from email.message import EmailMessage
from pathlib import Path

import pytest

from sources.mail_imap import ImapMailSource, imap_since

ROOT = Path(__file__).resolve().parents[1]


class FakeIMAP:
    def __init__(self, raw: bytes):
        self.raw = raw
        self.readonly = None
        self.fetch_spec = None
        self.logged_out = False
        self.search_args = None

    def login(self, username, password):
        self.username = username

    def select(self, mailbox, readonly=False):
        self.mailbox = mailbox
        self.readonly = readonly
        return "OK", [b"1"]

    def search(self, charset, *criteria):
        self.search_args = (charset, criteria)
        return "OK", [b"1"]

    def fetch(self, msg_id, spec):
        self.fetch_spec = spec
        return "OK", [(b"1 (BODY[] {1}", self.raw), b")"]

    def store(self, *args, **kwargs):
        raise AssertionError("store is a write")

    def expunge(self, *args, **kwargs):
        raise AssertionError("expunge is a write")

    def append(self, *args, **kwargs):
        raise AssertionError("append is a write")

    def logout(self):
        self.logged_out = True


def _raw_message() -> bytes:
    message = EmailMessage()
    message["From"] = "ანა <ana@example.com>"
    message["To"] = "me@example.com"
    message["Subject"] = "ანგარიში"
    message["Date"] = "Tue, 06 Oct 2026 05:30:00 +0000"
    message.set_content("გთხოვ, ხვალამდე გამომიგზავნო ანგარიში.")
    return message.as_bytes()


def test_imap_date_is_english_regardless_of_locale():
    assert imap_since(date(2026, 10, 6)) == "06-Oct-2026"


def test_fetch_is_readonly_and_does_not_mark_seen():
    fake = FakeIMAP(_raw_message())
    source = ImapMailSource(
        host="imap.example.test",
        port=993,
        username="user",
        password="secret-password",
        folder="INBOX",
        security="ssl",
        lookback_days=2,
        max_messages=5,
        body_chars=200,
        timezone_name="Asia/Tbilisi",
        timeout=5,
        unseen_only=False,
        imap_factory=lambda: fake,
    )
    items = source.fetch()
    assert fake.readonly is True
    assert "PEEK" in fake.fetch_spec
    assert fake.logged_out is True
    assert len(items) == 1
    assert items[0].sender == "ანა <ana@example.com>"
    assert items[0].subject == "ანგარიში"
    assert items[0].received == "2026-10-06 09:30"
    assert "ანგარიში" in items[0].excerpt
    assert "secret-password" not in repr(source)


def test_source_file_has_no_write_calls():
    text = (ROOT / "sources" / "mail_imap.py").read_text(encoding="utf-8")
    for banned in (".store(", ".expunge(", ".copy(", "client.append("):
        assert banned not in text
    assert "readonly=True" in text
    assert "BODY.PEEK[]" in text


def test_gmail_app_password_spaces_are_removed():
    source = ImapMailSource.from_config(
        {
            "mail": {
                "host": "imap.gmail.com",
                "port": 993,
                "lookback_days": 2,
                "max_messages": 5,
                "body_chars": 100,
            },
            "timezone": "Asia/Tbilisi",
        },
        {"IMAP_USERNAME": "user@gmail.com", "IMAP_PASSWORD": "abcd efgh ijkl mnop"},
    )
    assert source._password == "abcdefghijklmnop"
    assert source._username == "user@gmail.com"
    assert source._host == "imap.gmail.com"


def test_missing_credentials_raise_before_connect():
    with pytest.raises(ValueError):
        ImapMailSource.from_config(
            {"mail": {"host": "imap.example.test", "port": 993, "lookback_days": 1, "max_messages": 1, "body_chars": 10}, "timezone": "Asia/Tbilisi"},
            {},
        )

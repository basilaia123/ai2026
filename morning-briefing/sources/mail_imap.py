"""Read-only IMAP. Uses BODY.PEEK and a readonly mailbox so flags stay unchanged."""

from __future__ import annotations

import email
import imaplib
import logging
from datetime import date, datetime, timedelta
from email import policy
from email.message import EmailMessage
from html import unescape
from typing import Any, Callable, Mapping
from zoneinfo import ZoneInfo
import re

from core.interfaces import MailItem, MailSource

logger = logging.getLogger(__name__)

_MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
_TAG_RE = re.compile(r"(?is)<(script|style).*?>.*?</\1>")
_HTML_RE = re.compile(r"(?s)<[^>]+>")

ImapFactory = Callable[[], imaplib.IMAP4]


def imap_since(value: date) -> str:
    """IMAP dates require English month names, independent of the OS locale."""
    return f"{value.day:02d}-{_MONTHS[value.month - 1]}-{value.year}"


class ImapMailSource(MailSource):
    def __init__(
        self,
        *,
        host: str,
        port: int,
        username: str,
        password: str,
        folder: str,
        security: str,
        lookback_days: int,
        max_messages: int,
        body_chars: int,
        timezone_name: str,
        timeout: float,
        unseen_only: bool,
        imap_factory: ImapFactory | None = None,
    ) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._folder = folder
        self._security = security
        self._lookback_days = lookback_days
        self._max_messages = max_messages
        self._body_chars = body_chars
        self._timezone_name = timezone_name
        self._timeout = timeout
        self._unseen_only = unseen_only
        self._imap_factory = imap_factory

    def __repr__(self) -> str:
        return f"ImapMailSource(host={self._host!r}, folder={self._folder!r})"

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "ImapMailSource":
        mail = config["mail"]
        username = env.get("IMAP_USERNAME", "").strip()
        # Gmail shows the App Password in groups of four. Spaces are not part of it.
        password = "".join(env.get("IMAP_PASSWORD", "").split())
        if not username or not password:
            raise ValueError("IMAP_USERNAME and IMAP_PASSWORD are required")
        return cls(
            host=str(mail["host"]),
            port=int(mail["port"]),
            username=username,
            password=password,
            folder=str(mail.get("folder", "INBOX")),
            security=str(mail.get("security", "ssl")),
            lookback_days=int(mail["lookback_days"]),
            max_messages=int(mail["max_messages"]),
            body_chars=int(mail["body_chars"]),
            timezone_name=str(config["timezone"]),
            timeout=float(mail.get("timeout_seconds", 20)),
            unseen_only=bool(mail.get("unseen_only", False)),
        )

    def fetch(self) -> list[MailItem]:
        client = self._connect()
        try:
            status, _ = client.select(self._folder, readonly=True)
            if status != "OK":
                raise RuntimeError(f"IMAP select failed ({status})")
            today = datetime.now(ZoneInfo(self._timezone_name)).date()
            since = today - timedelta(days=self._lookback_days)
            criteria: list[str] = ["SINCE", imap_since(since)]
            if self._unseen_only:
                criteria.insert(0, "UNSEEN")
            status, data = client.search(None, *criteria)
            if status != "OK" or not data or data[0] is None:
                raise RuntimeError(f"IMAP search failed ({status})")
            ids = data[0].split()
            chosen = ids[-self._max_messages :]
            chosen.reverse()
            items: list[MailItem] = []
            for msg_id in chosen:
                try:
                    items.append(self._read_one(client, msg_id))
                except Exception as exc:
                    logger.warning("Skipped one message (%s)", type(exc).__name__)
                    logger.debug("Message parse failed", exc_info=True)
            if chosen and not items:
                raise RuntimeError("IMAP messages could not be read")
            logger.info("Mail messages read: %s", len(items))
            return items
        finally:
            try:
                client.logout()
            except Exception:
                logger.debug("IMAP logout failed", exc_info=True)

    def _connect(self) -> imaplib.IMAP4:
        if self._imap_factory is not None:
            client = self._imap_factory()
        elif self._security == "ssl":
            client = imaplib.IMAP4_SSL(self._host, self._port, timeout=self._timeout)
        elif self._security == "starttls":
            client = imaplib.IMAP4(self._host, self._port, timeout=self._timeout)
            client.starttls()
        else:
            raise ValueError("mail.security must be ssl or starttls")
        client.login(self._username, self._password)
        return client

    def _read_one(self, client: imaplib.IMAP4, msg_id: bytes) -> MailItem:
        # BODY.PEEK does not set the Seen flag. Combined with readonly select.
        status, payload = client.fetch(msg_id, "(BODY.PEEK[])")
        if status != "OK":
            raise RuntimeError(f"IMAP fetch failed ({status})")
        raw = _rfc822(payload)
        if raw is None:
            raise RuntimeError("IMAP fetch returned no body")
        message = email.message_from_bytes(raw, policy=policy.default)
        if not isinstance(message, EmailMessage):
            raise RuntimeError("Unexpected message type")
        return MailItem(
            sender=_sender(message),
            subject=_subject(message),
            received=_received(message, self._timezone_name),
            excerpt=_excerpt(message, self._body_chars),
        )


def _rfc822(payload: Any) -> bytes | None:
    if not payload:
        return None
    for item in payload:
        if isinstance(item, tuple) and len(item) >= 2 and isinstance(item[1], (bytes, bytearray)):
            return bytes(item[1])
    return None


def _sender(message: EmailMessage) -> str:
    raw = str(message.get("From", "") or "")
    name, addr = email.utils.parseaddr(raw)
    name = " ".join(name.split())
    if name and addr:
        return f"{name} <{addr}>"
    return name or addr or " ".join(raw.split()) or "უცნობი"


def _subject(message: EmailMessage) -> str:
    text = " ".join(str(message.get("Subject", "") or "").split())
    return text or "(თემის გარეშე)"


def _received(message: EmailMessage, timezone_name: str) -> str:
    raw = message.get("Date")
    if not raw:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(str(raw))
    except (TypeError, ValueError, IndexError):
        return ""
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=ZoneInfo("UTC"))
    local = parsed.astimezone(ZoneInfo(timezone_name))
    return local.strftime("%Y-%m-%d %H:%M")


def _excerpt(message: EmailMessage, limit: int) -> str:
    try:
        part = message.get_body(preferencelist=("plain", "html"))
    except Exception:
        return ""
    if part is None:
        return ""
    try:
        content = part.get_content()
    except Exception:
        return ""
    if not isinstance(content, str):
        return ""
    if part.get_content_type() == "text/html":
        content = _html_to_text(content)
    text = " ".join(content.split())
    if len(text) > limit:
        return text[:limit].rstrip() + "..."
    return text


def _html_to_text(value: str) -> str:
    without_code = _TAG_RE.sub(" ", value)
    without_tags = _HTML_RE.sub(" ", without_code)
    return unescape(without_tags)

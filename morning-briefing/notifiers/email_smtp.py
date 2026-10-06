"""Deliver the briefing by SMTP. This does not touch the read-only mailbox."""

from __future__ import annotations

import smtplib
from email.message import EmailMessage
from typing import Any, Callable, Mapping

from core.interfaces import Notifier

Connect = Callable[[], Any]


class SmtpNotifier(Notifier):
    def __init__(
        self,
        *,
        host: str,
        port: int,
        username: str,
        password: str,
        sender: str,
        recipient: str,
        security: str,
        timeout: float,
        connect: Connect | None = None,
    ) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._sender = sender
        self._recipient = recipient
        self._security = security
        self._timeout = timeout
        self._connect = connect or self._default_connect

    def __repr__(self) -> str:
        return f"SmtpNotifier(host={self._host!r})"

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "SmtpNotifier":
        smtp = config.get("smtp")
        if not isinstance(smtp, Mapping):
            raise ValueError("smtp settings are required when delivery channel is email")
        username = (env.get("SMTP_USERNAME") or env.get("IMAP_USERNAME") or "").strip()
        password = "".join((env.get("SMTP_PASSWORD") or env.get("IMAP_PASSWORD") or "").split())
        sender = (env.get("SMTP_FROM") or username).strip()
        recipient = env.get("SMTP_TO", "").strip()
        if not username or not password or not sender or not recipient:
            raise ValueError("SMTP_USERNAME, SMTP_PASSWORD, SMTP_FROM and SMTP_TO are required")
        return cls(
            host=str(smtp["host"]),
            port=int(smtp["port"]),
            username=username,
            password=password,
            sender=sender,
            recipient=recipient,
            security=str(smtp.get("security", "starttls")),
            timeout=float(smtp.get("timeout_seconds", 20)),
        )

    def send(self, subject: str, body: str) -> None:
        message = EmailMessage()
        message["From"] = self._sender
        message["To"] = self._recipient
        message["Subject"] = subject
        message.set_content(body, charset="utf-8")
        with self._connect() as client:
            client.login(self._username, self._password)
            client.send_message(message)

    def _default_connect(self) -> Any:
        if self._security == "ssl":
            return smtplib.SMTP_SSL(self._host, self._port, timeout=self._timeout)
        if self._security == "starttls":
            client = smtplib.SMTP(self._host, self._port, timeout=self._timeout)
            client.ehlo()
            client.starttls()
            client.ehlo()
            return client
        raise ValueError("smtp.security must be ssl or starttls")

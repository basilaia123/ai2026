"""Command parsing, the menu, and the chat-id gate. No Telegram network calls."""

import asyncio

from core.briefing import Runtime
from notifiers.telegram_bot import (
    COMMANDS,
    FAILURE_TEXT,
    TELEGRAM_TEXT_LIMIT,
    BotCommand,
    button_rows,
    dispatch,
    handle_callback,
    menu_commands,
    parse_command,
    serve_callback,
    split_telegram,
)
from tests.test_briefing import _runtime


def test_parse_command_strips_bot_suffix_and_args():
    assert parse_command("/brief") == "brief"
    assert parse_command("/Brief@MorningBot ახლა") == "brief"
    assert parse_command("  /FX ") == "fx"
    assert parse_command("ამინდი") is None
    assert parse_command("") is None
    assert parse_command("/") is None


def test_registry_lists_the_briefing_commands():
    names = [item.name for item in COMMANDS]
    assert "start" in names
    assert [item.name for item in menu_commands()] == ["brief", "weather", "fx", "quote", "news", "help"]
    assert button_rows() == [
        [("📋 ბრიფინგი", "brief")],
        [("🌤 ამინდი", "weather"), ("💱 კურსი", "fx")],
        [("💬 ციტატა და ფაქტი", "quote")],
        [("📰 სიახლეები", "news")],
    ]


def test_foreign_chat_is_ignored_and_does_not_call_the_handler():
    def boom(_runtime: Runtime) -> str:
        raise AssertionError("handler ran for a foreign chat")

    commands = (BotCommand("weather", "ამინდი", boom),)
    assert dispatch("/weather", chat_id=111, allowed_chat_id="222", runtime=_runtime(), commands=commands) is None
    assert dispatch("/weather", chat_id="222", allowed_chat_id="", runtime=_runtime(), commands=commands) is None


def test_allowed_chat_runs_only_the_named_section():
    runtime = _runtime()
    text = dispatch("/weather", chat_id="42", allowed_chat_id="42", runtime=runtime)
    assert text is not None
    assert "12.0°C" in text
    assert "ციტატა:" not in text
    help_reply = dispatch("/start", chat_id=42, allowed_chat_id="42", runtime=runtime)
    assert help_reply is not None
    assert "/brief" in help_reply
    assert "/fx" in help_reply


def test_handler_error_is_a_short_message_without_the_exception_text():
    def boom(_runtime: Runtime) -> str:
        raise RuntimeError("token-should-stay-hidden")

    commands = (BotCommand("brief", "სრული ბრიფინგი", boom),)
    text = dispatch("/brief", "9", "9", _runtime(), commands=commands)
    assert text == FAILURE_TEXT
    assert "token-should-stay-hidden" not in (text or "")


def test_foreign_callback_is_ignored():
    def boom(_runtime: Runtime) -> str:
        raise AssertionError("callback ran for a foreign chat")

    commands = (BotCommand("weather", "ამინდი", boom, button="🌤 ამინდი", row=1),)
    answered: list[bool] = []
    sent: list[str] = []

    async def answer() -> None:
        answered.append(True)

    async def send(text: str) -> None:
        sent.append(text)

    asyncio.run(
        serve_callback(
            chat_id=111,
            data="weather",
            allowed_chat_id="222",
            runtime=_runtime(),
            answer=answer,
            send=send,
            commands=commands,
        )
    )
    assert handle_callback("weather", 111, "222", _runtime(), commands) is None
    assert answered == []
    assert sent == []


def test_allowed_callback_answers_and_uses_the_command():
    answered: list[bool] = []
    sent: list[str] = []

    async def answer() -> None:
        answered.append(True)

    async def send(text: str) -> None:
        sent.append(text)

    asyncio.run(
        serve_callback(
            chat_id="42",
            data="weather",
            allowed_chat_id="42",
            runtime=_runtime(),
            answer=answer,
            send=send,
        )
    )
    assert answered == [True]
    assert sent and "12.0°C" in sent[0]
    assert "ციტატა:" not in sent[0]


def test_unknown_command_for_the_owner_gets_the_list():
    text = dispatch("/missing", "7", "7", _runtime())
    assert text is not None
    assert "ასეთი ბრძანება არ არის." in text
    assert "/weather" in text


def test_split_respects_the_telegram_limit():
    body = ("ხაზი\n" * 2000).strip()
    parts = split_telegram(body, limit=TELEGRAM_TEXT_LIMIT)
    assert len(parts) > 1
    assert all(len(part) <= TELEGRAM_TEXT_LIMIT for part in parts)
    assert "\n".join(parts) == body

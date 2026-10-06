"""Interactive Telegram commands. Only the chat id from the environment is answered."""

from __future__ import annotations

import logging
from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass

from core.briefing import Runtime, build_briefing

logger = logging.getLogger(__name__)

TELEGRAM_TEXT_LIMIT = 4096
FAILURE_TEXT = "ვერ შესრულდა. სცადე თავიდან."
UNKNOWN_TEXT = "ასეთი ბრძანება არ არის."


@dataclass(frozen=True)
class BotCommand:
    name: str
    description: str
    handler: Callable[[Runtime], str]
    menu: bool = True
    show_buttons: bool = False
    button: str | None = None
    row: int | None = None


def cmd_help(runtime: Runtime) -> str:
    del runtime
    return help_text()


def cmd_brief(runtime: Runtime) -> str:
    return build_briefing(runtime, sections=("weather", "quote", "news", "fx"))


def cmd_weather(runtime: Runtime) -> str:
    return build_briefing(runtime, sections=("weather",))


def cmd_fx(runtime: Runtime) -> str:
    return build_briefing(runtime, sections=("fx",))


def cmd_quote(runtime: Runtime) -> str:
    return build_briefing(runtime, sections=("quote",))


def cmd_news(runtime: Runtime) -> str:
    return build_briefing(runtime, sections=("news",))


# New command: one handler above, one line here.
# menu=True registers it in set_my_commands. button and row add an inline button.
COMMANDS: tuple[BotCommand, ...] = (
    BotCommand("start", "ბრძანებების სია", cmd_help, menu=False, show_buttons=True),
    BotCommand("brief", "სრული ბრიფინგი", cmd_brief, button="📋 ბრიფინგი", row=0),
    BotCommand("weather", "მხოლოდ ამინდი", cmd_weather, button="🌤 ამინდი", row=1),
    BotCommand("fx", "მხოლოდ ვალუტის კურსი", cmd_fx, button="💱 კურსი", row=1),
    BotCommand("quote", "მხოლოდ ციტატა და ფაქტი", cmd_quote, button="💬 ციტატა და ფაქტი", row=2),
    BotCommand("news", "სიახლეები", cmd_news, button="📰 სიახლეები", row=3),
    BotCommand("help", "ბრძანებების სია", cmd_help, show_buttons=True),
)


def help_text(commands: Sequence[BotCommand] | None = None) -> str:
    rows = commands if commands is not None else COMMANDS
    lines = ["ბრძანებები:"]
    for item in rows:
        lines.append(f"/{item.name} {item.description}")
    return "\n".join(lines)


def menu_commands(commands: Sequence[BotCommand] | None = None) -> list[BotCommand]:
    rows = commands if commands is not None else COMMANDS
    return [item for item in rows if item.menu]


def button_rows(commands: Sequence[BotCommand] | None = None) -> list[list[tuple[str, str]]]:
    rows = commands if commands is not None else COMMANDS
    grouped: dict[int, list[tuple[str, str]]] = {}
    for item in rows:
        if not item.button or item.row is None:
            continue
        grouped.setdefault(item.row, []).append((item.button, item.name))
    return [grouped[key] for key in sorted(grouped)]


def chat_allowed(chat_id: object, allowed_chat_id: str) -> bool:
    allowed = str(allowed_chat_id).strip()
    return bool(allowed) and str(chat_id) == allowed


def invoke(
    name: str,
    runtime: Runtime,
    commands: Sequence[BotCommand] | None = None,
) -> str:
    rows = commands if commands is not None else COMMANDS
    command = next((item for item in rows if item.name == name), None)
    if command is None:
        return f"{UNKNOWN_TEXT}\n\n{help_text(rows)}"
    try:
        body = command.handler(runtime)
    except Exception as exc:
        logger.error("Command %s failed (%s)", name, type(exc).__name__)
        return FAILURE_TEXT
    return (body or "").strip() or FAILURE_TEXT


def handle_callback(
    data: str,
    chat_id: object,
    allowed_chat_id: str,
    runtime: Runtime,
    commands: Sequence[BotCommand] | None = None,
) -> str | None:
    """Same handlers as slash commands. None means the chat is ignored."""
    if not chat_allowed(chat_id, allowed_chat_id):
        return None
    return invoke((data or "").strip(), runtime, commands)


async def serve_callback(
    *,
    chat_id: object,
    data: str,
    allowed_chat_id: str,
    runtime: Runtime,
    answer: Callable[[], Awaitable[None]],
    send: Callable[[str], Awaitable[None]],
    commands: Sequence[BotCommand] | None = None,
) -> None:
    reply = handle_callback(data, chat_id, allowed_chat_id, runtime, commands)
    if reply is None:
        return
    await answer()
    await send(reply)


def parse_command(text: str) -> str | None:
    stripped = (text or "").strip()
    if not stripped.startswith("/"):
        return None
    token = stripped.split(maxsplit=1)[0]
    name = token[1:]
    if "@" in name:
        name = name.split("@", 1)[0]
    name = name.strip().lower()
    if not name:
        return None
    return name


def dispatch(
    text: str,
    chat_id: object,
    allowed_chat_id: str,
    runtime: Runtime,
    commands: Sequence[BotCommand] | None = None,
) -> str | None:
    """Return a reply, or None when the chat must be ignored."""
    if not chat_allowed(chat_id, allowed_chat_id):
        return None
    name = parse_command(text)
    if name is None:
        return None
    return invoke(name, runtime, commands)


def split_telegram(text: str, limit: int = TELEGRAM_TEXT_LIMIT) -> list[str]:
    if limit < 1:
        raise ValueError("limit must be positive")
    rest = (text or "").strip()
    if not rest:
        return [FAILURE_TEXT]
    parts: list[str] = []
    while rest:
        if len(rest) <= limit:
            parts.append(rest)
            break
        cut = rest.rfind("\n", 0, limit + 1)
        if cut <= 0:
            cut = limit
        parts.append(rest[:cut].rstrip())
        rest = rest[cut:].lstrip("\n")
    return [part for part in parts if part]


def run_bot(token: str, allowed_chat_id: str, runtime: Runtime) -> None:
    from telegram import BotCommand as TelegramCommand
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
    from telegram.ext import (
        Application,
        CallbackQueryHandler,
        CommandHandler,
        ContextTypes,
        MessageHandler,
        filters,
    )

    allowed = allowed_chat_id.strip()

    def _markup() -> InlineKeyboardMarkup:
        rows = [
            [InlineKeyboardButton(label, callback_data=data) for label, data in row]
            for row in button_rows()
        ]
        return InlineKeyboardMarkup(rows)

    async def _post_init(application: Application) -> None:
        try:
            await application.bot.set_my_commands(
                [TelegramCommand(item.name, item.description) for item in menu_commands()]
            )
            logger.info("Telegram command menu registered")
        except Exception as exc:
            logger.error("Command menu failed (%s)", type(exc).__name__)

    application = Application.builder().token(token).post_init(_post_init).build()

    async def _send(message: object, text: str | None, markup: InlineKeyboardMarkup | None = None) -> None:
        if not text or message is None:
            return
        reply = getattr(message, "reply_text", None)
        if not callable(reply):
            return
        parts = split_telegram(text)
        for index, part in enumerate(parts):
            await reply(part, reply_markup=markup if index == 0 else None)

    def _bound(command: BotCommand):
        async def inner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            del context
            chat = update.effective_chat
            message = update.effective_message
            if chat is None or message is None:
                return
            try:
                reply = dispatch(message.text or f"/{command.name}", chat.id, allowed, runtime)
                markup = _markup() if command.show_buttons else None
                await _send(message, reply, markup)
            except Exception as exc:
                logger.error("Command %s failed (%s)", command.name, type(exc).__name__)
                try:
                    await _send(message, FAILURE_TEXT)
                except Exception as send_exc:
                    logger.error("Reply failed (%s)", type(send_exc).__name__)

        return inner

    for command in COMMANDS:
        application.add_handler(CommandHandler(command.name, _bound(command)))

    async def _unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        del context
        chat = update.effective_chat
        message = update.effective_message
        if chat is None or message is None:
            return
        try:
            reply = dispatch(message.text or "", chat.id, allowed, runtime)
            await _send(message, reply)
        except Exception as exc:
            logger.error("Command unknown failed (%s)", type(exc).__name__)

    application.add_handler(MessageHandler(filters.COMMAND, _unknown))

    async def _on_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        del context
        query = update.callback_query
        chat = update.effective_chat
        if query is None or chat is None:
            return

        async def answer() -> None:
            await query.answer()

        async def send(text: str) -> None:
            await _send(query.message, text)

        try:
            await serve_callback(
                chat_id=chat.id,
                data=query.data or "",
                allowed_chat_id=allowed,
                runtime=runtime,
                answer=answer,
                send=send,
            )
        except Exception as exc:
            logger.error("Callback failed (%s)", type(exc).__name__)

    application.add_handler(CallbackQueryHandler(_on_button))

    async def _on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        del update
        logger.error("Bot update failed (%s)", type(context.error).__name__)

    application.add_error_handler(_on_error)
    logger.info("Telegram bot polling started")
    application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)

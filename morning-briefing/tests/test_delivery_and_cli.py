"""Delivery adapters and the CLI wiring."""

import json
import urllib.error
from pathlib import Path

import pytest
import yaml

from core.briefing import INSTRUCTION_GUARD, build_system_prompt
from core.config import apply_provider_override, load_config, validate_config
from main import main
from notifiers.email_smtp import SmtpNotifier
from notifiers.file_output import FileNotifier
from notifiers.telegram import TelegramNotifier
from tests.fakes import RecordingLLM

ROOT = Path(__file__).resolve().parents[1]


class _SMTP:
    def __init__(self):
        self.sent = []
        self.login_user = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def login(self, username, password):
        self.login_user = username
        self.password = password

    def send_message(self, message):
        self.sent.append(message)


def test_file_notifier_writes_utf8(tmp_path):
    path = tmp_path / "nested" / "briefing.txt"
    FileNotifier(path).send("დილის ბრიფინგი", "ტექსტი\n")
    assert path.read_text(encoding="utf-8").startswith("დილის ბრიფინგი\n")
    assert "ტექსტი" in path.read_text(encoding="utf-8")


def test_smtp_uses_the_gmail_imap_account_when_smtp_fields_are_empty():
    notifier = SmtpNotifier.from_config(
        {"smtp": {"host": "smtp.gmail.com", "port": 587, "security": "starttls"}},
        {
            "IMAP_USERNAME": "user@gmail.com",
            "IMAP_PASSWORD": "abcd efgh ijkl mnop",
            "SMTP_TO": "user@gmail.com",
        },
    )
    assert notifier._username == "user@gmail.com"
    assert notifier._password == "abcdefghijklmnop"
    assert notifier._sender == "user@gmail.com"
    assert notifier._host == "smtp.gmail.com"


def test_smtp_sends_without_printing_the_password():
    client = _SMTP()
    notifier = SmtpNotifier(
        host="smtp.example.test",
        port=587,
        username="sender",
        password="smtp-secret",
        sender="sender@example.test",
        recipient="me@example.test",
        security="starttls",
        timeout=5,
        connect=lambda: client,
    )
    notifier.send("დილის ბრიფინგი", "მზადაა")
    assert client.login_user == "sender"
    assert client.password == "smtp-secret"
    assert client.sent[0]["Subject"] == "დილის ბრიფინგი"
    assert "smtp-secret" not in repr(notifier)


def test_telegram_error_hides_the_token():
    token = "123456:telegram-secret"

    def opener(request, timeout=0):
        raise urllib.error.HTTPError(request.full_url, 401, "no", email_headers(), None)

    notifier = TelegramNotifier(token=token, chat_id="42", timeout=5, max_chars=20, opener=opener)
    with pytest.raises(RuntimeError) as caught:
        notifier.send("სათაური", "ძალიან გრძელი ტექსტი რომელიც უნდა შემოკლდეს")
    assert token not in str(caught.value)
    assert caught.value.__suppress_context__ is True


def test_telegram_posts_plain_text():
    captured = {}

    class _Response:
        status = 200

        def read(self):
            return b"{}"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    def opener(request, timeout=0):
        captured["url"] = request.full_url
        captured["body"] = json.loads(request.data.decode("utf-8"))
        return _Response()

    TelegramNotifier(token="token-value", chat_id="77", timeout=5, max_chars=3500, opener=opener).send(
        "დილის ბრიფინგი",
        "მზადაა",
    )
    assert captured["body"]["chat_id"] == "77"
    assert captured["body"]["text"].startswith("დილის ბრიფინგი")
    assert "parse_mode" not in captured["body"]


def email_headers():
    from email.message import EmailMessage

    return EmailMessage()


def _write_config(path: Path, out: Path, *, mail_enabled: bool) -> None:
    config = {
        "timezone": "Asia/Tbilisi",
        "llm": {
            "provider": "tests.fakes:RecordingLLM",
            "models": ["custom/a", "custom/b"],
            "fake_text": "ბრიფინგი",
            "temperature": 0.1,
            "max_tokens": 100,
        },
        "briefing": {
            "subject": "დილის ბრიფინგი",
            "max_reply_emails": 5,
            "priority_count": 3,
            "system_prompt": "მოკლე ფორმატი $max_reply_emails\n",
        },
        "delivery": {"channel": "file", "file_path": str(out)},
        "notifiers": {"file": "notifiers.file_output:FileNotifier"},
        "mail": {
            "enabled": mail_enabled,
            "source": "tests.missing_mod:Nope",
        },
        "calendar": {"enabled": False},
        "weather": {"enabled": False},
    }
    path.write_text(yaml.safe_dump(config, allow_unicode=True), encoding="utf-8")


def test_cli_refuses_to_send_when_the_api_key_is_missing(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setattr("dotenv.load_dotenv", lambda *args, **kwargs: False)
    config_path = tmp_path / "config.yaml"
    out = tmp_path / "briefing.txt"
    _write_config(config_path, out, mail_enabled=False)
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    data["llm"]["api_key_env"] = "GEMINI_API_KEY"
    data["llm"]["enabled"] = True
    config_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    code = main(["--config", str(config_path)])
    captured = capsys.readouterr()
    assert code == 2
    assert "GEMINI_API_KEY" in captured.err
    assert "არაფერი გაიგზავნა" in captured.err
    assert not out.exists()


def test_provider_override_replaces_the_list_only():
    updated = apply_provider_override({"llm": {"models": ["custom/a"], "temperature": 0.1}, "timezone": "Asia/Tbilisi"}, "forced/model")
    assert updated["llm"]["models"] == ["forced/model"]
    assert updated["llm"]["temperature"] == 0.1


def test_dry_run_cli(tmp_path, capsys):
    config_path = tmp_path / "config.yaml"
    out = tmp_path / "briefing.txt"
    _write_config(config_path, out, mail_enabled=True)
    code = main(["--config", str(config_path), "--dry-run", "--provider", "forced/model"])
    captured = capsys.readouterr()
    assert code == 0
    assert "ბრიფინგი" in captured.out
    assert not out.exists()
    assert RecordingLLM.seen_models == ["forced/model"]
    assert "მიუწვდომელია" in RecordingLLM.last_user
    assert "გამორთულია" in RecordingLLM.last_user
    assert INSTRUCTION_GUARD in RecordingLLM.last_system


def test_cli_writes_a_file_when_not_dry_run(tmp_path, capsys):
    config_path = tmp_path / "config.yaml"
    out = tmp_path / "briefing.txt"
    _write_config(config_path, out, mail_enabled=False)
    code = main(["--config", str(config_path)])
    assert code == 0
    text = out.read_text(encoding="utf-8")
    assert text.startswith("დილის ბრიფინგი")
    assert "ბრიფინგი" in text


def test_shipped_config_is_valid_and_guarded():
    config = load_config(ROOT / "config.yaml")
    validate_config(config)
    prompt = config["briefing"]["system_prompt"]
    assert INSTRUCTION_GUARD in prompt
    assert "დღის ციტატა და ფაქტი" in prompt
    assert "ქართულად" in prompt
    quote = config["daily_quote"]
    assert quote["enabled"] is True
    assert quote["timeout_seconds"] == 10
    assert quote["user_agent"] == "morning-briefing"
    fx = config["fx"]
    assert fx["enabled"] is True
    assert fx["currencies"] == ["USD", "EUR"]
    assert fx["timeout_seconds"] == 10
    assert "ვალუტის კურსი" in prompt
    assert "რიცხვი ნუ შეცვალო" in prompt
    rendered = build_system_prompt(config)
    assert INSTRUCTION_GUARD in rendered
    assert "$max_reply_emails" not in rendered
    assert "5" in rendered
    assert "3" in rendered
    assert config["briefing"]["max_reply_emails"] == 5
    assert config["briefing"]["priority_count"] == 3
    assert config["llm"]["enabled"] is True
    assert config["llm"]["api_key_env"] == "GEMINI_API_KEY"
    assert config["llm"]["models"] == [
        "gemini/gemini-3.5-flash-lite",
        "gemini/gemini-3.8-flash",
    ]
    assert config["llm"]["rate_limit_retry_seconds"] == 3
    assert config["news"]["enabled"] is True
    assert config["news"]["max_links"] == 5
    assert "ქალაქი" in prompt
    assert "სიახლეები" in prompt


def test_dotenv_is_loaded_before_config_and_runtime():
    text = (ROOT / "main.py").read_text(encoding="utf-8")
    body = text.split("def main(", 1)[1]
    assert body.index("load_dotenv(") < body.index("validate_config(")
    assert body.index("load_dotenv(") < body.index("build_runtime(")


def test_python_modules_do_not_hardcode_model_ids():
    banned = ("gemini/", "anthropic/", "openai/", "ollama/", "ollama_chat/", "claude-")
    files = [ROOT / "main.py"]
    for folder in ("core", "providers", "sources", "notifiers"):
        files.extend((ROOT / folder).rglob("*.py"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        for item in banned:
            assert item not in text, f"{item} found in {path.name}"

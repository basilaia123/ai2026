"""LiteLLM fallback stays inside the provider and does not leak error text."""

import pytest

from providers.llm_litellm import LiteLLMProvider


def test_fallback_stops_on_first_success():
    calls = []

    def complete_fn(*, model, messages, temperature, max_tokens):
        calls.append(model)
        if model == "first":
            raise RuntimeError("rate limit secret-token-value")
        if model == "second":
            return "  მზადაა  "
        raise AssertionError("later model must not be called")

    provider = LiteLLMProvider(
        ["first", "second", "third"],
        temperature=0.0,
        max_tokens=20,
        complete_fn=complete_fn,
    )
    assert provider.complete("system", "user") == "მზადაა"
    assert calls == ["first", "second"]
    assert messages_are_plain(complete_fn, provider)


def messages_are_plain(complete_fn, provider):
    seen = {}

    def spy(*, model, messages, temperature, max_tokens):
        seen["messages"] = messages
        seen["keys"] = set()
        return "ok"

    provider._complete_fn = spy
    provider._models = ["only"]
    provider.complete("სისტემა", "მონაცემი")
    assert seen["messages"] == [
        {"role": "system", "content": "სისტემა"},
        {"role": "user", "content": "მონაცემი"},
    ]
    assert "tools" not in seen["messages"][0]
    return True


def test_empty_completion_tries_the_next_model():
    calls = []

    def complete_fn(*, model, messages, temperature, max_tokens):
        calls.append(model)
        if model == "first":
            return "   "
        return "ტექსტი"

    provider = LiteLLMProvider(
        ["first", "second"],
        temperature=0.1,
        max_tokens=10,
        complete_fn=complete_fn,
    )
    assert provider.complete("s", "u") == "ტექსტი"
    assert calls == ["first", "second"]


def test_all_models_failed_hides_exception_text():
    def complete_fn(*, model, messages, temperature, max_tokens):
        raise RuntimeError("secret-token-value")

    provider = LiteLLMProvider(
        ["first"],
        temperature=0.0,
        max_tokens=10,
        complete_fn=complete_fn,
    )
    with pytest.raises(RuntimeError) as caught:
        provider.complete("s", "u")
    assert "secret-token-value" not in str(caught.value)
    assert "RuntimeError" in str(caught.value)


def test_rate_limit_retries_the_same_model_once():
    calls = []
    waits = []

    class Limited(Exception):
        status_code = 429

    def complete_fn(*, model, messages, temperature, max_tokens):
        calls.append(model)
        if len(calls) == 1:
            raise Limited("secret-token-value")
        return "მზადაა"

    provider = LiteLLMProvider(
        ["first", "second"],
        temperature=0.0,
        max_tokens=10,
        complete_fn=complete_fn,
        sleep_fn=lambda seconds: waits.append(seconds),
        rate_limit_retry_seconds=3,
    )
    assert provider.complete("s", "u") == "მზადაა"
    assert calls == ["first", "first"]
    assert waits == [3]


def test_rate_limit_twice_moves_to_the_next_model():
    calls = []

    class Limited(Exception):
        status_code = 429

    def complete_fn(*, model, messages, temperature, max_tokens):
        calls.append(model)
        if model == "first":
            raise Limited("secret-token-value")
        return "შემდეგი"

    provider = LiteLLMProvider(
        ["first", "second"],
        temperature=0.0,
        max_tokens=10,
        complete_fn=complete_fn,
        sleep_fn=lambda seconds: None,
    )
    assert provider.complete("s", "u") == "შემდეგი"
    assert calls == ["first", "first", "second"]


def test_timeout_does_not_retry_the_same_model():
    calls = []

    def complete_fn(*, model, messages, temperature, max_tokens):
        calls.append(model)
        if model == "first":
            raise TimeoutError("slow")
        return "მზადაა"

    waits = []
    provider = LiteLLMProvider(
        ["first", "second"],
        temperature=0.0,
        max_tokens=10,
        complete_fn=complete_fn,
        sleep_fn=lambda seconds: waits.append(seconds),
    )
    assert provider.complete("s", "u") == "მზადაა"
    assert calls == ["first", "second"]
    assert waits == []


def test_missing_library_is_not_called_a_missing_model():
    from providers.llm_litellm import explain_failure

    reason = explain_failure(ModuleNotFoundError("No module named 'litellm'"))
    assert reason == "საჭირო ბიბლიოთეკა არ არის დაყენებული"


def test_from_config_reads_models_without_hardcoding_them():
    provider = LiteLLMProvider.from_config(
        {"llm": {"models": ["  custom/one  ", "custom/two"], "temperature": 0.2, "max_tokens": 30}},
        {},
    )
    assert provider._models == ["custom/one", "custom/two"]
    assert provider._temperature == 0.2
    assert provider._max_tokens == 30


def test_failure_reasons_and_the_logged_error_hide_the_key(caplog, monkeypatch):
    import logging

    from core.redact import configure_logging

    monkeypatch.setenv("GEMINI_API_KEY", "secret-token-value")
    configure_logging("INFO", ["secret-token-value"])

    class Auth(Exception):
        status_code = 401

    class Missing(Exception):
        status_code = 404

    class Limited(Exception):
        status_code = 429

    seen = {"kind": "auth"}

    def complete_fn(*, model, messages, temperature, max_tokens):
        kind = seen["kind"]
        if kind == "auth":
            raise Auth("bad secret-token-value")
        if kind == "missing":
            raise Missing("model is not found")
        raise Limited("quota secret-token-value")

    provider = LiteLLMProvider(
        ["first"],
        temperature=0.0,
        max_tokens=10,
        complete_fn=complete_fn,
        sleep_fn=lambda seconds: None,
    )
    with caplog.at_level(logging.WARNING):
        with pytest.raises(RuntimeError) as auth_error:
            provider.complete("s", "u")
        seen["kind"] = "missing"
        with pytest.raises(RuntimeError) as missing_error:
            provider.complete("s", "u")
        seen["kind"] = "limit"
        with pytest.raises(RuntimeError) as limit_error:
            provider.complete("s", "u")
    assert "API გასაღები არასწორია" in str(auth_error.value)
    assert "მოდელი ვერ მოიძებნა" in str(missing_error.value)
    assert "ლიმიტი ამოიწურა" in str(limit_error.value)
    assert "secret-token-value" not in caplog.text
    assert "secret-token-value" not in str(auth_error.value)


def test_default_complete_passes_the_configured_model_id(monkeypatch):
    seen = {}

    def fake_completion(**kwargs):
        seen["model"] = kwargs["model"]

        class Message:
            content = "კარგი"

        class Choice:
            message = Message()

        class Response:
            choices = [Choice()]

        return Response()

    import litellm

    monkeypatch.setattr(litellm, "completion", fake_completion)
    from providers.llm_litellm import default_complete

    model_id = "gemini/gemini-3.5-flash-lite"
    assert default_complete(model=model_id, messages=[], temperature=1.0, max_tokens=8) == "კარგი"
    assert seen["model"] == model_id

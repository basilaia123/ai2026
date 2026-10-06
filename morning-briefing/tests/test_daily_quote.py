"""Daily quote and fact. HTTP is mocked; parsers do not touch the network."""

from unittest.mock import patch

import pytest
import requests

from core.briefing import UNAVAILABLE, render_direct
from core.interfaces import DailyQuote
from sources.daily_quote import DailyQuoteSource, fact_from_payload, quote_from_payload
from tests.test_briefing import _runtime


def _source() -> DailyQuoteSource:
    return DailyQuoteSource(
        quote_url="https://quotes.example/today",
        fact_url="https://facts.example/today",
        timeout=10,
        user_agent="morning-briefing",
    )


def _response(status: int, payload):
    class Response:
        status_code = status

        def json(self):
            if isinstance(payload, Exception):
                raise payload
            return payload

    return Response()


def test_quote_keeps_text_and_author():
    quote, author = quote_from_payload(
        [{"q": "A gentleman is one who puts more into the world than he takes out.", "a": "George Bernard Shaw"}]
    )
    assert quote == "A gentleman is one who puts more into the world than he takes out."
    assert author == "George Bernard Shaw"


def test_quote_without_author_is_just_the_text():
    quote, author = quote_from_payload([{"q": "მხოლოდ ტექსტი"}])
    assert quote == "მხოლოდ ტექსტი"
    assert author == ""


def test_empty_quote_is_rejected():
    with pytest.raises(ValueError):
        quote_from_payload([{"q": "  ", "a": "ვიღაც"}])


def test_fact_uses_the_text_field():
    assert fact_from_payload({"text": "The average person blinks."}) == "The average person blinks."


def test_fact_without_text_is_rejected():
    with pytest.raises(ValueError):
        fact_from_payload({"text": ""})


@patch("sources.daily_quote.requests.get")
def test_request_uses_timeout_and_user_agent(mock_get):
    def side_effect(url, **kwargs):
        assert kwargs["timeout"] == 10
        assert kwargs["headers"]["User-Agent"] == "morning-briefing"
        if url.endswith("/today") and "quotes" in url:
            return _response(200, [{"q": "Be kind.", "a": "Someone"}])
        return _response(200, {"text": "A short fact."})

    mock_get.side_effect = side_effect
    item = _source().fetch()
    assert item == DailyQuote(quote="Be kind.", author="Someone", fact="A short fact.")
    assert mock_get.call_count == 2


@patch("sources.daily_quote.requests.get")
def test_quote_timeout_keeps_the_fact(mock_get):
    def side_effect(url, **kwargs):
        if "quotes" in url:
            raise requests.Timeout("slow")
        return _response(200, {"text": "The fact remains."})

    mock_get.side_effect = side_effect
    item = _source().fetch()
    assert item.quote is None
    assert item.fact == "The fact remains."


@patch("sources.daily_quote.requests.get")
def test_fact_http_error_keeps_the_quote(mock_get):
    def side_effect(url, **kwargs):
        if "facts" in url:
            return _response(500, {})
        return _response(200, [{"q": "Still here.", "a": ""}])

    mock_get.side_effect = side_effect
    item = _source().fetch()
    assert item.quote == "Still here."
    assert item.fact is None


@patch("sources.daily_quote.requests.get")
def test_bad_json_is_a_clear_failure(mock_get):
    mock_get.return_value = _response(200, ValueError("not json"))
    item = _source().fetch()
    assert item.quote is None
    assert item.fact is None


@patch("sources.daily_quote.requests.get")
def test_connection_error_does_not_drop_the_other_part(mock_get):
    def side_effect(url, **kwargs):
        if "quotes" in url:
            return _response(200, [{"q": "Quoted.", "a": "Author"}])
        raise requests.ConnectionError("down")

    mock_get.side_effect = side_effect
    item = _source().fetch()
    assert item.quote == "Quoted."
    assert item.fact is None


@patch("sources.daily_quote.requests.get")
def test_source_failure_still_renders_weather(mock_get):
    mock_get.side_effect = requests.Timeout("down")
    runtime = _runtime(
        mail_enabled=False,
        calendar_enabled=False,
        daily_quote=_source(),
        daily_quote_enabled=True,
    )
    runtime.config["daily_quote"] = {"heading": "დღის ციტატა და ფაქტი"}
    text = render_direct(runtime)
    assert "12.0°C" in text
    assert "ციტატა: " + UNAVAILABLE in text
    assert "ფაქტი: " + UNAVAILABLE in text


@patch("sources.daily_quote.requests.get")
def test_disabled_quote_does_not_call_requests(mock_get):
    runtime = _runtime(daily_quote=_source(), daily_quote_enabled=False)
    text = render_direct(runtime)
    mock_get.assert_not_called()
    assert "12.0°C" in text
    assert "ციტატა:" not in text

"""Weather facts and secret redaction."""

import io
import logging
import urllib.error

import pytest

from core.redact import RedactingFormatter, collect_secrets
from sources.weather_openmeteo import OpenMeteoWeatherSource, facts_from_payload


def test_facts_use_only_payload_fields():
    text = facts_from_payload(
        {
            "current": {"temperature_2m": 12.3, "weather_code": 61, "wind_speed_10m": 14.2},
            "daily": {
                "temperature_2m_min": [8],
                "temperature_2m_max": [15.5],
                "precipitation_probability_max": [40],
            },
        },
        "თბილისი",
    )
    assert "ქალაქი: თბილისი" in text
    assert "ახლანდელი ტემპერატურა: 12.3°C" in text
    assert "მდგომარეობა: სუსტი წვიმა" in text
    assert "ქარი: 14 კმ/სთ" in text
    assert "დღის მინიმუმი: 8.0°C" in text
    assert "დღის მაქსიმუმი: 15.5°C" in text
    assert "ნალექის ალბათობა: 40%" in text


def test_missing_temperature_is_an_error():
    with pytest.raises(ValueError):
        facts_from_payload({"current": {}}, "თბილისი")


def test_weather_http_error_hides_the_query():
    token = "super-secret-token"

    def opener(request, timeout=0):
        raise urllib.error.URLError(token)

    source = OpenMeteoWeatherSource(
        city="თბილისი",
        latitude=41.7,
        longitude=44.8,
        timezone_name="Asia/Tbilisi",
        base_url="https://example.test/forecast",
        timeout=5,
        opener=opener,
    )
    with pytest.raises(RuntimeError) as caught:
        source.fetch()
    assert token not in str(caught.value)


def test_blank_secret_values_are_removed():
    env = {"GEMINI_API_KEY": "", "IMAP_PASSWORD": "  ", "CITY": "", "OLLAMA_API_BASE": "http://127.0.0.1:11434"}
    from core.redact import drop_blank_secrets

    drop_blank_secrets(env)
    assert "GEMINI_API_KEY" not in env
    assert "IMAP_PASSWORD" not in env
    assert env["CITY"] == ""
    assert env["OLLAMA_API_BASE"].startswith("http://")


def test_collect_secrets_uses_names_not_a_provider_list():
    secrets = collect_secrets(
        {
            "IMAP_PASSWORD": "mailbox-secret",
            "ICS_URL": "https://example.test/feed?token=abc",
            "CITY": "თბილისი",
            "SHORT": "ab",
        }
    )
    assert "mailbox-secret" in secrets
    assert secrets[0].startswith("https://")
    assert "თბილისი" not in secrets
    assert "ab" not in secrets


def test_formatter_redacts_secret_values():
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(RedactingFormatter("%(message)s", ["mailbox-secret"]))
    log = logging.getLogger("redact-test-morning")
    log.handlers = [handler]
    log.propagate = False
    log.setLevel(logging.INFO)
    log.info("login failed for mailbox-secret")
    rendered = stream.getvalue()
    assert "mailbox-secret" not in rendered
    assert "***" in rendered

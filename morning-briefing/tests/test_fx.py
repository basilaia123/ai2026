"""FX rates. HTTP is mocked for both the national bank and the fallback."""

from datetime import date
from unittest.mock import patch

import requests

from core.briefing import FX_UNAVAILABLE, render_direct
from main import execute
from sources.fx import FxSource, format_fx, rates_from_nbg
from tests.test_briefing import _runtime


NBG_URL = "https://nbg.example/json"
ER_URL = "https://er.example/v6/latest/{base}"


def _source() -> FxSource:
    return FxSource(
        codes=["USD", "EUR"],
        timeout=10,
        user_agent="morning-briefing/1.0",
        nbg_url=NBG_URL,
        er_url=ER_URL,
    )


def _response(status: int, payload):
    class Response:
        status_code = status

        def json(self):
            if isinstance(payload, Exception):
                raise payload
            return payload

    return Response()


def _nbg_payload():
    return [
        {
            "date": "2026-10-06T00:00:00.000Z",
            "currencies": [
                {"code": "EUR", "quantity": 1, "rate": 3.18, "diff": -0.002},
                {"code": "USD", "quantity": 1, "rate": 2.705, "diff": 0.004},
                {"code": "GBP", "quantity": 1, "rate": 3.5, "diff": 0.01},
            ],
        }
    ]


@patch("sources.fx.requests.get")
def test_nbg_divides_by_quantity_and_formats(mock_get):
    mock_get.return_value = _response(
        200,
        [
            {
                "date": "2026-10-06",
                "currencies": [{"code": "USD", "quantity": 100, "rate": 270.5, "diff": 0.4}],
            }
        ],
    )
    source = FxSource(
        codes=["USD"],
        timeout=10,
        user_agent="morning-briefing/1.0",
        nbg_url=NBG_URL,
        er_url=ER_URL,
    )
    data = source.fetch()
    assert data["source"] == "NBG"
    assert data["rates"]["USD"]["rate"] == 2.705
    assert data["rates"]["USD"]["diff"] == 0.4
    assert format_fx(data) == "💱 ვალუტის კურსი (ეროვნული ბანკი)\nUSD: 2.7050 ₾ (▲ 0.4000)"
    mock_get.assert_called_once_with(
        NBG_URL,
        params=[("currencies", "USD")],
        timeout=10,
        headers={"User-Agent": "morning-briefing/1.0", "Accept": "application/json"},
    )


def test_nbg_parser_keeps_requested_order_and_sample_lines():
    data = rates_from_nbg(_nbg_payload(), ["USD", "EUR"])
    assert list(data["rates"]) == ["USD", "EUR"]
    text = format_fx(data)
    assert text == (
        "💱 ვალუტის კურსი (ეროვნული ბანკი)\n"
        "USD: 2.7050 ₾ (▲ 0.0040)\n"
        "EUR: 3.1800 ₾ (▼ 0.0020)"
    )


def test_missing_diff_omits_the_arrow():
    text = format_fx({"source": "open.er-api.com", "date": None, "rates": {"USD": {"rate": 2.71, "diff": None}}})
    assert text == "💱 ვალუტის კურსი (open.er-api.com)\nUSD: 2.7100 ₾"


@patch("sources.fx.requests.get")
def test_nbg_timeout_uses_er_api(mock_get):
    def side_effect(url, **kwargs):
        assert kwargs["timeout"] == 10
        assert kwargs["headers"]["User-Agent"] == "morning-briefing/1.0"
        if url == NBG_URL:
            raise requests.Timeout("slow")
        code = url.rsplit("/", 1)[-1]
        gel = {"USD": 2.705, "EUR": 3.18}[code]
        return _response(200, {"rates": {"GEL": gel}})

    mock_get.side_effect = side_effect
    data = _source().fetch()
    assert data["source"] == "open.er-api.com"
    assert data["date"] is None
    assert data["rates"]["USD"] == {"rate": 2.705, "diff": None}
    assert data["rates"]["EUR"]["rate"] == 3.18
    assert "▲" not in format_fx(data)
    assert mock_get.call_count == 3


@patch("sources.fx.requests.get")
def test_nbg_http_error_uses_er_api(mock_get):
    def side_effect(url, **kwargs):
        if url == NBG_URL:
            return _response(500, {})
        return _response(200, {"rates": {"GEL": 2.5}})

    mock_get.side_effect = side_effect
    data = _source().fetch()
    assert data["source"] == "open.er-api.com"
    assert set(data["rates"]) == {"USD", "EUR"}


@patch("sources.fx.requests.get")
def test_both_sources_return_none(mock_get):
    def side_effect(url, **kwargs):
        if url == NBG_URL:
            raise requests.ConnectionError("down")
        raise requests.Timeout("down")

    mock_get.side_effect = side_effect
    assert _source().fetch() is None


@patch("sources.fx.requests.get")
def test_bad_json_falls_through_then_fails(mock_get):
    mock_get.return_value = _response(200, ValueError("not json"))
    assert _source().fetch() is None
    assert mock_get.call_count == 2


@patch("sources.fx.requests.get")
def test_unavailable_fx_still_renders_weather(mock_get):
    mock_get.side_effect = requests.Timeout("down")
    runtime = _runtime(mail_enabled=False, calendar_enabled=False, fx=_source(), fx_enabled=True)
    text = render_direct(runtime)
    assert "12.0°C" in text
    assert FX_UNAVAILABLE in text


@patch("sources.fx.requests.get")
def test_disabled_fx_does_not_call_requests(mock_get):
    runtime = _runtime(fx=_source(), fx_enabled=False)
    text = render_direct(runtime)
    mock_get.assert_not_called()
    assert "ვალუტის კურსი" not in text
    assert "12.0°C" in text


def test_model_cannot_rewrite_the_rates(capsys):
    class FixedFx:
        def fetch(self):
            return {"source": "NBG", "date": "2026-10-06", "rates": {"USD": {"rate": 2.705, "diff": 0.004}}}

    class RewritingLLM:
        def complete(self, system_prompt, user_prompt):
            assert "2.705" not in user_prompt
            return "მოდელის ტექსტი USD: 9.9999"

    runtime = _runtime(
        llm=RewritingLLM(),
        mail_enabled=False,
        calendar_enabled=False,
        fx=FixedFx(),
        fx_enabled=True,
    )
    runtime.config["llm"] = {"enabled": True}
    code = execute(runtime, dry_run=True, today=date(2026, 10, 6))
    captured = capsys.readouterr()
    assert code == 0
    assert "მოდელის ტექსტი USD: 9.9999" in captured.out
    assert "USD: 2.7050 ₾ (▲ 0.0040)" in captured.out

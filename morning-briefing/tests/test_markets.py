"""CoinGecko and Yahoo chart. Network calls are mocked."""

import requests

from sources.markets import fetch, fetch_crypto, fetch_stock, format_markets


CG_BODY = {
    "bitcoin": {"usd": 67250, "usd_24h_change": 1.84},
    "ethereum": {"usd": 2610, "usd_24h_change": -0.64},
}

def chart(closes: list[float]) -> dict:
    start = 1_759_363_200  # 2025-10-01 UTC-ish, only the spacing matters
    return {
        "chart": {
            "result": [
                {
                    "timestamp": [start + index * 86400 for index in range(len(closes))],
                    "indicators": {"quote": [{"close": closes}]},
                }
            ]
        }
    }


class Response:
    def __init__(self, *, status_code=200, payload=None, text=""):
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def json(self):
        return self._payload


def test_coingecko_success_formats_price_and_day_change(monkeypatch):
    seen = {}

    def get(url, params, headers, timeout):
        seen["url"] = url
        seen["params"] = params
        seen["headers"] = headers
        seen["timeout"] = timeout
        return Response(payload=CG_BODY)

    monkeypatch.setattr("sources.markets.requests.get", get)
    data = fetch(["bitcoin", "ethereum"], [], vs="usd", api_key="demo-key")
    assert seen["params"]["ids"] == "bitcoin,ethereum"
    assert seen["params"]["include_24hr_change"] == "true"
    assert seen["headers"]["x-cg-demo-api-key"] == "demo-key"
    assert seen["timeout"] == 10
    text = format_markets(data)
    assert "₿ bitcoin: $67,250 (▲ 1.8% / 24სთ)" in text
    assert "Ξ ethereum: $2,610 (▼ 0.6% / 24სთ)" in text
    assert "აქციები:" not in text
    assert "იყიდე" not in text
    assert "გაყიდე" not in text


def test_coingecko_error_still_returns_stocks(monkeypatch):
    def get(url, params, headers, timeout):
        if "coingecko" in url:
            raise requests.ConnectionError("down")
        return Response(payload=chart([229.30, 231.40]))

    monkeypatch.setattr("sources.markets.requests.get", get)
    data = fetch(["bitcoin"], ["aapl.us"])
    assert data["crypto"] is None
    assert data["stocks"][0]["name"] == "AAPL.US"
    text = format_markets(data)
    assert "კრიპტო: მიუწვდომელია" in text
    assert "AAPL: $231.40 (▲ 0.9%)" in text


def test_yahoo_uses_the_last_two_closes(monkeypatch):
    def get(url, params, headers, timeout):
        assert url.endswith("/AAPL")
        assert params == {"interval": "1d", "range": "10d"}
        return Response(payload=chart([229.30, 231.40]))

    monkeypatch.setattr("sources.markets.requests.get", get)
    item = fetch_stock("aapl.us")
    assert item["price"] == 231.40
    assert item["name"] == "AAPL.US"
    assert round(item["change_pct"], 1) == 0.9


def test_single_close_cannot_compute_a_change(monkeypatch):
    monkeypatch.setattr(
        "sources.markets.requests.get",
        lambda url, params, headers, timeout: Response(payload=chart([231.40])),
    )
    assert fetch_stock("aapl.us") is None


def test_one_stock_error_keeps_the_others(monkeypatch):
    def get(url, params, headers, timeout):
        if url.endswith("/NVDA"):
            raise requests.Timeout("slow")
        if url.endswith("/MSFT"):
            return Response(payload=chart([405.00, 415.50]))
        return Response(payload=chart([229.30, 231.40]))

    monkeypatch.setattr("sources.markets.requests.get", get)
    data = fetch([], ["aapl.us", "nvda.us", "msft.us"])
    assert [item["name"] for item in data["stocks"]] == ["AAPL.US", "MSFT.US"]
    text = format_markets(data)
    assert "კრიპტო:" not in text
    assert "AAPL:" in text
    assert "MSFT:" in text
    assert "NVDA" not in text


def test_google_label_uses_the_company_name(monkeypatch):
    monkeypatch.setattr(
        "sources.markets.requests.get",
        lambda url, params, headers, timeout: Response(payload=chart([250.00, 255.25])),
    )
    text = format_markets(fetch([], ["GOOGL", "NVDA"]))
    assert "Google: $255.25 (▲ 2.1%)" in text
    assert "NVDA: $255.25 (▲ 2.1%)" in text


def test_html_instead_of_json_does_not_become_a_price(monkeypatch):
    monkeypatch.setattr(
        "sources.markets.requests.get",
        lambda url, params, headers, timeout: Response(text="<!DOCTYPE html><html>verify your browser</html>"),
    )
    try:
        fetch_stock("aapl.us")
    except RuntimeError as exc:
        assert str(exc) == "stock payload is not JSON"
    else:
        raise AssertionError("HTML must not be parsed as a price")
    data = fetch([], ["aapl.us", "msft.us"])
    assert data["stocks"] is None


def test_http_error_is_a_crypto_failure(monkeypatch):
    monkeypatch.setattr(
        "sources.markets.requests.get",
        lambda url, params, headers, timeout: Response(status_code=429, payload={}),
    )
    try:
        fetch_crypto(["bitcoin"])
    except RuntimeError as exc:
        assert "429" in str(exc)
        assert "demo-key" not in str(exc)
    else:
        raise AssertionError("crypto HTTP error must raise")

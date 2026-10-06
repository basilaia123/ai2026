"""Crypto from CoinGecko and US stocks from Yahoo chart. One failed block does not stop the other."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Mapping

import requests

logger = logging.getLogger(__name__)

TIMEOUT = 10
HEADERS = {"User-Agent": "morning-briefing/1.0"}
CG_URL = "https://api.coingecko.com/api/v3/simple/price"
YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

CRYPTO_UNAVAILABLE = "კრიპტო: მიუწვდომელია"
STOCKS_UNAVAILABLE = "აქციები: მიუწვდომელია"

_CRYPTO_ICONS = {
    "bitcoin": "₿",
    "ethereum": "Ξ",
}
_STOCK_LABELS = {
    "GOOGL": "Google",
    "GOOG": "Google",
}


class MarketsSource:
    def __init__(
        self,
        *,
        crypto_ids: list[str],
        stock_symbols: list[str],
        vs_currency: str,
        timeout: float,
        user_agent: str,
        api_key: str | None,
    ) -> None:
        self._crypto_ids = crypto_ids
        self._stock_symbols = stock_symbols
        self._vs = vs_currency
        self._timeout = timeout
        self._user_agent = user_agent
        self._api_key = api_key

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "MarketsSource":
        block = config["markets"]
        key = str(env.get("COINGECKO_API_KEY") or "").strip()
        return cls(
            crypto_ids=[str(item).strip() for item in (block.get("crypto") or []) if str(item).strip()],
            stock_symbols=[str(item).strip() for item in (block.get("stocks") or []) if str(item).strip()],
            vs_currency=str(block.get("vs_currency") or "usd").strip().lower(),
            timeout=float(block.get("timeout_seconds", TIMEOUT)),
            user_agent=str(block.get("user_agent") or HEADERS["User-Agent"]),
            api_key=key or None,
        )

    def fetch(self) -> dict:
        return fetch(
            self._crypto_ids,
            self._stock_symbols,
            self._vs,
            timeout=self._timeout,
            user_agent=self._user_agent,
            api_key=self._api_key,
        )


def fetch_crypto(
    ids: list[str],
    vs: str = "usd",
    *,
    timeout: float = TIMEOUT,
    user_agent: str = HEADERS["User-Agent"],
    api_key: str | None = None,
) -> list[dict]:
    """CoinGecko price and 24h change. CoinGecko does not cover stocks."""
    headers = {"User-Agent": user_agent}
    if api_key:
        headers["x-cg-demo-api-key"] = api_key
    try:
        response = requests.get(
            CG_URL,
            params={"ids": ",".join(ids), "vs_currencies": vs, "include_24hr_change": "true"},
            headers=headers,
            timeout=timeout,
        )
    except requests.RequestException:
        raise RuntimeError("crypto request failed") from None
    if response.status_code >= 400:
        raise RuntimeError(f"crypto HTTP {response.status_code}")
    try:
        data = response.json()
    except ValueError:
        raise RuntimeError("crypto payload is not JSON") from None
    if not isinstance(data, dict):
        raise RuntimeError("crypto payload is not an object")
    out: list[dict] = []
    for coin_id in ids:
        item = data.get(coin_id)
        if not isinstance(item, dict) or vs not in item:
            continue
        out.append(
            {
                "name": coin_id,
                "price": item[vs],
                "change_pct": item.get(f"{vs}_24h_change"),
            }
        )
    return out


def fetch_stock(
    symbol: str,
    *,
    timeout: float = TIMEOUT,
    user_agent: str = HEADERS["User-Agent"],
) -> dict | None:
    """Yahoo daily closes. Change is versus the previous close. A .us suffix is optional."""
    ticker = _yahoo_symbol(symbol)
    if not ticker:
        return None
    try:
        response = requests.get(
            YAHOO_CHART.format(symbol=ticker),
            params={"interval": "1d", "range": "10d"},
            headers={"User-Agent": user_agent},
            timeout=timeout,
        )
    except requests.RequestException:
        raise RuntimeError("stock request failed") from None
    if response.status_code >= 400:
        raise RuntimeError(f"stock HTTP {response.status_code}")
    try:
        payload = response.json()
    except ValueError:
        raise RuntimeError("stock payload is not JSON") from None
    if not isinstance(payload, dict):
        raise RuntimeError("stock payload is not JSON")
    closes = _yahoo_closes(payload)
    if len(closes) < 2:
        return None
    last, prev = closes[-1][1], closes[-2][1]
    change = (last - prev) / prev * 100 if prev else None
    return {
        "name": symbol.upper(),
        "price": last,
        "change_pct": change,
        "date": closes[-1][0],
    }


def fetch(
    crypto_ids: list[str],
    stock_symbols: list[str],
    vs: str = "usd",
    *,
    timeout: float = TIMEOUT,
    user_agent: str = HEADERS["User-Agent"],
    api_key: str | None = None,
) -> dict:
    """A failed crypto call or a failed symbol does not stop the rest."""
    result: dict[str, Any] = {
        "crypto": None,
        "stocks": None,
        "crypto_requested": bool(crypto_ids),
        "stocks_requested": bool(stock_symbols),
    }
    if crypto_ids:
        try:
            result["crypto"] = fetch_crypto(
                crypto_ids,
                vs,
                timeout=timeout,
                user_agent=user_agent,
                api_key=api_key,
            )
        except Exception as exc:
            logger.warning("Crypto unavailable (%s)", type(exc).__name__)
    if stock_symbols:
        stocks: list[dict] = []
        for symbol in stock_symbols:
            try:
                item = fetch_stock(symbol, timeout=timeout, user_agent=user_agent)
            except Exception as exc:
                logger.warning("Stock unavailable (%s)", type(exc).__name__)
                continue
            if item:
                stocks.append(item)
        result["stocks"] = stocks or None
    return result


def format_markets(data: Mapping[str, Any]) -> str:
    """Prices are formatted here. This is information, not a buy or sell recommendation."""
    lines = ["📈 ბაზრები"]
    if data.get("crypto_requested", True):
        crypto = data.get("crypto")
        if crypto:
            for item in crypto:
                lines.append(_crypto_line(item))
        else:
            lines.append(CRYPTO_UNAVAILABLE)
    if data.get("stocks_requested", True):
        stocks = data.get("stocks")
        if stocks:
            for item in stocks:
                lines.append(_stock_line(item))
        else:
            lines.append(STOCKS_UNAVAILABLE)
    return "\n".join(lines)


def _crypto_line(item: Mapping[str, Any]) -> str:
    name = str(item.get("name") or "").strip()
    icon = _CRYPTO_ICONS.get(name.lower())
    label = f"{icon} {name}" if icon else name
    return f"{label}: {_price(item.get('price'))}{_change(item.get('change_pct'), ' / 24სთ')}"


def _stock_line(item: Mapping[str, Any]) -> str:
    raw = str(item.get("name") or "").strip()
    ticker = raw.split(".", 1)[0].upper()
    label = _STOCK_LABELS.get(ticker, ticker)
    return f"{label}: {_price(item.get('price'))}{_change(item.get('change_pct'), '')}"


def _yahoo_symbol(symbol: str) -> str:
    return symbol.split(".", 1)[0].strip().upper()


def _yahoo_closes(payload: Mapping[str, Any]) -> list[tuple[str, float]]:
    chart = payload.get("chart")
    result = chart.get("result") if isinstance(chart, dict) else None
    if not isinstance(result, list) or not result or not isinstance(result[0], dict):
        return []
    row = result[0]
    stamps = row.get("timestamp") or []
    quote = row.get("indicators") if isinstance(row.get("indicators"), dict) else {}
    series = quote.get("quote") if isinstance(quote, dict) else None
    if not isinstance(series, list) or not series or not isinstance(series[0], dict):
        return []
    closes = series[0].get("close") or []
    found: list[tuple[str, float]] = []
    for stamp, close in zip(stamps, closes):
        if close is None:
            continue
        try:
            price = float(close)
            day = datetime.fromtimestamp(int(stamp), timezone.utc).date().isoformat()
        except (TypeError, ValueError, OSError):
            continue
        found.append((day, price))
    return found


def _price(value: Any) -> str:
    number = float(value)
    if abs(number) >= 1000:
        return f"${number:,.0f}"
    if abs(number) >= 1:
        return f"${number:,.2f}"
    return f"${number:,.4f}"


def _change(value: Any, suffix: str) -> str:
    if value is None:
        return ""
    number = float(value)
    arrow = "▲" if number >= 0 else "▼"
    return f" ({arrow} {abs(number):.1f}%{suffix})"


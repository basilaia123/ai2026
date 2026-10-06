"""Official GEL rates. National Bank of Georgia first, open.er-api.com as fallback."""

from __future__ import annotations

import logging
from typing import Any, Mapping

import requests

from core.interfaces import FxSource as FxSourceBase

logger = logging.getLogger(__name__)

NBG_LABEL = "ეროვნული ბანკი"


class FxSource(FxSourceBase):
    def __init__(
        self,
        *,
        codes: list[str],
        timeout: float,
        user_agent: str,
        nbg_url: str,
        er_url: str,
    ) -> None:
        self._codes = [code.strip().upper() for code in codes if code.strip()]
        self._timeout = timeout
        self._user_agent = user_agent
        self._nbg_url = nbg_url
        self._er_url = er_url

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "FxSource":
        del env
        block = config["fx"]
        codes = block.get("currencies") or ["USD", "EUR"]
        return cls(
            codes=[str(code) for code in codes],
            timeout=float(block.get("timeout_seconds", 10)),
            user_agent=str(block.get("user_agent", "morning-briefing/1.0")),
            nbg_url=str(block["nbg_url"]),
            er_url=str(block["er_url"]),
        )

    def fetch(self) -> dict | None:
        return fetch_rates(
            self._codes,
            timeout=self._timeout,
            user_agent=self._user_agent,
            nbg_url=self._nbg_url,
            er_url=self._er_url,
        )


def fetch_rates(
    codes: list[str] | None = None,
    *,
    timeout: float = 10,
    user_agent: str = "morning-briefing/1.0",
    nbg_url: str = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json",
    er_url: str = "https://open.er-api.com/v6/latest/{base}",
) -> dict | None:
    chosen = [code.strip().upper() for code in (codes or ["USD", "EUR"]) if code.strip()]
    getters = (
        ("NBG", lambda: _from_nbg(chosen, nbg_url, timeout, user_agent)),
        ("open.er-api.com", lambda: _from_erapi(chosen, er_url, timeout, user_agent)),
    )
    for name, getter in getters:
        try:
            data = getter()
        except Exception as exc:
            logger.warning("FX source %s unavailable (%s)", name, type(exc).__name__)
            continue
        if data.get("rates"):
            return data
        logger.warning("FX source %s unavailable (%s)", name, "empty")
    return None


def _from_nbg(codes: list[str], url: str, timeout: float, user_agent: str) -> dict:
    payload = _get_json(
        url,
        timeout=timeout,
        user_agent=user_agent,
        params=[("currencies", code) for code in codes],
    )
    return rates_from_nbg(payload, codes)


def _from_erapi(codes: list[str], url_template: str, timeout: float, user_agent: str) -> dict:
    rates: dict[str, dict[str, Any]] = {}
    for code in codes:
        payload = _get_json(url_template.format(base=code), timeout=timeout, user_agent=user_agent)
        gel = _gel_rate(payload)
        rates[code] = {"rate": round(gel, 4), "diff": None}
    return {"source": "open.er-api.com", "date": None, "rates": rates}


def _get_json(
    url: str,
    *,
    timeout: float,
    user_agent: str,
    params: list[tuple[str, str]] | None = None,
) -> Any:
    try:
        response = requests.get(
            url,
            params=params,
            timeout=timeout,
            headers={"User-Agent": user_agent, "Accept": "application/json"},
        )
    except requests.Timeout:
        raise RuntimeError("request timed out") from None
    except requests.ConnectionError:
        raise RuntimeError("connection failed") from None
    except requests.RequestException:
        raise RuntimeError("request failed") from None
    if response.status_code >= 400:
        raise RuntimeError(f"HTTP {response.status_code}")
    try:
        return response.json()
    except ValueError:
        raise RuntimeError("payload is not JSON") from None


def rates_from_nbg(payload: Any, codes: list[str]) -> dict:
    if not isinstance(payload, list) or not payload or not isinstance(payload[0], dict):
        raise ValueError("nbg payload is empty")
    day = payload[0]
    rows = day.get("currencies")
    if not isinstance(rows, list):
        raise ValueError("nbg currencies are missing")
    by_code: dict[str, dict] = {}
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get("code"), str):
            by_code[row["code"].upper()] = row
    result: dict[str, dict[str, Any]] = {}
    for code in codes:
        row = by_code.get(code)
        if row is None or "rate" not in row:
            continue
        quantity = row.get("quantity", 1) or 1
        result[code] = {
            "rate": round(float(row["rate"]) / float(quantity), 4),
            "diff": _number_or_none(row.get("diff")),
        }
    return {"source": "NBG", "date": day.get("date"), "rates": result}


def _gel_rate(payload: Any) -> float:
    if not isinstance(payload, dict):
        raise ValueError("er payload is not an object")
    rates = payload.get("rates")
    if not isinstance(rates, dict) or "GEL" not in rates:
        raise ValueError("GEL rate is missing")
    return float(rates["GEL"])


def _number_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def format_fx(data: Mapping[str, Any]) -> str:
    source = str(data.get("source") or "")
    label = NBG_LABEL if source == "NBG" else source
    lines = [f"💱 ვალუტის კურსი ({label})"]
    rates = data.get("rates")
    if not isinstance(rates, Mapping):
        raise ValueError("rates are missing")
    for code, item in rates.items():
        if not isinstance(item, Mapping) or "rate" not in item:
            continue
        rate = f"{float(item['rate']):.4f}"
        diff = item.get("diff")
        if diff is None:
            lines.append(f"{code}: {rate} ₾")
        else:
            number = float(diff)
            arrow = "▲" if number >= 0 else "▼"
            lines.append(f"{code}: {rate} ₾ ({arrow} {abs(number):.4f})")
    return "\n".join(lines)

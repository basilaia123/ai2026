"""Open-Meteo forecast. No API key. Facts only; the model writes the sentence."""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable, Mapping

from core.interfaces import WeatherSnapshot, WeatherSource

logger = logging.getLogger(__name__)

Opener = Callable[..., Any]

# WMO weather interpretation codes.
_CONDITIONS = {
    0: "მოწმენდილი",
    1: "ძირითადად მოწმენდილი",
    2: "ნაწილობრივ ღრუბლიანი",
    3: "მოღრუბლული",
    45: "ნისლი",
    48: "ნისლი და ჭირხლი",
    51: "სუსტი წვრილი წვიმა",
    53: "წვრილი წვიმა",
    55: "ძლიერი წვრილი წვიმა",
    56: "სუსტი მოყინული წვიმა",
    57: "მოყინული წვიმა",
    61: "სუსტი წვიმა",
    63: "წვიმა",
    65: "ძლიერი წვიმა",
    66: "სუსტი ყინულიანი წვიმა",
    67: "ყინულიანი წვიმა",
    71: "სუსტი თოვლი",
    73: "თოვლი",
    75: "ძლიერი თოვლი",
    77: "თოვლის მარცვლები",
    80: "სუსტი წვიმის ჯერი",
    81: "წვიმის ჯერი",
    82: "ძლიერი წვიმის ჯერი",
    85: "სუსტი თოვლის ჯერი",
    86: "ძლიერი თოვლის ჯერი",
    95: "ჭექა-ქუხილი",
    96: "ჭექა-ქუხილი და სეტყვა",
    99: "ძლიერი ჭექა-ქუხილი და სეტყვა",
}


class OpenMeteoWeatherSource(WeatherSource):
    def __init__(
        self,
        *,
        city: str,
        latitude: float,
        longitude: float,
        timezone_name: str,
        base_url: str,
        timeout: float,
        opener: Opener | None = None,
    ) -> None:
        self._city = city
        self._latitude = latitude
        self._longitude = longitude
        self._timezone_name = timezone_name
        self._base_url = base_url
        self._timeout = timeout
        self._opener = opener or urllib.request.urlopen

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "OpenMeteoWeatherSource":
        del env
        weather = config["weather"]
        return cls(
            city=str(weather["city"]),
            latitude=float(weather["latitude"]),
            longitude=float(weather["longitude"]),
            timezone_name=str(weather.get("timezone") or config["timezone"]),
            base_url=str(weather.get("base_url", "https://api.open-meteo.com/v1/forecast")),
            timeout=float(weather.get("timeout_seconds", 20)),
        )

    def fetch(self) -> WeatherSnapshot:
        query = urllib.parse.urlencode(
            {
                "latitude": self._latitude,
                "longitude": self._longitude,
                "current": "temperature_2m,weather_code,wind_speed_10m",
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                "timezone": self._timezone_name,
                "forecast_days": 1,
                "temperature_unit": "celsius",
                "wind_speed_unit": "kmh",
            }
        )
        request = urllib.request.Request(
            f"{self._base_url}?{query}",
            headers={"User-Agent": "morning-briefing"},
        )
        try:
            with self._opener(request, timeout=self._timeout) as response:
                raw = response.read()
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"Weather HTTP {exc.code}") from None
        except urllib.error.URLError:
            raise RuntimeError("Weather HTTP failed") from None
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("Weather payload is not JSON") from exc
        if not isinstance(payload, dict):
            raise RuntimeError("Weather payload is not an object")
        text = facts_from_payload(payload, self._city)
        logger.info("Weather facts ready for %s", self._city)
        return WeatherSnapshot(text=text)


def facts_from_payload(payload: Mapping[str, Any], city: str) -> str:
    current = payload.get("current")
    if not isinstance(current, dict) or current.get("temperature_2m") is None:
        raise ValueError("weather payload has no current temperature")
    daily = payload.get("daily") if isinstance(payload.get("daily"), dict) else {}
    lines = [f"ქალაქი: {city}"]
    lines.append(f"ახლანდელი ტემპერატურა: {_num(current.get('temperature_2m'), 1)}°C")
    condition = _condition(current.get("weather_code"))
    if condition:
        lines.append(f"მდგომარეობა: {condition}")
    wind = _num(current.get("wind_speed_10m"), 0)
    if wind is not None:
        lines.append(f"ქარი: {wind} კმ/სთ")
    minimum = _num(_first(daily.get("temperature_2m_min")), 1)
    maximum = _num(_first(daily.get("temperature_2m_max")), 1)
    if minimum is not None:
        lines.append(f"დღის მინიმუმი: {minimum}°C")
    if maximum is not None:
        lines.append(f"დღის მაქსიმუმი: {maximum}°C")
    rain = _num(_first(daily.get("precipitation_probability_max")), 0)
    if rain is not None:
        lines.append(f"ნალექის ალბათობა: {rain}%")
    return "\n".join(lines)


def _condition(code: Any) -> str | None:
    if code is None:
        return None
    try:
        number = int(code)
    except (TypeError, ValueError):
        return None
    return _CONDITIONS.get(number, f"კოდი {number}")


def _first(value: Any) -> Any:
    if isinstance(value, list):
        return value[0] if value else None
    return value


def _num(value: Any, digits: int) -> str | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if digits == 0:
        return str(int(round(number)))
    return f"{number:.{digits}f}"

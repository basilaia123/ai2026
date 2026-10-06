"""LLMProvider via LiteLLM. Model names come from config, one after another."""

from __future__ import annotations

import logging
import os
import time
from typing import Any, Callable, Mapping, Sequence

from core.interfaces import LLMProvider
from core.redact import scrub

logger = logging.getLogger(__name__)

CompleteFn = Callable[..., str]
SleepFn = Callable[[float], None]


class ModelFailure(RuntimeError):
    def __init__(self, reason: str, detail: str) -> None:
        self.reason = reason
        self.detail = detail
        super().__init__(f"მოდელი მიუწვდომელია\nმიზეზი: {reason}")


class LiteLLMProvider(LLMProvider):
    def __init__(
        self,
        models: Sequence[str],
        *,
        temperature: float,
        max_tokens: int,
        complete_fn: CompleteFn | None = None,
        sleep_fn: SleepFn | None = None,
        rate_limit_retry_seconds: float = 3,
    ) -> None:
        cleaned = [model.strip() for model in models if isinstance(model, str) and model.strip()]
        if not cleaned:
            raise ValueError("llm.models must be a non-empty list")
        self._models = cleaned
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._complete_fn = complete_fn or default_complete
        self._sleep = sleep_fn or time.sleep
        self._retry_wait = rate_limit_retry_seconds

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "LiteLLMProvider":
        del env  # LiteLLM reads the API key from the process environment.
        llm = config["llm"]
        return cls(
            models=list(llm["models"]),
            temperature=float(llm.get("temperature", 0.1)),
            max_tokens=int(llm.get("max_tokens", 800)),
            rate_limit_retry_seconds=float(llm.get("rate_limit_retry_seconds", 3)),
        )

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        failures: list[tuple[str, str]] = []
        for model in self._models:
            text, reason, detail = self._complete_model(model, messages)
            if text is not None:
                logger.info("Model succeeded: %s", model)
                return text
            failures.append((reason, f"{model}: {detail}"))
            logger.warning("Model %s failed: %s", model, reason)
        reasons: list[str] = []
        for reason, _detail in failures:
            if reason not in reasons:
                reasons.append(reason)
        raise ModelFailure(". ".join(reasons), "\n".join(detail for _reason, detail in failures))

    def _complete_model(self, model: str, messages: list[dict[str, str]]) -> tuple[str | None, str, str]:
        try:
            return self._once(model, messages), "", ""
        except Exception as exc:
            self._log_failure(model, exc)
            if not _is_rate_limit(exc):
                return None, explain_failure(exc), scrub(str(exc))
            self._sleep(self._retry_wait)
            try:
                return self._once(model, messages), "", ""
            except Exception as retry_exc:
                self._log_failure(model, retry_exc)
                return None, explain_failure(retry_exc), scrub(str(retry_exc))

    def _log_failure(self, model: str, exc: BaseException) -> None:
        logger.error("Model %s error (%s): %s", model, type(exc).__name__, scrub(str(exc)))

    def _once(self, model: str, messages: list[dict[str, str]]) -> str:
        text = self._complete_fn(
            model=model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
        )
        cleaned = _as_text(text).strip()
        if not cleaned:
            raise RuntimeError("empty completion")
        return cleaned


def explain_failure(exc: BaseException) -> str:
    if _is_rate_limit(exc):
        return "ლიმიტი ამოიწურა"
    if _is_timeout(exc):
        return "დრო ამოიწურა"
    if type(exc).__name__ in {"ModuleNotFoundError", "ImportError"}:
        return "საჭირო ბიბლიოთეკა არ არის დაყენებული"
    status = _status(exc)
    name = type(exc).__name__.lower()
    if status in {401, 403} or "auth" in name or "permission" in name:
        return "API გასაღები არასწორია"
    if status == 404 or name == "notfounderror" or "not_found" in name:
        return "მოდელი ვერ მოიძებნა"
    lowered = scrub(str(exc)).lower()
    if "api key" in lowered or "api_key_invalid" in lowered or "unauthenticated" in lowered:
        return "API გასაღები არასწორია"
    if "not found" in lowered or "is not found" in lowered or "model_not_found" in lowered:
        return "მოდელი ვერ მოიძებნა"
    return type(exc).__name__


def _status(exc: BaseException) -> int | None:
    status = getattr(exc, "status_code", None)
    if isinstance(status, int):
        return status
    response = getattr(exc, "response", None)
    code = getattr(response, "status_code", None)
    if isinstance(code, int):
        return code
    return None


def _is_timeout(exc: BaseException) -> bool:
    if _status(exc) == 408:
        return True
    return "timeout" in type(exc).__name__.lower()


def _is_rate_limit(exc: BaseException) -> bool:
    if getattr(exc, "status_code", None) == 429:
        return True
    response = getattr(exc, "response", None)
    if getattr(response, "status_code", None) == 429:
        return True
    return type(exc).__name__ == "RateLimitError"


def default_complete(*, model: str, messages: list[dict[str, str]], temperature: float, max_tokens: int) -> str:
    import litellm

    os.environ.setdefault("LITELLM_LOG", "ERROR")
    litellm.suppress_debug_info = True
    litellm.drop_params = True
    try:
        litellm.telemetry = False
    except Exception:
        pass
    try:
        litellm.set_verbose = False
    except Exception:
        pass
    response = litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return _as_text(response.choices[0].message.content)


def _as_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict):
                parts.append(str(part.get("text", "")))
            else:
                parts.append(str(getattr(part, "text", "")))
        return "".join(parts)
    return str(content)

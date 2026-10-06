"""Shared fakes for wiring tests. Not a production provider."""

from __future__ import annotations

from typing import Any, Mapping

from core.interfaces import LLMProvider


class RecordingLLM(LLMProvider):
    seen_models: list[str] | None = None
    last_system = ""
    last_user = ""

    def __init__(self, models: list[str], text: str) -> None:
        self.models = models
        self.text = text

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "RecordingLLM":
        del env
        llm = config["llm"]
        instance = cls(list(llm["models"]), str(llm.get("fake_text", "ბრიფინგი")))
        cls.seen_models = instance.models
        return instance

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        type(self).last_system = system_prompt
        type(self).last_user = user_prompt
        return self.text

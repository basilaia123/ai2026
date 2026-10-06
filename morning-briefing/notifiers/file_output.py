"""Write the briefing to a local file. Nothing leaves the machine."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from core.interfaces import Notifier


class FileNotifier(Notifier):
    def __init__(self, path: Path) -> None:
        self._path = path

    @classmethod
    def from_config(cls, config: Mapping[str, Any], env: Mapping[str, str]) -> "FileNotifier":
        del env
        raw = Path(str(config["delivery"]["file_path"]))
        if not raw.is_absolute():
            raw = Path(__file__).resolve().parents[1] / raw
        return cls(raw)

    def send(self, subject: str, body: str) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        text = f"{subject}\n\n{body.rstrip()}\n"
        self._path.write_text(text, encoding="utf-8")

"""Load a class from a 'package.module:ClassName' config string."""

from __future__ import annotations

import importlib
from typing import Any


def load_symbol(spec: str) -> Any:
    if not isinstance(spec, str) or ":" not in spec:
        raise ValueError(f"Component spec must be 'module:Class', got {spec!r}")
    module_name, _, attr = spec.partition(":")
    module_name = module_name.strip()
    attr = attr.strip()
    if not module_name or not attr:
        raise ValueError(f"Component spec must be 'module:Class', got {spec!r}")
    module = importlib.import_module(module_name)
    try:
        return getattr(module, attr)
    except AttributeError as exc:
        raise ValueError(f"Component not found: {spec}") from exc

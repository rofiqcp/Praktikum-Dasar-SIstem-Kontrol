from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import time


def encode_command(key: str, value) -> bytes:
    key = str(key).strip().upper()
    if not key or "," in key or "\n" in key:
        raise ValueError("invalid command key")
    text = str(value).strip().replace("\r", "").replace("\n", "")
    return f"{key},{text}\n".encode("ascii", errors="strict")


def safe_float(text: str, default=float("nan")) -> float:
    try:
        return float(text)
    except (TypeError, ValueError):
        return default


@dataclass
class Heartbeat:
    interval_s: float = 0.5
    _last: float = 0.0

    def due(self, now: Optional[float] = None) -> bool:
        now = time.monotonic() if now is None else now
        if now - self._last >= self.interval_s:
            self._last = now
            return True
        return False

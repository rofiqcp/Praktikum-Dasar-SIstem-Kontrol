"""Reusable step-response metrics for laboratory data.

The implementation intentionally avoids requiring control-system-specific packages.
It accepts array-like time, process value, and either scalar or array-like setpoint.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable
import math
import numpy as np


@dataclass
class StepMetrics:
    initial_value: float = math.nan
    final_setpoint: float = math.nan
    final_value: float = math.nan
    delay_time_s: float = math.nan
    rise_time_s: float = math.nan
    peak_time_s: float = math.nan
    settling_time_s: float = math.nan
    maximum_overshoot_pct: float = math.nan
    steady_state_error: float = math.nan

    def as_dict(self) -> dict[str, float]:
        return asdict(self)


def _first_crossing(t: np.ndarray, y: np.ndarray, level: float, direction: float) -> float:
    if direction >= 0:
        idx = np.flatnonzero(y >= level)
    else:
        idx = np.flatnonzero(y <= level)
    return float(t[idx[0]]) if idx.size else math.nan


def step_metrics(
    time_s: Iterable[float],
    process_value: Iterable[float],
    setpoint: float | Iterable[float],
    settling_band: float = 0.02,
    tail_fraction: float = 0.10,
) -> dict[str, float]:
    """Calculate common response metrics.

    Definitions used by this repository:
    - delay time: first crossing of 50% of commanded step.
    - rise time: t90 - t10.
    - peak time: time of extreme response in the commanded direction.
    - settling time: earliest time after which all remaining samples are inside
      ±settling_band of step magnitude (2% default).
    - maximum overshoot: excess beyond final SP relative to step magnitude.
    - steady-state error: final SP minus mean of last tail_fraction samples.

    Returns NaN when a metric cannot be defined from the provided data.
    """
    t = np.asarray(list(time_s), dtype=float)
    y = np.asarray(list(process_value), dtype=float)
    if np.isscalar(setpoint):
        sp = np.full_like(y, float(setpoint))
    else:
        sp = np.asarray(list(setpoint), dtype=float)

    if t.size < 3 or y.size != t.size or sp.size != t.size:
        raise ValueError("time, process_value, and setpoint must have equal length >= 3")

    mask = np.isfinite(t) & np.isfinite(y) & np.isfinite(sp)
    t, y, sp = t[mask], y[mask], sp[mask]
    if t.size < 3:
        raise ValueError("not enough finite samples")

    order = np.argsort(t)
    t, y, sp = t[order], y[order], sp[order]
    t = t - t[0]

    n_tail = max(3, int(round(t.size * tail_fraction)))
    y0 = float(np.mean(y[: min(3, y.size)]))
    spf = float(np.mean(sp[-n_tail:]))
    yss = float(np.mean(y[-n_tail:]))
    delta = spf - y0
    direction = 1.0 if delta >= 0 else -1.0
    amp = abs(delta)

    out = StepMetrics(initial_value=y0, final_setpoint=spf, final_value=yss)
    out.steady_state_error = spf - yss

    if amp <= 1e-12:
        return out.as_dict()

    l10 = y0 + 0.10 * delta
    l50 = y0 + 0.50 * delta
    l90 = y0 + 0.90 * delta

    t10 = _first_crossing(t, y, l10, direction)
    t50 = _first_crossing(t, y, l50, direction)
    t90 = _first_crossing(t, y, l90, direction)
    out.delay_time_s = t50
    if math.isfinite(t10) and math.isfinite(t90):
        out.rise_time_s = t90 - t10

    peak_idx = int(np.argmax(y) if direction > 0 else np.argmin(y))
    peak = float(y[peak_idx])
    out.peak_time_s = float(t[peak_idx])
    overshoot = direction * (peak - spf)
    out.maximum_overshoot_pct = max(0.0, overshoot / amp * 100.0)

    band = max(amp * settling_band, 1e-9)
    err = np.abs(y - spf)
    inside = err <= band
    settle = math.nan
    for i in range(inside.size):
        if bool(np.all(inside[i:])):
            settle = float(t[i])
            break
    out.settling_time_s = settle
    return out.as_dict()

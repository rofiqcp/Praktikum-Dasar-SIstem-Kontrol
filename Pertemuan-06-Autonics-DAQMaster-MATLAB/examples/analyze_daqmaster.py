#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "shared" / "python"))
from response_metrics import step_metrics  # noqa: E402


def pick(cols, names):
    lut = {c.lower(): c for c in cols}
    for name in names:
        if name.lower() in lut:
            return lut[name.lower()]
    return None


def main():
    ap = argparse.ArgumentParser(description="Analyze P6 CSV data")
    ap.add_argument("csv", type=Path)
    args = ap.parse_args()

    source = args.csv.expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"file not found: {source}")

    df = pd.read_csv(source)
    cols = list(df.columns)
    tc = pick(cols, ["time_s", "time", "seconds"])
    yc = pick(cols, ["PV_C", "PV", "value", "temperature_C", "temp_C"])
    sc = pick(cols, ["SV_C", "SV", "SP", "setpoint_C", "sp_C"])
    if not all((tc, yc, sc)):
        raise SystemExit(f"required columns not found; available={cols}")

    out = pd.DataFrame({
        "time_s": pd.to_numeric(df[tc], errors="coerce"),
        "pv": pd.to_numeric(df[yc], errors="coerce"),
        "sp": pd.to_numeric(df[sc], errors="coerce"),
    })

    if len(out) < 3 or not np.isfinite(out.to_numpy()).all():
        raise SystemExit("dataset must contain at least 3 finite rows")

    dt = np.diff(out.time_s.to_numpy())
    if np.any(dt <= 0):
        raise SystemExit("timestamps must be strictly increasing")

    metrics = step_metrics(out.time_s, out.pv, out.sp)
    result_dir = HERE / "results"
    result_dir.mkdir(exist_ok=True)
    out.to_csv(result_dir / "normalized.csv", index=False)
    pd.DataFrame([metrics]).to_csv(result_dir / "metrics.csv", index=False)

    print("rows:", len(out))
    print("dt min/median/max:", float(dt.min()), float(np.median(dt)), float(dt.max()))
    for key, value in metrics.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

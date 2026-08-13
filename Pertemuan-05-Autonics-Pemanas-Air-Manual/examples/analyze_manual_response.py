from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'templates' / 'template_pengamatan.csv'
df = pd.read_csv(path)
required = ['time_s','setpoint_C','temperature_C']
missing = [c for c in required if c not in df.columns]
if missing:
    raise SystemExit(f'Missing columns: {missing}')
df = df.dropna(subset=required).sort_values('time_s')
if len(df) < 3:
    raise SystemExit('Need at least 3 valid rows')
summary = pd.DataFrame([{
    'file': path.name,
    'samples': len(df),
    'duration_s': df.time_s.iloc[-1] - df.time_s.iloc[0],
    'peak_C': df.temperature_C.max(),
    'final_error_C': (df.setpoint_C-df.temperature_C).iloc[-1],
}])
out = path.resolve().parent / 'analysis'
out.mkdir(exist_ok=True)
summary.to_csv(out/'summary.csv', index=False)
fig = plt.figure(figsize=(10,6))
plt.plot(df.time_s, df.temperature_C, 'o-', label='PV')
plt.plot(df.time_s, df.setpoint_C, '--', label='SV')
plt.xlabel('Time (s)'); plt.ylabel('Temperature (C)'); plt.grid(True); plt.legend(); fig.tight_layout()
fig.savefig(out/'response.png', dpi=160)
print(summary.to_string(index=False))
print('saved:', out)

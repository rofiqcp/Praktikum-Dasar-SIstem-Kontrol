from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    raise SystemExit('usage: python compare_manual_runs.py run1.csv [run2.csv ...]')

rows=[]
fig=plt.figure(figsize=(10,6))
for name in sys.argv[1:]:
    p=Path(name)
    df=pd.read_csv(p)
    needed=['time_s','setpoint_C','temperature_C']
    df=df.dropna(subset=needed).sort_values('time_s')
    rows.append({'file':p.name,'samples':len(df),'peak_C':float(df.temperature_C.max()),'final_error_C':float((df.setpoint_C-df.temperature_C).iloc[-1])})
    plt.plot(df.time_s,df.temperature_C,label=p.stem)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.legend()
fig.tight_layout()
fig.savefig('p5_manual_comparison.png',dpi=160)
summary=pd.DataFrame(rows)
summary.to_csv('p5_manual_comparison_summary.csv',index=False)
print(summary.to_string(index=False))

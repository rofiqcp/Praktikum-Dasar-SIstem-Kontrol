import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]/'shared'))
from control_metrics import step_metrics
f=Path(__file__).resolve().parents[1]/'templates'/'template_pengamatan.csv'
df=pd.read_csv(f).dropna(subset=['temperature_C'])
if len(df)<3: raise SystemExit('Isi template dengan minimal 3 data.')
m=step_metrics(df.time_s,df.temperature_C,df.setpoint_C)
print(m)
plt.plot(df.time_s,df.temperature_C,'o-',label='PV'); plt.plot(df.time_s,df.setpoint_C,'--',label='SV'); plt.grid(); plt.legend(); plt.show()

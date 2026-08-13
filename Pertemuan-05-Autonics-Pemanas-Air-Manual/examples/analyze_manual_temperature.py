import sys, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/'common'))
try:
    from response_metrics import response_metrics
except Exception:
    # fallback when run from module folder
    sys.path.append(str(Path(__file__).resolve().parents[2].parent/'common'))
    from response_metrics import response_metrics
f=sys.argv[1] if len(sys.argv)>1 else 'template_manual_temperature.csv'
df=pd.read_csv(f); sp=float(df['setpoint_c'].iloc[-1]); m=response_metrics(df.time_s,df.temp_c,sp)
print(pd.Series(m));
ax=df.plot(x='time_s',y=['temp_c','setpoint_c'],grid=True); ax.set_ylabel('°C'); plt.tight_layout(); plt.show()

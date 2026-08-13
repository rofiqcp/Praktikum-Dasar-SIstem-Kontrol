import argparse,sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'shared'/'python'))
from response_metrics import step_metrics

ap=argparse.ArgumentParser();ap.add_argument('csv');a=ap.parse_args();df=pd.read_csv(a.csv)
mode=int(round(df['mode'].iloc[-1]));y=df['rpm_lpf'] if mode==1 else df['position_deg'];t=(df['ms']-df['ms'].iloc[0])/1000
m=step_metrics(t.to_numpy(),y.to_numpy(),df['sp'].to_numpy());print(pd.Series(m).to_string())
out=Path(a.csv).with_name(Path(a.csv).stem+'_analysis.jpg');plt.figure(figsize=(11,6));plt.plot(t,df.sp,label='SP');plt.plot(t,y,label='RPM LPF' if mode==1 else 'Position');plt.grid(True);plt.legend();plt.tight_layout();plt.savefig(out,dpi=160);print('saved',out)

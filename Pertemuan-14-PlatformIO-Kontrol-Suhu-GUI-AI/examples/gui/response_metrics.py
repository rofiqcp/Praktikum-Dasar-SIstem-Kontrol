import sys,pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]/'shared'))
from control_metrics import step_metrics
f=sys.argv[1];d=pd.read_csv(f);print(step_metrics(d.ms/1000,d.temp_C,d.sp_C))

import sys, pandas as pd, matplotlib.pyplot as plt
f=sys.argv[1] if len(sys.argv)>1 else 'daq_export.csv'
df=pd.read_csv(f)
# Ganti nama kolom sesuai hasil export DAQMaster Anda.
lookup={c.lower().strip():c for c in df.columns}
def pick(*names):
    for n in names:
        if n in lookup:return lookup[n]
    raise KeyError(f'Kolom {names} tidak ditemukan: {list(df.columns)}')
t=pick('time_s','time','elapsed'); pv=pick('pv','temp_c','temperature');
sv=pick('sv','setpoint_c','setpoint')
df.plot(x=t,y=[pv,sv],grid=True); plt.ylabel('Temperature'); plt.tight_layout(); plt.show()
print(df[[t,pv,sv]].describe())

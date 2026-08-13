import numpy as np

def response_metrics(t, y, setpoint):
    t=np.asarray(t,float); y=np.asarray(y,float)
    if len(t)<3: return {}
    y0=y[0]; amp=setpoint-y0
    if abs(amp)<1e-12: return {}
    norm=(y-y0)/amp
    def first_time(mask):
        idx=np.where(mask)[0]
        return float(t[idx[0]]) if idx.size else float('nan')
    delay=first_time(norm>=0.5)
    t10=first_time(norm>=0.1); t90=first_time(norm>=0.9)
    rise=t90-t10 if np.isfinite(t10) and np.isfinite(t90) else float('nan')
    peak_idx=int(np.argmax(y) if amp>0 else np.argmin(y))
    peak_time=float(t[peak_idx]); peak=float(y[peak_idx])
    overshoot=max(0.0, (peak-setpoint)/abs(amp)*100.0) if amp>0 else max(0.0,(setpoint-peak)/abs(amp)*100.0)
    band=0.02*abs(amp)
    settling=float('nan')
    for i in range(len(y)):
        if np.all(np.abs(y[i:]-setpoint)<=band):
            settling=float(t[i]); break
    ess=float(setpoint-y[-1])
    return dict(delay_time=delay,rise_time=rise,peak_time=peak_time,peak_value=peak,settling_time=settling,maximum_overshoot_percent=overshoot,steady_state_error=ess)

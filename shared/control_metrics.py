from __future__ import annotations
import numpy as np


def step_metrics(t, y, sp, settle_band=0.02):
    """Return simple step-response metrics for lab data.

    t, y: 1D arrays. sp can be scalar or array. Metrics are best-effort and
    intentionally transparent for teaching, not a replacement for formal identification.
    """
    t=np.asarray(t,dtype=float); y=np.asarray(y,dtype=float)
    if np.ndim(sp):
        sp_arr=np.asarray(sp,dtype=float); target=float(np.nanmedian(sp_arr[-max(3,len(sp_arr)//10):]))
        initial_sp=float(sp_arr[0])
    else:
        target=float(sp); initial_sp=target
    y0=float(np.nanmedian(y[:max(1,min(5,len(y)))]))
    amp=target-y0
    if len(t)<3 or abs(amp)<1e-12:
        return {k: float('nan') for k in ['delay_time','rise_time','peak_time','settling_time','overshoot_pct','steady_state_error']}
    direction=1 if amp>=0 else -1
    yn=(y-y0)*direction; A=abs(amp)
    def first_cross(level):
        idx=np.where(yn>=level*A)[0]
        return float(t[idx[0]]-t[0]) if len(idx) else float('nan')
    t10=first_cross(0.10); t50=first_cross(0.50); t90=first_cross(0.90)
    rise=t90-t10 if np.isfinite(t10) and np.isfinite(t90) else float('nan')
    if direction>0: ip=int(np.nanargmax(y))
    else: ip=int(np.nanargmin(y))
    peak=float(y[ip]); peak_time=float(t[ip]-t[0])
    overshoot=max(0.0, direction*(peak-target))/max(abs(amp),1e-12)*100.0
    band=max(abs(target)*settle_band, 0.02*max(abs(amp),1.0))
    err=np.abs(y-target)
    settling=float('nan')
    for i in range(len(y)):
        if np.all(err[i:]<=band):
            settling=float(t[i]-t[0]); break
    ess=float(target-np.nanmean(y[-max(3,len(y)//10):]))
    return {'delay_time':t50,'rise_time':rise,'peak_time':peak_time,'settling_time':settling,'overshoot_pct':overshoot,'steady_state_error':ess}

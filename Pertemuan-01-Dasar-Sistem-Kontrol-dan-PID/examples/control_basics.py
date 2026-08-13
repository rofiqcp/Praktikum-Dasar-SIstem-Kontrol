import numpy as np
import matplotlib.pyplot as plt

DT=0.1; T_END=120.0; SP=60.0; AMBIENT=25.0
TAU=35.0; HEATER_GAIN=0.85

def simulate(mode,kp=3.0,ki=0.08,kd=2.0):
    t=np.arange(0,T_END+DT,DT); temp=np.zeros_like(t); temp[0]=AMBIENT
    integ=0.0; prev_e=SP-temp[0]
    for k in range(1,len(t)):
        e=SP-temp[k-1]
        if mode=='open': u=55.0
        else:
            integ+=e*DT
            deriv=(e-prev_e)/DT
            if mode=='P': u=kp*e
            elif mode=='PI': u=kp*e+ki*integ
            else: u=kp*e+ki*integ+kd*deriv
        u=float(np.clip(u,0,100))
        dT=((AMBIENT-temp[k-1])/TAU + HEATER_GAIN*u/100.0)*DT
        temp[k]=temp[k-1]+dT
        prev_e=e
    return t,temp

for mode in ['open','P','PI','PID']:
    t,y=simulate(mode)
    plt.plot(t,y,label=mode)
plt.axhline(SP,ls='--',label='setpoint')
plt.xlabel('Waktu (s)'); plt.ylabel('Suhu model (°C)'); plt.grid(True); plt.legend(); plt.tight_layout(); plt.show()

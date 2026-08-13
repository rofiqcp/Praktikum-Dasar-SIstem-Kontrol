from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

DT = 0.05
T_END = 40.0
SP = 50.0
PLANT_K = 1.0
TAU = 5.0
KP = 2.0
KI = 0.35
KD = 0.20
U_MIN = 0.0
U_MAX = 100.0

def simulate_open_loop(duty=50.0):
    t = np.arange(0.0, T_END + DT, DT)
    y = np.zeros_like(t)
    for k in range(1, len(t)):
        dy = (-y[k - 1] + PLANT_K * duty) / TAU
        y[k] = y[k - 1] + DT * dy
    return t, y

def simulate_pid():
    t = np.arange(0.0, T_END + DT, DT)
    y = np.zeros_like(t); u = np.zeros_like(t)
    pterm=np.zeros_like(t);iterm=np.zeros_like(t);dterm=np.zeros_like(t)
    integral=0.0;prev_y=0.0
    for k in range(1,len(t)):
        e=SP-y[k-1];p=KP*e;d=-KD*(y[k-1]-prev_y)/DT
        candidate_i=integral+KI*e*DT;raw_candidate=p+candidate_i+d
        high=raw_candidate>U_MAX;low=raw_candidate<U_MIN
        if (not high and not low) or (high and e<0) or (low and e>0): integral=candidate_i
        raw=p+integral+d;u[k]=np.clip(raw,U_MIN,U_MAX);pterm[k],iterm[k],dterm[k]=p,integral,d
        dy=(-y[k-1]+PLANT_K*u[k])/TAU;prev_y=y[k-1];y[k]=y[k-1]+DT*dy
    return t,y,u,pterm,iterm,dterm

def main():
    out=Path(__file__).resolve().parent/'output';out.mkdir(exist_ok=True)
    t,y_ol=simulate_open_loop(50.0);tc,y,u,p,i,d=simulate_pid()
    fig,ax=plt.subplots(2,1,figsize=(10,8),sharex=True)
    ax[0].plot(t,y_ol,label='Open-loop PV');ax[0].plot(t,np.full_like(t,SP),'--',label='SP');ax[0].set_ylabel('PV');ax[0].grid(True);ax[0].legend()
    ax[1].plot(tc,y,label='Closed-loop PV');ax[1].plot(tc,np.full_like(tc,SP),'--',label='SP');ax[1].plot(tc,u,label='Control %',alpha=.8);ax[1].set_xlabel('Time (s)');ax[1].set_ylabel('PV / Control');ax[1].grid(True);ax[1].legend()
    fig.suptitle(f'PID basics Kp={KP}, Ki={KI}, Kd={KD}');fig.tight_layout();png=out/'pid_basics.png';fig.savefig(png,dpi=160)
    print(f'Saved {png}');print(f'Final PV={y[-1]:.3f}, final error={SP-y[-1]:.3f}')
if __name__=='__main__': main()

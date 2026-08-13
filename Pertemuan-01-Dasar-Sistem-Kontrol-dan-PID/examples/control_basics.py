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
    y = np.zeros_like(t)
    u = np.zeros_like(t)
    integral = 0.0
    prev_y = 0.0
    for k in range(1, len(t)):
        error = SP - y[k - 1]
        p = KP * error
        d = -KD * (y[k - 1] - prev_y) / DT
        candidate_i = integral + KI * error * DT
        candidate = p + candidate_i + d
        if (candidate <= U_MAX or error < 0) and (candidate >= U_MIN or error > 0):
            integral = candidate_i
        u[k] = np.clip(p + integral + d, U_MIN, U_MAX)
        dy = (-y[k - 1] + PLANT_K * u[k]) / TAU
        prev_y = y[k - 1]
        y[k] = y[k - 1] + DT * dy
    return t, y, u


def main():
    out = Path(__file__).resolve().parent / 'output'
    out.mkdir(exist_ok=True)
    t, y_open = simulate_open_loop()
    tc, y_closed, u = simulate_pid()
    fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ax[0].plot(t, y_open, label='Open-loop PV')
    ax[0].plot(t, np.full_like(t, SP), '--', label='SP')
    ax[0].grid(True); ax[0].legend(); ax[0].set_ylabel('PV')
    ax[1].plot(tc, y_closed, label='Closed-loop PV')
    ax[1].plot(tc, np.full_like(tc, SP), '--', label='SP')
    ax[1].plot(tc, u, label='Control output')
    ax[1].grid(True); ax[1].legend(); ax[1].set_xlabel('Time (s)')
    fig.tight_layout()
    fig.savefig(out / 'pid_basics.png', dpi=160)
    print(f'Final PV={y_closed[-1]:.3f}; error={SP-y_closed[-1]:.3f}')


if __name__ == '__main__':
    main()

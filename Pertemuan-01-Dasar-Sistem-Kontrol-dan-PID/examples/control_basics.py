import numpy as np
import matplotlib.pyplot as plt

# Simulasi diskrit sederhana agar alur PID terlihat jelas.
# Plant orde-1: dy/dt = (-y + K*u) / tau
K = 1.0
tau = 2.0
sp = 1.0
kp, ki, kd = 2.0, 0.8, 0.15
umin, umax = 0.0, 2.0
Ts = 0.01
Tend = 20.0


def simulate(mode="PID"):
    t = np.arange(0.0, Tend + Ts, Ts)
    y = np.zeros_like(t)
    u = np.zeros_like(t)
    integral = 0.0
    e_prev = sp - y[0]

    for k in range(1, len(t)):
        e = sp - y[k - 1]
        derivative = (e - e_prev) / Ts

        p_term = kp * e if "P" in mode else 0.0
        i_candidate = integral + e * Ts if "I" in mode else 0.0
        i_term = ki * i_candidate if "I" in mode else 0.0
        d_term = kd * derivative if "D" in mode else 0.0

        u_unsat = p_term + i_term + d_term
        u[k] = np.clip(u_unsat, umin, umax)

        # Conditional integration anti-windup:
        # integral hanya diterima jika tidak memperparah saturasi.
        if "I" in mode:
            saturating_high = u_unsat > umax and e > 0
            saturating_low = u_unsat < umin and e < 0
            if not (saturating_high or saturating_low):
                integral = i_candidate

        y_dot = (-y[k - 1] + K * u[k]) / tau
        y[k] = y[k - 1] + Ts * y_dot
        e_prev = e

    return t, y, u


plt.figure(figsize=(10, 5))
for mode in ["P", "PI", "PID"]:
    t, y, _ = simulate(mode)
    plt.plot(t, y, label=mode)
plt.axhline(sp, linestyle="--", label="Setpoint")
plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.title("Perbandingan P, PI, dan PID pada plant orde-1")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

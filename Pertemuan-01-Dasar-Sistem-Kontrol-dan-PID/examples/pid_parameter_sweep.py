from pathlib import Path
import matplotlib.pyplot as plt
import control_basics as cb

CASES = {
    'P rendah': (0.6, 0.0, 0.0),
    'P tinggi': (4.0, 0.0, 0.0),
    'PI': (2.0, 0.35, 0.0),
    'PID': (2.0, 0.35, 0.20),
}


def run_case(kp, ki, kd):
    old = cb.KP, cb.KI, cb.KD
    cb.KP, cb.KI, cb.KD = kp, ki, kd
    t, y, u = cb.simulate_pid()
    cb.KP, cb.KI, cb.KD = old
    return t, y, u


def main():
    out = Path(__file__).resolve().parent / 'output'
    out.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    for label, gains in CASES.items():
        t, y, _ = run_case(*gains)
        ax.plot(t, y, label=label)
        print(f'{label:10s} final PV={y[-1]:.3f}, error={cb.SP-y[-1]:.3f}')
    ax.axhline(cb.SP, linestyle='--', label='Setpoint')
    ax.set_xlabel('Time (s)'); ax.set_ylabel('PV')
    ax.set_title('Perbandingan P, PI, dan PID')
    ax.grid(True); ax.legend(); fig.tight_layout()
    fig.savefig(out / 'pid_parameter_sweep.png', dpi=160)
    print(f'Saved {out / "pid_parameter_sweep.png"}')


if __name__ == '__main__':
    main()

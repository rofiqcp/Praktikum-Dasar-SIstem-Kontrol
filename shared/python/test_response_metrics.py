from response_metrics import step_metrics
import numpy as np

t = np.linspace(0, 20, 201)
y = 10.0 * (1.0 - np.exp(-t / 3.0))
m = step_metrics(t, y, 10.0)

assert 1.5 < m["delay_time_s"] < 2.5, m
assert 5.0 < m["rise_time_s"] < 8.0, m
assert m["maximum_overshoot_pct"] < 0.1, m
assert abs(m["steady_state_error"]) < 0.2, m
print("response_metrics: PASS")

#!/usr/bin/env python3
"""P10 offline quadrature lookup-table demonstration."""
QDEC = [
    0, -1,  1,  0,
    1,  0,  0, -1,
   -1,  0,  0,  1,
    0,  1, -1,  0,
]

def delta(prev_state: int, state: int) -> int:
    return QDEC[(prev_state << 2) | state]

def run_sequence(name, states):
    total = 0
    print(f"\n{name}: {states}")
    for a, b in zip(states, states[1:]):
        d = delta(a, b)
        total += d
        print(f"  {a:02b} -> {b:02b}: {d:+d}, total={total:+d}")
    return total

if __name__ == "__main__":
    seq_a = [0b00, 0b01, 0b11, 0b10, 0b00]
    seq_b = list(reversed(seq_a))
    a = run_sequence("Sequence A", seq_a)
    b = run_sequence("Sequence B", seq_b)
    print(f"\nOne cycle totals: A={a:+d}, B={b:+d}")
    assert a == -b and abs(a) == 4
    print("PASS: opposite quadrature sequences produce opposite signed counts.")

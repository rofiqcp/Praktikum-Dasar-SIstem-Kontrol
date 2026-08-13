# Worksheet Analisis P12 — PID Posisi

Worksheet ini melengkapi `Jobsheet.md` dan `Project.md`. Fokusnya adalah audit data dan reproducibility.

## 1. Metadata dataset
Catat untuk setiap file:

| Parameter | Nilai |
|---|---:|
| nama file | |
| CPR | |
| reference zero | |
| sample interval nominal | |
| target | |
| Kp | |
| Ki | |
| Kd | |
| output limit | |
| jumlah sampel | |
| kondisi dataset | |

## 2. Konsep
Jawab:
1. Apa beda position dan speed feedback?
2. Bagaimana count/CPR menjadi degree?
3. Apa beda zero software dan homing?
4. Apa beda wrapped dan unwrapped coordinate?
5. Mengapa saturation harus ditampilkan saat membahas tuning?
6. Apa tujuan anti-windup?

## 3. P/PD/PID comparison
| Mode | Rise | Overshoot | Settling | Final error | Max output |
|---|---:|---:|---:|---:|---:|
| P | | | | | |
| PD | | | | | |
| PID | | | | | |

Jelaskan apakah D menambah damping dan apakah I benar-benar diperlukan untuk residual error.

## 4. Positive/negative comparison
| Target | Final position | Final error | Overshoot | Settling |
|---:|---:|---:|---:|---:|
| positive | | | | |
| negative | | | | |

Bahas sign consistency dan asimetri response.

## 5. Repeatability
Bandingkan minimal dua dataset dengan target sama. Laporkan mean/range final position, mean absolute final error, dan variasi settling time. Diskusikan backlash, zero reference, quantization, atau missed count bila relevan.

## 6. Source audit
Identifikasi bagian source yang menangani:
- encoder count;
- count-to-degree;
- ZERO/reference;
- SP/error;
- P/I/D;
- conditional anti-windup;
- saturation;
- telemetry;
- stop/timeout state.

## 7. Grafik wajib
1. SP vs position;
2. error;
3. P/I/D;
4. control output.

Gunakan `examples/analyze_position_pid_log.m` untuk struktur analisis dasar.

## 8. Wrapped vs unwrapped
Contoh:

```text
unwrapped: 350, 355, 360, 365, 370
wrapped:   350, 355,   0,   5,  10
```

Jelaskan mengapa mencampur keduanya dapat membuat error atau derivative tampak meloncat.

## 9. Troubleshooting berbasis data
| Gejala | Audit |
|---|---|
| posisi salah skala | CPR/reference shaft |
| sign tidak konsisten | count, degree, SP, error |
| drift | encoder/reference zero |
| overshoot besar | P/I/D dan saturation |
| residual error | friction/dead-zone/integral |
| loncat 0/360 | coordinate wrapping |
| data terputus | timestamp/status timeout |

## 10. Kesimpulan wajib
Tuliskan coordinate/reference, tuning yang dipilih, metrics utama, perbedaan positive/negative, repeatability, keterbatasan data, dan satu usulan perbaikan.
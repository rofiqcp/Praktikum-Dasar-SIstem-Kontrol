# Tugas Video Pertemuan 10 — Encoder, RPM, dan Posisi

## Tujuan
Membuktikan mahasiswa memahami feedback encoder dari state A/B sampai data position/RPM yang siap dipakai pada PID.

## Struktur wajib

### 1. Pembukaan
Tampilkan nama/NIM, tujuan P10, dan diagram:

```text
Encoder A/B -> quadrature decoder -> count -> position
                                  -> delta count/dt -> RPM -> filter
```

### 2. Teori quadrature
Jelaskan:
- state 00/01/11/10;
- perubahan arah;
- x4 decoding;
- lookup table `-1/0/+1`.

Jalankan:

```bash
python examples/quadrature_state_test.py
```

### 3. CPR
Jelaskan beda PPR dan CPR serta referensi shaft. Tampilkan tabel beberapa trial dan jalankan:

```matlab
run('examples/cpr_calibration.m')
```

Sebutkan CPR final dan alasan pemilihannya.

### 4. Posisi
Jelaskan:

```text
position_deg = count/CPR*360
```

Bedakan unwrapped position dan wrapped 0–360°.

### 5. RPM
Jelaskan:

```text
rpm = delta_count/CPR * 60/dt
```

Berikan satu contoh hitung manual.

### 6. Sample-time quantization
Hitung `DeltaRPM = 60/(CPR*dt)` untuk minimal dua interval dan jelaskan tradeoff.

### 7. Firmware
Buka `arduino_encoder_stream.ino` dan tunjukkan:
- pin D2/D3;
- ISR;
- QDEC;
- atomic count snapshot;
- degree;
- raw RPM;
- moving average;
- LPF;
- serial telemetry.

### 8. MATLAB monitor
Jalankan `matlab_monitor_encoder.m`. Tampilkan data dengan tanda positif, diam, dan negatif.

### 9. Filter comparison
Tampilkan raw vs MA vs LPF. Jelaskan smoothing dan delay, bukan hanya mengatakan satu grafik lebih bagus.

### 10. Analisis log
Jalankan:

```matlab
run('examples/analyze_encoder_log.m')
```

Tampilkan sample interval dan ringkasan min/max RPM.

### 11. Kesimpulan gate P11
Nyatakan apakah feedback sudah lulus:
- sign;
- CPR;
- scale position;
- positive/negative RPM;
- logging.

Jika belum lulus, jelaskan apa yang harus diperbaiki sebelum P11.

## File pendamping
- source firmware;
- MATLAB scripts;
- tabel CPR;
- CSV log;
- grafik raw/MA/LPF;
- screenshot serial;
- video link.

## Rubrik
| Aspek | Bobot |
|---|---:|
| quadrature dan arah | 20% |
| CPR dan position scaling | 20% |
| RPM dan sample-time analysis | 20% |
| filtering | 15% |
| bukti program/data | 15% |
| kesimpulan kesiapan P11 | 10% |

## Kesalahan yang mengurangi nilai
- menyamakan PPR dan CPR tanpa verifikasi;
- tidak menunjukkan data arah negatif;
- tidak menjelaskan sample interval;
- hanya menampilkan RPM LPF tanpa raw;
- tidak menyimpan CSV;
- mengubah tanda di satu tempat tanpa menjelaskan konvensi end-to-end.
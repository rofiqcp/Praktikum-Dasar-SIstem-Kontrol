# Jobsheet Pertemuan 9 — MATLAB–Arduino PID Suhu

## Tujuan
Memvalidasi sensor temperatur, menjalankan PID diskrit host-side, merekam seluruh term kontrol, dan membandingkan P/PI/PID dengan data kuantitatif pada trainer laboratorium yang telah disiapkan.

## Prasyarat
- P1–P7 selesai;
- MATLAB Support Package for Arduino tersedia;
- trainer dan sensor telah diverifikasi instruktur;
- tahap awal menggunakan simulasi/dummy output.

## File
```text
examples/temperature_sensor_calibration.m
examples/temp_pid_offline_simulation.m
examples/matlab_temp_pid_host.m
examples/analyze_temp_pid_log.m
examples/build_temp_pid_simulink.m
```

## A. Pre-test
Jawab:
1. tuliskan `e=SP-PV`;
2. jelaskan fungsi P, I, D;
3. jelaskan saturasi 0–100%;
4. jelaskan integral windup;
5. jelaskan derivative-on-measurement;
6. bedakan sample time dengan time-proportional window.

## B. Audit data dan I/O
Catat board, port, pin sensor, pin command, tipe sensor, satuan, range, sumber temperatur referensi, dan batas operasi trainer yang diberikan instruktur.

## C. Kalibrasi sensor
Kumpulkan minimal tiga pasangan `voltage_V` dan `reference_C`, lalu jalankan:

```matlab
run('examples/temperature_sensor_calibration.m')
```

Catat slope, intercept, residual, dan range kalibrasi. Jangan lanjut bila scaling tidak masuk akal.

## D. Simulasi offline
Jalankan:

```matlab
run('examples/temp_pid_offline_simulation.m')
```

Uji empat konfigurasi:
- P;
- PI;
- PID;
- satu tuning lebih agresif.

Buat tabel Kp/Ki/Kd, rise time, overshoot, settling time, SSE, dan maximum control output.

## E. Verifikasi dummy output
Gunakan indikator/dummy output trainer. Verifikasi secara visual bahwa 0%, sekitar 50%, dan 100% menghasilkan proporsi waktu aktif yang sesuai. Pastikan penghentian script mengembalikan command ke kondisi aman.

## F. Konfigurasi script
Buka `examples/matlab_temp_pid_host.m` dan dokumentasikan:

```text
PORT, SP, KP, KI, KD, TS, WINDOW_S, MAX_TEMP_C, RUN_TIME_S
```

Fungsi konversi sensor harus sesuai hasil kalibrasi; `voltage*100` hanya baseline sensor tertentu.

## G. Run P
Gunakan `Ki=0` dan `Kd=0`. Simpan CSV, PNG, metrics, kondisi awal, sample time nominal, dan parameter controller.

## H. Run PI
Pertahankan kondisi lain semirip mungkin dan tambahkan Ki kecil. Analisis perubahan SSE, overshoot, dan integral.

## I. Run PID
Tambahkan Kd hanya bila dibutuhkan. Analisis apakah term D memperbaiki damping atau hanya memperbesar noise.

## J. Analisis CSV
Set path data di `examples/analyze_temp_pid_log.m`, kemudian jalankan:

```matlab
run('examples/analyze_temp_pid_log.m')
```

Grafik minimal:
1. SP dan PV;
2. error;
3. P/I/D;
4. PID output %;
5. status command.

## K. Tabel perbandingan
| Parameter | P | PI | PID |
|---|---:|---:|---:|
| temperatur awal | | | |
| SP | | | |
| Kp | | | |
| Ki | | | |
| Kd | | | |
| Ts | | | |
| window | | | |
| rise time | | | |
| overshoot | | | |
| settling | | | |
| SSE | | | |

Jika kondisi awal berbeda jauh, nyatakan keterbatasan perbandingan.

## L. Bandingkan dengan P5/P6
Bandingkan satu run Autonics yang paling comparable terhadap P9 dari sisi response metrics, kualitas logging, transparansi algoritma, dan timing controller.

## M. Source review
Praktikan harus dapat menunjukkan baris yang:
- membaca sensor;
- menghitung error;
- menghitung P/I/D;
- melakukan anti-windup;
- membatasi output;
- membentuk time-proportional command;
- melakukan cleanup bila program berhenti.

## Pertanyaan analisis
1. Mengapa output heating hanya 0–100%?
2. Mengapa overshoot pada plant termal dapat turun lambat?
3. Mengapa host-side control cukup untuk praktikum termal namun bukan hard real-time?
4. Mengapa Ki dapat memperkecil SSE tetapi menambah overshoot?
5. Kapan Kd tidak memberi manfaat?
6. Mengapa kalibrasi harus dilakukan sebelum tuning?
7. Apa beda `TS` nominal dan interval aktual?
8. Mengapa raw CSV harus dipertahankan?
9. Apa keuntungan Autonics dibanding MATLAB–Arduino dan sebaliknya?
10. Bukti apa yang menunjukkan hasil dapat direproduksi?

## Deliverable
```text
NIM_Nama_P09/
  source/
  raw/
  results/
  screenshots/
  laporan.pdf
```

Minimal berisi data kalibrasi, run P/PI/PID, grafik, metrics, tabel perbandingan, source yang digunakan, serta kesimpulan.

## Expected result
Mahasiswa mampu menjelaskan seluruh rantai `sensor -> PV -> error -> PID -> saturated output`, menunjukkan tiga run terdokumentasi, dan memilih tuning berdasarkan data.
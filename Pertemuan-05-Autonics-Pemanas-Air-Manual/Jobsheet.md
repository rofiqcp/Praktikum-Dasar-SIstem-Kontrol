# Pertemuan 05 — Jobsheet — Stopwatch, Excel, ON/OFF dan PID


## Bagian A — baseline
1. Pastikan output OFF.
2. Catat suhu awal dan volume air.
3. Set SV sesuai instruksi lab (contoh 50 °C bila aman untuk plant).
4. Mulai stopwatch bersamaan dengan RUN.
5. Catat PV tiap interval tetap ke `templates/template_pengamatan.csv` atau Excel.

## Bagian B — ON/OFF
Lakukan minimal 3 variasi hysteresis yang aman. Untuk setiap run, biarkan kondisi awal dibuat sebanding atau catat perbedaannya.

## Bagian C — PID/time proportional
Mulai dari parameter dosen/auto-tuning yang aman. Lakukan variasi terkontrol; jangan mengubah banyak parameter sekaligus tanpa tujuan.

## Analisis
- buka CSV di Excel, buat line chart;
- jalankan `examples/analyze_manual_response.m` atau `.py`;
- bandingkan overshoot, settling, error akhir;
- jelaskan trade-off.

## Kolom minimum data
`time_s, temperature_C, setpoint_C, mode, Kp_or_PB, Ki_or_I, Kd_or_D, hysteresis_C, note`.


## Template Excel
Gunakan `templates/template_pengamatan_pemanas_air.xlsx` untuk pencatatan stopwatch. Kolom error dan grafik sudah disiapkan; isi PV/suhu hasil pengamatan secara manual.

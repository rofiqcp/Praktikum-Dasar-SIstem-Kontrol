# Pertemuan 05 — Autonics TK4S/T4RN + Pemanas Air — Pengambilan Data Manual


## Capaian
Mengoperasikan controller temperatur, membedakan ON/OFF hysteresis dan PID/time-proportional, serta mengambil data temperatur manual menggunakan stopwatch untuk dianalisis di Excel/MATLAB/Python.

## Konsep Autonics
- PV = process value (suhu terukur).
- SV = set value/setpoint.
- ON/OFF control membandingkan PV dan SV dengan hysteresis agar output tidak chatter.
- PID menghitung manipulated value (MV). Untuk output switching/SSR, MV diterjemahkan menjadi rasio waktu ON/OFF pada window tertentu (time proportional).

## Hysteresis
Lebar terlalu kecil menjaga suhu dekat SV tetapi meningkatkan switching dan dapat hunting akibat noise/delay. Lebar lebih besar mengurangi switching namun deviasi suhu lebih lebar.

## Prosedur pengamatan manual
Catat waktu dari stopwatch dan PV pada interval tetap (contoh 5 s atau 10 s). Jangan mengubah interval di tengah run. Catat juga SV, mode, hysteresis atau P/I/D, kondisi awal, volume air, daya heater, dan gangguan.

## Data yang dianalisis
- grafik temperature vs time;
- overshoot;
- rise/settling time;
- steady-state error;
- perbandingan parameter antar run.

## Keselamatan
Gunakan plant heater yang disetujui lab. Jangan menyentuh koneksi power/SSR saat energize. Output kontrol harus OFF sebelum wiring.


## File pencatatan
Repository menyediakan CSV sederhana dan workbook Excel `templates/template_pengamatan_pemanas_air.xlsx` yang siap diisi saat percobaan.

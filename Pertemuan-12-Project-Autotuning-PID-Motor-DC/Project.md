# Project Pertemuan 12 — Autotuning PID Motor DC MATLAB/Simulink

## Scope
Lakukan autotuning untuk dua mode plant:
- posisi: karakter **stable**;
- kecepatan: karakter **integrating** sesuai workflow praktikum.

Masing-masing diuji dengan tiga excitation:
1. Sinestream,
2. Superposition,
3. PRBS.

## Deliverable
- model/diagram block;
- prosedur injection dan operating point;
- grafik input/output;
- Kp, Ki, Kd hasil setiap metode;
- tabel 6 konfigurasi (3 position + 3 speed);
- validasi closed-loop untuk setiap hasil tuning;
- analisis konfigurasi terbaik.

## Prosedur Minimum
1. Stabilkan plant pada setpoint aman.
2. Aktifkan autotuning/excitation.
3. Tunggu durasi eksperimen yang cukup (materi contoh sekitar >200 s).
4. Matikan excitation dan ambil model/gain hasil.
5. Ulangi untuk Sinestream, Superposition, PRBS.
6. Jangan mengubah lebih dari satu faktor tanpa mencatatnya.

## Kriteria
Tuning terbaik tidak hanya nilai error terkecil, tetapi juga mempertimbangkan overshoot, settling time, effort PWM, noise dan stabilitas dua arah.

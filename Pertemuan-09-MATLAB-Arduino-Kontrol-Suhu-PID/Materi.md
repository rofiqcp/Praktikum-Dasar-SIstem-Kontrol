# Pertemuan 09 — MATLAB–Arduino Kontrol Suhu PID — Pemanas Air + SSR


## Tujuan
Menggantikan controller Autonics P5/P6 dengan Arduino Mega sebagai controller/DAQ, sementara MATLAB dipakai untuk monitoring/tuning dan analisis.

## Plant
Sensor temperatur low-voltage → A0 (atau interface lain yang sudah dikalibrasi), controller PID → duty 0…100%, SSR D8 → heater.

## Time proportional SSR
Jangan memakai PWM ratusan Hz ke SSR mekanik/SSR tertentu tanpa melihat karakter output. Praktikum memakai **window control**: misalnya window 2 s; bila PID 25%, SSR ON 0.5 s lalu OFF 1.5 s. Sesuaikan window dengan hardware SSR dan plant.

## PID diskrit heater
- error `SP-PV`;
- P, I, D;
- command dibatasi 0–100%;
- anti-windup;
- sensor validity dan over-temperature stop;
- output SSR OFF saat komunikasi/program berhenti.

## Perbandingan dengan P5/P6
Gunakan setpoint dan kondisi eksperimen yang sebanding. Bandingkan Autonics vs Arduino dari rise/overshoot/settling/steady-state error.

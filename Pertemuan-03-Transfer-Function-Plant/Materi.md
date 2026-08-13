# Pertemuan 03 — MATLAB Transfer Function — Pemanas Air, Motor DC Speed, Motor DC Position


## Capaian
Mahasiswa dapat menurunkan/menggunakan transfer function, pole-zero, step response, dan membedakan model temperatur, speed, serta position.

## 1. Pemanas air
Model awal praktikum: first-order plus dead time (FOPDT):

`G_T(s)=K/(tau*s+1) * exp(-L*s)`

- `K`: process gain;
- `tau`: time constant;
- `L`: dead time.

Untuk simulasi rasional, delay dapat didekati Padé. Nilai contoh di source hanya untuk latihan; plant nyata harus diidentifikasi dari P5/P6/P9.

## 2. Motor DC — kecepatan
Dengan resistansi `R`, induktansi `L`, inertia `J`, damping `b`, motor constant `K`:

`G_w(s)=K / ((J*s+b)(L*s+R)+K^2)`

Output adalah rad/s terhadap tegangan input.

## 3. Motor DC — posisi
Karena `theta_dot = omega`, maka:

`G_theta(s)=G_w(s)/s`.

Tambahan integrator membuat plant posisi berbeda karakter dari speed. Karena itu gain PID speed tidak otomatis cocok untuk position.

## 4. Analisis MATLAB
Gunakan `tf`, `step`, `pole`, `zero`, `dcgain`, `stepinfo`, `feedback`, `pade`.

## 5. Identifikasi sederhana water heater
Dari step open-loop yang stabil, estimasi kasar process gain: `K=(Delta T)/(Delta u)`. Time constant dapat diperkirakan dari waktu mencapai sekitar 63.2% perubahan keluaran setelah dead time.

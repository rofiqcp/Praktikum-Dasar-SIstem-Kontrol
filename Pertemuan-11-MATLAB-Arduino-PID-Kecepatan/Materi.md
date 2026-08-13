# Pertemuan 11 — MATLAB–Arduino PID Kecepatan Motor DC

## 1. Loop speed
`SP_rpm → error → PID → signed PWM → L293D → motor → encoder → RPM`

## 2. Signed PWM
Output PID dibatasi `-MAX_PWM..+MAX_PWM`.
- positif: CW PWM D5, D6=0;
- negatif: CCW PWM D6, D5=0;
- nol: keduanya 0.

## 3. Feedback
Firmware menghitung RPM dari delta encoder, moving average, lalu LPF. Feedback default PID menggunakan `rpm_lpf`.

## 4. Anti-windup
Integral hanya di-update bila output tidak saturasi atau error mendorong output kembali dari saturasi.

## 5. Reverse direction
Pengujian wajib positif dan negatif. Sensor yang bisa membaca RPM negatif belum membuktikan controller bisa reverse; jalur signed PID dan driver harus diverifikasi.

## 6. MATLAB
Arduino menjalankan loop deterministic. MATLAB mengirim setpoint/gain dan merekam telemetry. Ini membuat P11 stabil untuk hardware sambil tetap memakai MATLAB untuk eksperimen.

## 7. Tuning
- motor tanpa beban berat;
- MAX_PWM rendah dahulu;
- Kp;
- Ki;
- Kd bila diperlukan;
- step +RPM;
- step -RPM;
- STOP.

## 8. Simulink
Builder membuat model konseptual `motor_speed_pid.slx`.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **PID kecepatan**. Program yang harus dibuka dan dipahami:
- `arduino_speed_pid/arduino_speed_pid.ino`
- `matlab_speed_pid_experiment.m`
- `build_motor_speed_pid_simulink.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Motor mengikuti SP positif/negatif dan grafik error/P/I/D/PWM tersedia.

## Validasi dan troubleshooting
Jika positif jalan tetapi negatif tidak, periksa mapping signed command, PWM CW/CCW, arah encoder dan limit output secara end-to-end.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

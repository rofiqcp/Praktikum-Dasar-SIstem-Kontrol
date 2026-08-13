# Jobsheet Pertemuan 11

> Analisis kuantitatif, tabel P/PI/PID, audit saturation, filter, dan perbandingan dua arah dijelaskan lebih lengkap di `ANALISIS_DATA.md`.

## 1. Verifikasi P10
RPM + dan - harus benar.

## 2. Upload
`arduino_speed_pid.ino`.

Set `COUNTS_PER_REV`.

## 3. MATLAB
Run `matlab_speed_pid_experiment.m`.

Script mengirim:
`RUN, SP, KP, KI, KD, MAXPWM`.

## 4. Eksperimen
- +100 RPM;
- 0;
- -100 RPM;
- P;
- PI;
- PID.

## 5. Wajib
Uji STOP saat motor berputar. Kedua PWM harus nol.

## Analisis
Grafik SP, RPM, error, P/I/D, PID PWM. Hitung response metrics untuk step positif dan negatif secara terpisah. Lengkapi tabel dan pertanyaan pada `ANALISIS_DATA.md`.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
Motor mengikuti SP positif/negatif dan grafik error/P/I/D/PWM tersedia.

## Troubleshooting wajib dipahami
Jika positif jalan tetapi negatif tidak, periksa mapping signed command, PWM CW/CCW, arah encoder dan limit output secara end-to-end.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

# Jobsheet Pertemuan 4

## Percobaan 1 — P
Kp = 0.5, 1, 2, 5; Ki=Kd=0.

## Percobaan 2 — PI
Pilih Kp terbaik, variasikan Ki.

## Percobaan 3 — PID
Tambahkan Kd; bandingkan overshoot/noise.

## Percobaan 4 — Blok manual
Generate `.slx`, buka subsystem PID manual, telusuri jalur P/I/D.

## Percobaan 5 — Saturasi
Jalankan `pid_discrete_antiwindup.m`; bandingkan integral dengan dan tanpa conditional integration.

## Tabel wajib
Kp, Ki, Kd, rise time, overshoot, settling time, error akhir.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
Kurva P/PI/PID dapat dibandingkan dan blok P/I/D manual terbentuk di Simulink.

## Troubleshooting wajib dipahami
Jika simulasi divergen, kecilkan gain; cek tanda feedback dan saturasi sebelum menyimpulkan tuning.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

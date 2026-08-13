# Contoh Prompt AI P15

Gunakan AI sebagai reviewer/partner implementasi. Contoh:

> Audit firmware Arduino Mega 2560 kontrol motor DC ini. Hardware saya: L293D PWM CW D5, PWM CCW D6, encoder quadrature A D2 dan B D3. Saya butuh dua mode independen SPEED dan POSITION, output signed -255..255, anti-windup, derivative-on-measurement, speed raw + moving average + LPF, sampling 10–300 ms, CPR configurable, heartbeat host, stall fault, STOP yang selalu mematikan kedua PWM, dan serial CSV stabil. Jangan ubah pin tanpa menjelaskan alasannya. Tunjukkan risiko arah terbalik dan overflow/concurrency pada encoder.

Untuk GUI:

> Buat/review GUI PyQt5 1900x960: panel setting kiri, dua grafik kanan, port refresh/connect, Start/Stop, mode Speed/Position, zero otomatis saat masuk Position, setpoint -600..600 step 0.1, Kp/Ki/Kd 0..3 step .01, alpha 0..1 step .01, MA, sample 10–300 ms, CPR, MAXPWM, checkbox setiap kurva, CSV/XLSX/JPG, response metrics, mode --demo, dan graceful serial disconnect. Pastikan index telemetry persis sesuai protokol 15 kolom.

Setelah AI memberi patch, build dan tes ulang. Simpan prompt + perubahan yang Anda terima/tolak sebagai bagian laporan.

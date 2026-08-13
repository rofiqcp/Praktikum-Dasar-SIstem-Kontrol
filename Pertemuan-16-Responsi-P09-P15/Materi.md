# Pertemuan 16 — Responsi P9–P15 dan Integrasi Final

Pertemuan terakhir memverifikasi bahwa mahasiswa memahami **alur sistem**, bukan hanya menghafal source code. Scope responsi meliputi P9 PID suhu MATLAB-Arduino, P10 encoder, P11 PID kecepatan, P12 PID posisi, P13 PlatformIO/AI, P14 kontrol suhu embedded+GUI, dan P15 kontrol motor embedded+GUI.

## Kompetensi yang harus dapat dijelaskan
1. Perbedaan open-loop dan closed-loop pada pemanas air serta motor.
2. Peran sampling time pada PID diskrit.
3. Mengapa SSR pemanas menggunakan time-proportional, bukan PWM Arduino langsung ke mains.
4. Konversi ADC ke suhu dan kebutuhan kalibrasi sensor.
5. Encoder quadrature, signed count, CPR, posisi dan RPM.
6. Perbedaan PID speed dan position.
7. P, I, D, saturasi, anti-windup dan derivative noise.
8. Moving average vs LPF.
9. Serial protocol GUI-firmware.
10. Safety state: boot OFF, STOP, fault, heartbeat, stall/over-temperature.
11. Cara membaca grafik dan menentukan rise/settling/overshoot/SSE.
12. Cara memakai AI dengan verifikasi build dan hardware.

## Integrasi final
Trainer dianggap layak digunakan bila:
- jalur logika/USB aman;
- heater output OFF saat boot/disconnect/fault;
- motor output D5/D6 OFF saat boot/disconnect/fault;
- encoder benar dua arah;
- sensor suhu terbaca wajar;
- GUI demo dan GUI hardware dapat dijalankan;
- data dapat disimpan dan dianalisis;
- mahasiswa dapat menjelaskan setiap interlock yang ada.

Gunakan `examples/final_smoke_test.py` sebelum demonstrasi. Script ini bersifat pasif: mengirim STOP, heartbeat/status dan memeriksa format telemetry tanpa sengaja memberi command gerak/panas.

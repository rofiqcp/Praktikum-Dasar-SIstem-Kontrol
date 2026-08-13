# Pertemuan 14 — PlatformIO PID Pemanas Air dengan SSR

## Capaian Pembelajaran
- mengimplementasikan PID temperatur embedded
- mengendalikan SSR secara time-proportional
- menambahkan interlock sensor/overtemperature
- membandingkan controller embedded dan Autonics

## Materi Inti

Firmware temperatur memindahkan konsep Autonics ke Arduino Mega: sensor suhu → PID → output **time-proportional SSR**. Karena SSR/heater tidak dikendalikan seperti PWM motor berfrekuensi tinggi, output PID 0–100% diterjemahkan ke duty dalam window waktu misalnya 2 s.

Untuk lab contoh memakai library MAX6675 pada pin SPI. Sensor dapat diganti sesuai PCB. Proteksi software: batas setpoint, sensor fault, over-temperature cutoff, START/STOP, integral clamp dan output 0% saat fault.


## Program yang Wajib Dijalankan
- `examples/mega_pid_heater/platformio.ini`
- `examples/mega_pid_heater/src/main.cpp`
- `examples/serial_logger.py`

## Alur Praktikum
1. Pastikan output SSR terhubung ke LED dummy atau plant aman terlebih dahulu.
2. Build firmware.
3. Verifikasi pembacaan suhu serial.
4. Uji `START/STOP` tanpa heater.
5. Uji output time-proportional.
6. Set setpoint aman dan tuning P lalu PI lalu PID.
7. Simpan log CSV dengan Python `serial_logger.py`.
8. Bandingkan respon Arduino PID dengan Autonics.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.

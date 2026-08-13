# Pertemuan 13 — PlatformIO PID Motor DC + Python GUI

## Capaian Pembelajaran
- membuat firmware PID embedded
- menggunakan encoder interrupt
- membangun serial protocol
- membuat GUI monitoring Python

## Materi Inti

Firmware Arduino Mega 2560 mengimplementasikan PID speed/position dengan pin materi: **D5 CW, D6 CCW, encoder D2/D3** dan saturation -255..255. Speed pipeline menyediakan raw speed, moving average, LPF, dan speed per second. Saat berganti ke mode position, posisi otomatis di-zero-kan. Telemetry mengirim SP, position, raw/MA/LPF speed, feedback, error, P/I/D dan output.

GUI Python/PyQt berkomunikasi serial, mengatur mode, setpoint, Kp/Ki/Kd, alpha dan sampling; menampilkan dua grafik; menyimpan CSV, Excel dan PNG; serta menghitung karakteristik respon sistem.


## Program yang Wajib Dijalankan
- `examples/mega_pid_motor/platformio.ini`
- `examples/mega_pid_motor/src/main.cpp`
- `examples/gui_motor_pid.py`

## Alur Praktikum
1. Install Python 3.10+, VS Code/Cursor/Windsurf dan PlatformIO.
2. Build/upload firmware `mega_pid_motor`.
3. Test serial command manual.
4. Install Python requirements.
5. Jalankan `python gui_motor_pid.py`.
6. Uji connect/disconnect dan mode speed.
7. Uji mode position dan zero position.
8. Simpan data CSV, lalu hitung response metrics.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

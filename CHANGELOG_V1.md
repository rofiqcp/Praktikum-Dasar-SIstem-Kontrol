# Changelog branch v1

## Complete lab-ready pass
- Memperluas seluruh P1–P16 menjadi jalur belajar yang konsisten dengan materi/jobsheet/tugas atau project.
- Mengganti plant temperatur menjadi **pemanas air**.
- Menetapkan trainer Arduino Mega: SSR heater + L293D motor + encoder A/B.
- Menambahkan source generator Simulink P3/P4/P9/P11/P12 dan `build_all_slx.m`.
- Menambahkan MATLAB, Python, Arduino sketch dan PlatformIO runnable examples.
- Menambahkan P5 template pengamatan stopwatch, analisis CSV dan workbook Excel.
- Menambahkan DAQMaster -> MATLAB/Python analysis pada P6.
- Menambahkan MATLAB-Arduino LED/ADC P7.
- Menambahkan responsi/checkpoint P8 tanpa TugasVideo.
- Menambahkan PID suhu P9, encoder P10, PID speed P11, project PID position P12.
- Menambahkan PlatformIO/AI P13.
- Menambahkan firmware + GUI P14 dengan demo mode, heartbeat, fault, over-temperature, CSV/XLSX/JPG dan response metrics.
- Menambahkan firmware + GUI P15 speed/position, raw/MA/LPF, zero encoder, stall/heartbeat fault, CSV/XLSX/JPG dan response metrics.
- Menambahkan P16 passive smoke test dan Node serial logger.
- Menambahkan dokumentasi installation, wiring, safety, testing, serial protocol, troubleshooting, Simulink generation dan repository validator/CI.

## Hardware safety
Mains/heater power side tidak dirancang untuk breadboard. Praktikum awal wajib memakai pemanas DC low-voltage atau trainer mains yang sudah dilindungi enclosure/fuse/RCD dan ditangani personel kompeten.

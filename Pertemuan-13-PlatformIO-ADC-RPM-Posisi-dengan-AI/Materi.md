# Pertemuan 13 — PlatformIO Arduino Mega: ADC, RPM, Posisi, dan Workflow AI

## 1. Tujuan
Berpindah dari workflow MATLAB/Arduino ke firmware C++ yang dibangun dengan VS Code + PlatformIO. Mahasiswa harus memahami source yang dihasilkan AI, bukan hanya copy-paste.

## 2. PlatformIO
Project minimal:
```text
platformio.ini
src/main.cpp
```

Target:
```ini
platform = atmelavr
board = megaatmega2560
framework = arduino
```

## 3. I/O P13
- A1: ADC potensiometer;
- D2/D3: encoder;
- serial: 115200.

Firmware menghitung ADC raw, voltage, encoder count, position_deg, rpm_raw, rpm_ma, rpm_lpf.

## 4. Interrupt encoder
ISR harus singkat, tidak `Serial.print`, tidak `delay`, dan hanya update state/count. Data `long` dibaca main loop dalam critical section.

## 5. Timing
Gunakan `millis()` dan non-blocking scheduling. Hindari `delay()` di loop telemetry.

## 6. AI coding workflow
AI boleh dipakai untuk menjelaskan code, membuat fungsi, review bug, membuat test, dan refactor. Praktikan wajib menulis requirement, pin map, review output, compile, test fitur bertahap, simpan prompt, dan memahami setiap perubahan.

## 7. Debug checklist
Jika RPM salah: cek CPR, arah A/B, bounce/noise, Ts, integer/float division. Jika position lompat: cek wiring, pull-up, ISR state table, noise.

## Program wajib
`examples/mega_io_monitor`.

## Hasil yang diharapkan
`pio run` sukses dan serial memuat ADC, voltage, count, degree, RPM raw/MA/LPF.

## Validasi dan troubleshooting
AI output wajib di-compile. ISR harus singkat; akses count 32-bit harus atomik pada AVR 8-bit.

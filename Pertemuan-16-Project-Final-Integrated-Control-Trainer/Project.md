# Project Pertemuan 16 — Final Integrated Control Trainer

## Goal
Satu hardware Arduino Mega 2560 dapat menjalankan **dua mode plant** dengan software yang terstruktur:
1. `HEATER`: PID temperatur + SSR time-proportional.
2. `MOTOR_SPEED` / `MOTOR_POSITION`: PID motor DC encoder + L293D.

Host dapat memakai Python GUI atau Node.js DAQ. Mahasiswa wajib menunjukkan data dan analisis respon, bukan hanya hardware menyala.

## Requirement Firmware
- state machine mode;
- START/STOP global;
- command serial konsisten;
- sensor/encoder validation;
- saturation dan anti-windup;
- zero position command;
- telemetry timestamp, SP, PV, output, P, I, D, mode, fault;
- fail-safe output OFF pada fault/STOP.

## Acceptance Test
### Heater
- PV terbaca;
- SSR dummy test lulus sebelum heater;
- tracking setpoint;
- over-temperature/fault mematikan output.

### Motor
- encoder dua arah benar;
- speed positif/negatif benar;
- position zero dan tracking benar;
- output -255..255 dan anti-windup.

### DAQ
- serial connect stabil;
- logging CSV;
- grafik SP/PV/output;
- hitung delay, rise, peak, settling, overshoot, SSE.

## Deliverable
1. PCB final + schematic + BOM;
2. firmware final;
3. GUI/DAQ;
4. dataset minimal 3 eksperimen heater + 3 speed + 3 position;
5. laporan analisis;
6. video demo 12–20 menit;
7. README cara menjalankan sistem dari komputer baru.

## Rubrik
| Aspek | Bobot |
|---|---:|
| Hardware & safety | 20% |
| Firmware control | 25% |
| GUI/DAQ | 15% |
| Eksperimen & response analysis | 25% |
| Dokumentasi & demo | 15% |


## Offline smoke test
Jalankan `python examples/integration_simulator.py` untuk memverifikasi logika PID tiga mode (heater, motor speed, motor position) sebelum integrasi hardware.

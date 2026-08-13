# Pertemuan 14 — PlatformIO Arduino Mega PID Suhu + GUI Python + AI

P14 adalah implementasi lengkap jalur temperature: firmware embedded + GUI commissioning + logging + metrik.

## Arsitektur
`Sensor A0 -> PID MCU -> 0..100% -> time window -> D8 SSR`, dengan GUI Python untuk telemetry/commands.

## Firmware
Fitur: output OFF saat boot, setpoint/gain serial, PID anti-windup, derivative on measurement, SSR time-proportional, over-temperature, invalid sensor fault, heartbeat timeout, explicit RUN, fault clear, telemetry CSV.

## GUI
Fitur: refresh/select port, connect/disconnect, `--demo`, SP/Kp/Ki/Kd/Tmax/window, Start/Stop, dua live graph, status fault, CSV/XLSX/JPG, response metrics, heartbeat.

## Sensor
Baseline LM35 A0. Jika sensor lain, ubah `readTemperatureC()` dan lakukan kalibrasi sebelum PID.

## Heartbeat
Saat RUN, GUI mengirim `PING,1`. Jika host hilang, firmware mematikan heater dan membuat fault timeout.

## Demo mode
```bash
python examples/gui/app.py --demo
```
GUI mensimulasikan plant orde satu sehingga UI/logging dapat diuji tanpa hardware.

## AI
AI boleh membantu refactor/UI, tetapi safety requirement tidak boleh dihapus. Compile dan test dummy load sebelum plant aktual.

## Hasil yang diharapkan
GUI demo/hardware, fault, heartbeat, live plot dan export CSV/XLSX/JPG bekerja.

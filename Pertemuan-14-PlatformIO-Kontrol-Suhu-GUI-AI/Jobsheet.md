# Jobsheet Pertemuan 14

## Tahap 1 — GUI demo
```bash
cd examples/gui
pip install -r requirements.txt
python app.py --demo
```
Start, ubah SP/gain, Save. Pastikan CSV/XLSX/JPG terbentuk.

## Tahap 2 — firmware
```bash
cd ../mega_temp_pid
pio run
pio run -t upload
```

## Tahap 3 — sensor
Heater OFF: cek suhu, bandingkan thermometer, test sensor invalid.

## Tahap 4 — dummy SSR
Test Start/Stop pada LED/dummy SSR.

## Tahap 5 — plant
Setpoint aman. Tune P→PI→PID.

## Tahap 6 — fault
Disconnect GUI saat RUN → OFF setelah timeout; over-temperature → fault; sensor invalid → fault; restart MCU → output OFF.

## Data wajib
SP, PV, error, P, I, D, PID%, SSR, fault.

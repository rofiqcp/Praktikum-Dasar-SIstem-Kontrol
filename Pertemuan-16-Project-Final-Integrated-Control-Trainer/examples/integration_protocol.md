# Serial Protocol Final

## Commands
```text
MODE=HEATER
MODE=MOTOR_SPEED
MODE=MOTOR_POSITION
SP=50
KP=1.2
KI=0.3
KD=0.01
TS=50
ZERO
START
STOP
```

## Telemetry CSV
```text
time_ms,mode,setpoint,pv,output,p,i,d,fault
```

## Fail-safe
- `STOP` -> semua output 0/OFF.
- sensor temperatur invalid -> SSR OFF.
- mode heater -> motor output 0.
- mode motor -> SSR OFF.
- timeout host tidak wajib mematikan sistem bila controller lokal tetap aman, tetapi dapat ditambahkan sebagai enhancement.

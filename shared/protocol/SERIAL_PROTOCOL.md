# Serial Protocol P13–P15

Baud: **115200**, 8N1, ASCII/UTF-8 compatible, line ending `\n`.

## General rules

- Command dari host: `KEY,VALUE`.
- Telemetry dari MCU: CSV satu baris.
- Pesan debug/status diawali `#` agar parser GUI mengabaikannya sebagai telemetry.
- Firmware mengirim `#PROTO,<name>,<version>` saat boot.
- `RUN,0` harus mematikan aktuator segera.
- Nilai tetap di-clamp di firmware walaupun GUI sudah melakukan validasi.
- Saat `HOST,1`, GUI/MATLAB harus mengirim heartbeat `PING,1` secara berkala ketika sistem disupervisi host.

## Common commands

| Command | Arti |
|---|---|
| `RUN,0/1` | stop/start control |
| `SP,<value>` | setpoint |
| `KP,<value>` | Kp |
| `KI,<value>` | Ki |
| `KD,<value>` | Kd |
| `TS,<ms>` | sample time bila firmware mendukung |
| `ZERO,1` | zero encoder/position |
| `PING,1` | host heartbeat |
| `HOST,0/1` | nonaktif/aktifkan kebutuhan heartbeat |
| `STATUS,1` | minta status |
| `CLEAR,1` | clear latched fault bila kondisi aman |

## P14 temperature

Tambahan:
- `TMAX,<C>` over-temperature software limit.
- `WIN,<ms>` time-proportional window.

Telemetry:

```text
ms,temp_C,sp_C,error,P,I,D,pid_pct,ssr,fault
```

## P15 motor

Tambahan:
- `MODE,1` = SPEED.
- `MODE,2` = POSITION.
- `ALPHA,<0..1>`.
- `MA,<1..16>`.
- `CPR,<count/rev>`.
- `MAXPWM,<20..255>`.

Telemetry:

```text
ms,mode,sp,position_deg,rpm_raw,rpm_ma,rpm_lpf,error,P,I,D,pid_pwm,pwm_cw,pwm_ccw,fault
```

Mode:
- `1` SPEED.
- `2` POSITION.

## Fault codes baseline

- `0` OK.
- `1` sensor invalid (temperature firmware).
- `2` over-temperature.
- `3` host/heartbeat timeout.
- `4` stall/motion fault.
- `5` configuration fault/reserved.

Host harus memperlakukan `fault != 0` sebagai kondisi STOP dan tidak mengirim `RUN,1` kembali sebelum penyebab fault diperiksa dan `CLEAR,1` dilakukan secara sadar.

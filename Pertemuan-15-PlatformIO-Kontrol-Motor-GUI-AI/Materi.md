# Pertemuan 15 — PlatformIO Arduino Mega PID Speed & Position + GUI Lengkap + AI


## Tujuan
Mengintegrasikan encoder, filter speed, PID speed/position, anti-windup, protocol serial, GUI Python, logging CSV, JPG, dan metrik respon.

## Firmware
- ISR encoder A/B;
- raw RPM dari delta count/timestamp;
- moving average speed;
- LPF speed `y=alpha*x+(1-alpha)*y_prev`;
- mode `SPEED` atau `POSITION`;
- saat masuk position, user dapat zero encoder secara eksplisit;
- PID output -255…255;
- jika Kp/Ki/Kd = 0, komponen bersangkutan harus 0;
- anti-windup;
- telemetry lengkap.

## GUI
Parameter di kiri; dua grafik di kanan. Wajib connect/disconnect, refresh port, start/stop, mode, SP, Kp/Ki/Kd, alpha LPF, clear, save CSV/JPG. Pengembangan boleh menambah checkboxes trace, legend dinamis, XLSX, response metrics.

## Validasi
Uji speed + dan -, position + dan -, zero, stop, saturation, encoder disconnect/stall behavior, dan command yang berubah saat runtime.

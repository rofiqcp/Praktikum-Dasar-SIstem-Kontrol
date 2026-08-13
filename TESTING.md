# Strategi Pengujian Repository

## 1. Static validation

```bash
python validate_repo.py
```

## 2. Python smoke tests

```bash
python -m compileall .
python shared/python/test_response_metrics.py
```

GUI:

```bash
python Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui/app.py --demo
python Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/gui/app.py --demo
```

## 3. MATLAB

```matlab
build_all_slx
```

Jalankan P2–P4 tanpa hardware terlebih dahulu.

## 4. PlatformIO

Pada masing-masing project:

```bash
pio run
```

Kemudian upload:

```bash
pio run -t upload
```

## 5. Hardware commissioning

Urutan:
1. continuity;
2. power low-voltage;
3. LED;
4. ADC;
5. encoder diputar tangan;
6. motor PWM rendah;
7. closed-loop speed;
8. closed-loop position;
9. sensor temperatur;
10. SSR dummy load;
11. heater plant;
12. fault tests.

## 6. Fault injection

Wajib:
- sensor temperatur unplug;
- encoder tidak bergerak saat motor command;
- serial disconnect;
- restart MCU;
- setpoint ekstrem;
- PID gain ekstrem secara terbatas.

Hasil fault dicatat pada laporan.

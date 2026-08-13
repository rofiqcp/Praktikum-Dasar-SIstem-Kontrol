# Jobsheet Pertemuan 13

## 1. Instalasi
VS Code, PlatformIO, Python, dan minimal satu AI coding assistant.

## 2. Build
```bash
cd examples/mega_io_monitor
pio run
pio run -t upload
pio device monitor -b 115200
```

## 3. ADC
Putar pot A1; raw 0..1023 dan voltage berubah.

## 4. Encoder
Putar tangan CW/CCW. Count signed.

## 5. CPR
Set `COUNTS_PER_REV`/command CPR berdasarkan kalibrasi P10.

## 6. Filter
Kirim `ALPHA,0.25`, `MA,8`, `TS,50`, `ZERO,1`. Bandingkan raw/MA/LPF.

## 7. AI
Minta AI menambahkan satu fitur kecil. Review diff manual dan compile lagi.

## Bukti
Terminal build success, serial telemetry, prompt, kode sebelum/sesudah, dan penjelasan perubahan.

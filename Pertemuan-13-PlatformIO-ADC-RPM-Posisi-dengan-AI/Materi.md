# Pertemuan 13 — Pengenalan PlatformIO + AI — ADC, RPM, Posisi


## Tujuan
Berpindah dari controller yang bergantung PC ke firmware Arduino Mega yang dibangun di VS Code + PlatformIO. AI editor digunakan sebagai asisten, tetapi mahasiswa wajib memahami setiap perubahan dan menguji hardware.

## Tool
- VS Code + PlatformIO extension;
- Python 3.10+ + extension;
- opsional Cursor/Windsurf/Copilot sesuai kebijakan lab;
- Serial Monitor 115200.

## Struktur PlatformIO
`platformio.ini`, `src/main.cpp`. Build: `pio run`; upload: `pio run -t upload`; monitor: `pio device monitor -b 115200`.

## Firmware sensor
- ADC A0;
- encoder interrupt A/B;
- count → angle;
- delta count/time → RPM;
- telemetry CSV via serial.

## Penggunaan AI yang benar
Prompt harus menyebut board, pin, satuan, sample time, format serial, batas nilai, dan output yang diinginkan. Setelah AI menghasilkan kode: compile, baca warning, uji per fungsi, dan dokumentasikan bug/perbaikan. Jangan menerima kode yang mengganti tanda encoder dengan `abs()` hanya agar grafik terlihat positif.

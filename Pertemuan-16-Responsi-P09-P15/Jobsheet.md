# Jobsheet P16 — Responsi dan Final Acceptance Test

## Tahap 1 — Pemeriksaan sebelum daya aktuator
- [ ] PCB tidak short 5 V-GND.
- [ ] D5/D6/D8 LOW saat boot.
- [ ] Arduino terdeteksi serial.
- [ ] Firmware menampilkan `#PROTO`.
- [ ] sensor suhu/ADC masuk akal.
- [ ] encoder berubah saat diputar tangan.

## Tahap 2 — Smoke test serial
```bash
python examples/final_smoke_test.py --port COM5 --seconds 8
# Linux contoh: --port /dev/ttyACM0
```
Script selalu mengirim `RUN,0` sebelum pemeriksaan. Simpan file JSON hasilnya.

## Tahap 3 — Demonstrasi P14
1. GUI `--demo`.
2. GUI hardware terkoneksi.
3. setpoint aman.
4. Start/Stop.
5. tunjukkan SP/PV/error/P/I/D/PID/SSR.
6. simpan CSV/XLSX/JPG.
7. jelaskan over-temperature dan host-timeout.

## Tahap 4 — Demonstrasi P15
1. verifikasi encoder dengan tangan.
2. SPEED + dan -.
3. POSITION + dan - dalam batas mekanik.
4. ZERO encoder.
5. tunjukkan raw/MA/LPF dan anti-windup.
6. simpan CSV/XLSX/JPG.
7. jelaskan host timeout dan stall fault.

## Tahap 5 — Tanya jawab
Penguji memilih minimal 10 soal dari `Project.md`. Mahasiswa harus dapat menunjuk bagian source code yang terkait.

## Tahap 6 — Arsip
Kumpulkan source, screenshot build sukses, foto wiring, data CSV/XLSX, JPG grafik, parameter tuning, hasil metrik, dan jawaban responsi. Gunakan struktur pada `Project.md`.

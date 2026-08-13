# Pertemuan 16 — Project Final — Integrated Control Trainer

## Capaian Pembelajaran
- mengintegrasikan dua plant
- menerapkan fail-safe dan state machine
- membuat eksperimen yang reproducible
- menganalisis respon sistem end-to-end

## Materi Inti

Final project mengintegrasikan seluruh jalur semester: modeling → eksperimen → identifikasi → PID → autotuning → embedded → acquisition. Arsitektur disarankan menggunakan state machine agar output heater dan motor tidak aktif bersamaan secara tidak sengaja.


## Program yang Wajib Dijalankan
- `examples/final_integrated_firmware/platformio.ini`
- `examples/final_integrated_firmware/src/main.cpp`
- `examples/integration_simulator.py`
- `examples/integration_protocol.md`

## Alur Praktikum
1. Audit PCB dan pin map.
2. Integrasikan firmware menjadi mode heater/motor.
3. Tambahkan fail-safe.
4. Integrasikan GUI/Node DAQ.
5. Jalankan acceptance test heater.
6. Jalankan acceptance test motor speed dan position.
7. Simpan dataset dan response metrics.
8. Finalize dokumentasi reproducible.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.


## Offline smoke test
Jalankan `python examples/integration_simulator.py` untuk memverifikasi logika PID tiga mode (heater, motor speed, motor position) sebelum integrasi hardware.

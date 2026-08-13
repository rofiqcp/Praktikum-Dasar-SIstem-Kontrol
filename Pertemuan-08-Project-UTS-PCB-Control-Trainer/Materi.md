# Pertemuan 08 — Project UTS — PCB Arduino Mega Control Trainer

## Capaian Pembelajaran
- merancang PCB control trainer
- mengintegrasikan SSR logic, L293D dan encoder
- melakukan bring-up terstruktur

## Materi Inti

Pertemuan 8 adalah checkpoint UTS. Mahasiswa mengubah blok diagram dari P1 menjadi schematic dan PCB nyata. Desain mengikuti `HARDWARE_PCB_SPEC.md`. Fokus utama adalah testability, keselamatan, pemisahan supply motor/logika, dan konektor yang tidak ambigu.


## Program yang Wajib Dijalankan
- `examples/mega_trainer_bringup/platformio.ini`
- `examples/mega_trainer_bringup/src/main.cpp`

## Alur Praktikum
1. Freeze pin map.
2. Selesaikan schematic dan ERC.
3. Selesaikan PCB dan DRC.
4. Review power/ground dan kapasitor decoupling.
5. Fabrikasi/assembly atau prototype.
6. Jalankan program bring-up.
7. Rekam acceptance test.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.

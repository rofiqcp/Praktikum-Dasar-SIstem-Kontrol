# Pertemuan 12 — Project Autotuning PID Motor DC Simulink

## Capaian Pembelajaran
- menggunakan excitation autotuning
- membedakan stable dan integrating plant
- membandingkan tiga metode autotuning

## Materi Inti

Autotuning melakukan excitation terkontrol untuk mengestimasi dinamika plant, lalu memperoleh parameter PID. Materi praktikum memakai Sinestream, Superposition dan PRBS serta membedakan model posisi (stable) dan kecepatan (integrating).


## Program yang Wajib Dijalankan
- `examples/autotuning_experiment_table.m`

## Alur Praktikum
1. Siapkan model P11 dan Connected I/O.
2. Pastikan PWM, encoder, LPF, delta-time dan PID discrete bekerja.
3. Autotune posisi dengan Sinestream.
4. Autotune speed dengan Sinestream.
5. Ulangi keduanya dengan Superposition.
6. Ulangi keduanya dengan PRBS.
7. Validasi gain hasil tuning.
8. Isi tabel perbandingan.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

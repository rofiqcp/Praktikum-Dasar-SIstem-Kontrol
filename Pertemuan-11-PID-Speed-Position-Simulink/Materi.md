# Pertemuan 11 — PID Motor DC Speed dan Position dengan Simulink

## Capaian Pembelajaran
- membedakan PID speed dan position
- mengelola NaN/filter
- menerapkan anti-windup
- menganalisis komponen P/I/D

## Materi Inti

Dua mode kontrol motor:
- **Speed PID**: setpoint adalah kecepatan; feedback speed per second.
- **Position PID**: setpoint adalah encoder count/angle; feedback posisi.

Function `nan_to_zero` dipakai untuk melindungi pipeline dari nilai NaN. Saturation dan integral anti-windup mencegah integral terus tumbuh saat output sudah mentok. Grafik harus memuat SP, feedback, error, P, I, D dan PID.


## Program yang Wajib Dijalankan
- `examples/nan_to_zero.m`
- `examples/pid_speed_position_demo.m`

## Alur Praktikum
1. Implementasikan `nan_to_zero.m`.
2. Uji kontrol speed positif dan negatif.
3. Plot setpoint, speed, error, P, I, D, PID.
4. Pindah ke mode position dan zero-kan posisi saat pergantian mode.
5. Uji beberapa setpoint posisi positif/negatif.
6. Tunjukkan efek saturation dan anti-windup.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

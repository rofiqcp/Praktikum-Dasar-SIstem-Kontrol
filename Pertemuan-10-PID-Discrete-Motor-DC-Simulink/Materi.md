# Pertemuan 10 — PID Discrete Motor DC Simulink + Blok PID Manual

## Capaian Pembelajaran
- memfilter speed encoder
- menerapkan PID discrete
- menerapkan anti-windup
- membangun PID manual

## Materi Inti

Pertemuan ini menambahkan filter kecepatan dan PID discrete. Rangkaian proses: encoder count → delta count/delta time → speed raw → moving average/LPF → speed per second → error → PID discrete → saturation → PWM.

Mahasiswa wajib mencoba **PID block bawaan** dan **PID block buat sendiri**. Anti-windup digunakan karena PWM dibatasi -255..255.


## Program yang Wajib Dijalankan
- `examples/pid_discrete_reference.m`

## Alur Praktikum
1. Mulai dari model P9.
2. Tambahkan LPF dan perhitungan delta time.
3. Ubah speed menjadi unit per second.
4. Tambahkan Discrete PID Controller.
5. Batasi output -255..255.
6. Bangun PID manual dari P/I/D discrete.
7. Bandingkan respon dan data P,I,D,total.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

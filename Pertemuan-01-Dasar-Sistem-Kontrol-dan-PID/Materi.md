# Pertemuan 01 — Dasar Sistem Kontrol, PID, dan Briefing Project PCB

## Capaian Pembelajaran
- memahami blok sistem kontrol dan feedback
- membedakan open-loop dan closed-loop
- menjelaskan kontribusi P, I dan D
- mengenali parameter respon sistem
- membuat spesifikasi awal PCB control trainer

## Materi Inti

### 1. Sistem kontrol
Sistem kontrol mengatur output plant agar mengikuti nilai yang diinginkan. Blok dasar: **setpoint → error → controller → actuator → plant → sensor/feedback**.

### 2. Open-loop vs closed-loop
Open-loop tidak mengoreksi output berdasarkan feedback. Closed-loop mengukur output, menghitung `e(t)=r(t)-y(t)`, lalu mengoreksi actuator.

### 3. PID
\[
u(t)=K_p e(t)+K_i\int e(t)dt+K_d\frac{de(t)}{dt}
\]
- **P** bereaksi terhadap error sekarang.
- **I** mengakumulasi error dan menekan steady-state error.
- **D** bereaksi terhadap laju perubahan error; membantu damping tetapi sensitif noise.

### 4. Karakteristik respon
Delay time, rise time, peak time, settling time, maximum overshoot dan steady-state error dipakai sepanjang semester.

### 5. Briefing project hardware semester
Mahasiswa merancang PCB/shield Arduino Mega 2560 yang dapat dipakai untuk dua plant: (a) kontrol suhu pemanas air melalui input sensor temperatur dan output logika SSR, (b) kontrol motor DC encoder menggunakan L293D. PCB harus menyediakan test point, proteksi low-voltage, konektor jelas dan pemisahan plant. Lihat `../HARDWARE_PCB_SPEC.md` dari root repository.


## Program yang Wajib Dijalankan
- `examples/control_basics.py`

## Alur Praktikum
1. Jalankan `examples/control_basics.py`.
2. Bandingkan open-loop, P, PI dan PID pada model termal sederhana.
3. Ubah Kp/Ki/Kd dan catat efeknya.
4. Gambar diagram blok untuk pemanas air dan motor DC.
5. Buat draft blok diagram PCB semester: Arduino Mega, sensor suhu, SSR input, L293D, encoder A/B, supply dan konektor.
6. Tentukan pin awal dan buat tabel I/O.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

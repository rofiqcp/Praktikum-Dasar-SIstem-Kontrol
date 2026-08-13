# Pertemuan 5 — Autonics TK4S/T4RN + Pemanas Air, Pengambilan Data Manual

## 1. Tujuan
Mahasiswa mengoperasikan controller temperatur Autonics pada plant pemanas air, membandingkan ON/OFF hysteresis dan PID/time-proportional, serta merekam respon menggunakan stopwatch dan Excel.

## 2. PV, SV, MV
- **PV**: suhu aktual.
- **SV**: setpoint.
- **MV**: manipulated variable/control output.

Pada ON/OFF, MV pada dasarnya 0/100%. Pada PID dengan output relay/SSR, MV diterjemahkan menjadi rasio ON/OFF dalam satu window waktu.

## 3. ON/OFF hysteresis
Controller menghindari chatter dengan dua ambang.

Untuk heating sederhana:
- PV cukup di bawah SV → output ON;
- PV melewati batas atas → OFF.

Hysteresis kecil menjaga PV dekat SV tetapi switching lebih sering. Hysteresis besar switching lebih jarang tetapi ripple temperatur lebih besar.

## 4. PID/time-proportional
PID menghasilkan output persentase. Contoh window 10 s:
- MV 70% → ON 7 s, OFF 3 s;
- MV 20% → ON 2 s, OFF 8 s.

## 5. Eksperimen pemanas air
Gunakan setpoint yang aman untuk trainer, contoh 40–50°C sesuai instruksi laboratorium. Jangan memaksakan setpoint melebihi rating plant.

## 6. Pengambilan data manual
Satu operator melihat stopwatch, satu operator membaca PV. Interval contoh 10 s.

Kolom:
- nomor;
- waktu;
- SV;
- PV;
- error;
- status output/keterangan.

Gunakan `templates/template_pengamatan_pemanas_air.xlsx` atau CSV.

## 7. Uji hysteresis
Lakukan minimal tiga variasi hysteresis. Semua kondisi lain dijaga semirip mungkin:
- volume air;
- suhu awal;
- heater;
- posisi sensor;
- setpoint.

## 8. Uji PID
Tuning dilakukan bertahap:
1. tentukan P;
2. tambah I;
3. tambah D bila diperlukan.

Jangan membandingkan run dengan kondisi awal yang sangat berbeda tanpa mencatatnya.

## 9. Analisis
Gunakan `examples/analyze_manual_data.py`.

Output:
- grafik PV/SP;
- CSV ringkasan;
- delay/rise/peak/settling/overshoot/steady-state error bila data memenuhi definisi.

## 10. Keselamatan
Pemanas air dan listrik harus mengikuti `../SAFETY.md`. Untuk praktikum mahasiswa gunakan plant low-voltage/terisolasi bila memungkinkan.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **Autonics pemanas air manual**. Program yang harus dibuka dan dipahami:
- `templates/template_manual.csv`
- `templates/template_pengamatan_pemanas_air.xlsx`
- `examples/analyze_manual_data.py`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Tabel stopwatch lengkap, grafik PV-SV dan metrik respons tersedia.

## Validasi dan troubleshooting
Jangan mengubah volume air/daya heater di tengah perbandingan. Catat kondisi awal dan interval stopwatch.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

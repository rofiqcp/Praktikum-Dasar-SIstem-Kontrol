# Pertemuan 10 — MATLAB–Arduino Baca RPM dan Posisi Motor DC

## 1. Encoder quadrature
Dua kanal A/B bergeser fase 90°. Urutan transisi menentukan arah.

Repository menggunakan:
- A=D2;
- B=D3;
- signed count;
- lookup table quadrature 4-state.

## 2. Counts per revolution
`COUNTS_PER_REV` harus ditetapkan berdasarkan encoder **setelah** quadrature decoding dan gearbox bila ada.

Jika datasheet menyebut 100 pulse/rev per channel dan decoder memakai x4, CPR bisa 400 count/rev (tergantung definisi vendor).

Verifikasi manual: putar shaft satu revolusi dan lihat delta count.

## 3. Posisi
`position_deg = count / CPR * 360`

## 4. Kecepatan
Dalam window sampling:

`rpm = delta_count/CPR * 60/dt`

Sampling terlalu cepat memberi quantization besar pada RPM rendah.

## 5. Filter
P10 memperkenalkan:
- raw RPM;
- moving average;
- low-pass filter.

P15 mengimplementasikan semuanya embedded.

## 6. Arsitektur
Arduino sketch membaca encoder dan mengirim CSV. MATLAB membaca serial dan membuat plot. Cara ini menghindari konflik timing host dan menunjukkan format data yang dipakai P11/P12.

## 7. Validasi arah
Putar CW lalu CCW dengan tangan. Count/RPM harus berubah tanda. Jika arah mekanik terbalik dari konvensi, tukar A/B atau ubah sign satu kali secara konsisten.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **RPM dan posisi encoder**. Program yang harus dibuka dan dipahami:
- `arduino_encoder_stream/arduino_encoder_stream.ino`
- `matlab_monitor_encoder.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Count dan posisi bertanda benar; raw/MA/LPF RPM berubah sesuai arah dan kecepatan.

## Validasi dan troubleshooting
Jika arah salah, verifikasi kanal A/B dan konvensi mekanik; jangan membalik tanda di satu bagian saja tanpa audit jalur kontrol.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

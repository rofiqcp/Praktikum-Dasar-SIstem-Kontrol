# Pertemuan 6 — Autonics DAQMaster + Analisis MATLAB

## 1. Tujuan
Mengubah pengambilan data P5 yang manual menjadi logging digital melalui DAQMaster, lalu mengolah hasil CSV di MATLAB/Python.

## 2. DAQMaster
DAQMaster digunakan untuk:
- scan/connect perangkat yang didukung;
- monitor PV/SV;
- parameter setting sesuai hak akses/perangkat;
- graph;
- data logging;
- ekspor CSV.

Model/opsi komunikasi Autonics dapat berbeda. Ikuti manual unit aktual untuk address, baud, parity, dan wiring RS485.

## 3. Workflow
1. Pastikan Autonics bekerja standalone.
2. Hubungkan converter RS485 yang benar.
3. Set communication parameter perangkat.
4. Buka DAQMaster.
5. Add/scan device.
6. Pastikan PV/SV masuk akal.
7. Buat graph.
8. Enable logging CSV.
9. RUN eksperimen.
10. STOP.
11. Buka CSV.
12. Import MATLAB.

## 4. Kualitas data
Periksa:
- timestamp monoton;
- tidak ada nilai kosong aneh;
- unit benar;
- sampling interval;
- SV berubah sesuai eksperimen.

## 5. Analisis MATLAB
`examples/analyze_daqmaster.m` berusaha mendeteksi kolom waktu/PV/SV. Bila nama kolom export DAQMaster berbeda, ubah tiga mapping di bagian awal.

## 6. Perbandingan P5 vs P6
Manual:
- mudah tetapi resolusi rendah;
- rawan salah tulis.

DAQ:
- sampling konsisten;
- data lebih banyak;
- perlu konfigurasi komunikasi yang benar.

## 7. Eksperimen
Ulangi tiga hysteresis dan tuning PID dengan logging otomatis. Gunakan kondisi awal yang dikontrol.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **Autonics DAQMaster dan MATLAB**. Program yang harus dibuka dan dipahami:
- `examples/analyze_daqmaster.m`
- `examples/analyze_daqmaster.py`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
CSV DAQMaster dapat dibaca dan menghasilkan grafik/metrik yang bisa dibandingkan dengan P5.

## Validasi dan troubleshooting
Jika kolom tidak terbaca, ekspor CSV sederhana dan identifikasi nama kolom time/PV/SV. Samakan baud/parity/address dengan controller.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

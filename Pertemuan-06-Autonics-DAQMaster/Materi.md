# Pertemuan 06 — Autonics TK4S + Pemanas Air: DAQMaster

## Capaian Pembelajaran
- menghubungkan TK4S ke DAQMaster
- melakukan logging PV/SV secara otomatis
- menjalankan eksperimen hysteresis dan PID
- menganalisis data hasil ekspor

## Materi Inti

DAQMaster digunakan untuk parameter setting, monitoring dan logging controller Autonics melalui komunikasi serial/RS485 sesuai perangkat. Fokus praktikum: membuat koneksi, memilih device TK4, menambahkan unit, connect, memonitor PV/SV/MV dan mengekspor data.

Uji yang sama dengan P5 diulang sehingga hasil manual dan DAQ dapat dibandingkan. Praktikum asli menekankan tiga variasi hysteresis dan pencarian PID bertahap (P terbaik → I → D).


## Program yang Wajib Dijalankan
- `examples/analyze_daqmaster_export.py`

## Alur Praktikum
1. Hubungkan converter komunikasi trainer ke PC sesuai manual lab.
2. Buka DAQMaster dan tambahkan device Autonics TK4.
3. Pilih interface/port yang benar lalu Connect.
4. Tambahkan channel PV, SV dan MV/output bila tersedia.
5. Set logging interval konstan.
6. Uji 3 hysteresis pada SV 50 °C.
7. Uji PID: cari P terbaik, tambah I, lalu D. Simpan minimal 10 dataset/variasi parameter.
8. Export CSV.
9. Jalankan `examples/analyze_daqmaster_export.py export.csv`.
10. Bandingkan ketelitian timestamp manual vs DAQMaster.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.


## Dataset contoh untuk uji program
Sebelum memakai ekspor DAQMaster asli, jalankan analyzer dengan `examples/daq_export_sample.csv` agar alur analisis dapat diverifikasi tanpa hardware.

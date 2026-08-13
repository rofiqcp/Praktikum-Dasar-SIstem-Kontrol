# Pertemuan 15 — Node.js Serial DAQ dan Dashboard Kontrol

## Capaian Pembelajaran
- membaca serial dengan Node.js
- menyimpan data CSV
- membuat endpoint HTTP sederhana
- memahami pemisahan firmware dan DAQ

## Materi Inti

Node.js dipakai sebagai DAQ/dashboard lintas plant. Program serial menerima CSV dari Arduino, menyimpan file log, menghitung statistik sederhana dan menyediakan endpoint HTTP lokal untuk data terbaru. Dengan pola ini mahasiswa melihat pemisahan firmware, protocol, acquisition dan visualization.


## Program yang Wajib Dijalankan
- `examples/node_serial_logger/package.json`
- `examples/node_serial_logger/index.js`

## Alur Praktikum
1. Install Node.js LTS.
2. Masuk ke `examples/node_serial_logger`.
3. Jalankan `npm install`.
4. Jalankan `node index.js COM5 115200` (ubah port).
5. Buka `http://localhost:3000`.
6. Jalankan plant motor atau heater dan lihat data terbaru.
7. Pastikan `data_log.csv` bertambah.
8. Jelaskan perbedaan logging Python, DAQMaster dan Node.js.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

# Pertemuan 06 — Autonics Lanjutan — DAQMaster dan Analisis MATLAB


## Capaian
Melakukan monitoring/logging TK4S/T4RN dengan DAQMaster, menyimpan CSV, mengimpor ke MATLAB, membuat grafik, dan membandingkan variasi hysteresis/PID.

## DAQMaster
DAQMaster digunakan untuk device management, parameter monitoring, project, graph, dan data logging. Data monitoring dapat disimpan sebagai CSV dan dibuka langsung di Excel. Untuk praktikum, CSV menjadi format pertukaran agar analisis MATLAB dapat direproduksi.

## Alur
`TK4S/T4RN -> RS485 converter -> DAQMaster -> CSV -> MATLAB -> metrics/plot`.

## Praktik ON/OFF
Lakukan tiga nilai hysteresis pada SV yang sama dan plant/kondisi awal yang terdokumentasi. Tujuannya bukan sekadar mencari "paling kecil", tetapi membandingkan ripple temperatur, switching, overshoot, dan settling.

## Praktik PID
Ubah parameter secara sistematis. Jika pendekatan praktikum memakai urutan P → I → D, simpan setiap run dengan nama jelas dan jangan menimpa data mentah.

## MATLAB
`analyze_daqmaster.m` menerima CSV generik. Karena nama kolom DAQMaster dapat berbeda menurut konfigurasi, script menyediakan bagian pemetaan kolom yang harus disesuaikan praktikan.

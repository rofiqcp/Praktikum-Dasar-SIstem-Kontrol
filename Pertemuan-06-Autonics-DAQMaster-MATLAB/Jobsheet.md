# Pertemuan 06 — Jobsheet — DAQMaster → CSV → MATLAB


1. Hubungkan controller dan converter RS485 yang disediakan lab.
2. Pastikan address/baud/parity sesuai konfigurasi trainer.
3. Buka DAQMaster, scan/add device, tampilkan PV dan SV.
4. Tambahkan line graph.
5. Aktifkan logging CSV sebelum RUN.
6. Lakukan run ON/OFF minimal 3 hysteresis.
7. Lakukan run PID sesuai skenario dosen.
8. Simpan file tanpa mengubah data mentah.
9. Copy salah satu CSV menjadi `sample_data/daq_export.csv`.
10. Edit mapping kolom di `analyze_daqmaster.m`, lalu jalankan.
11. Ekspor grafik dan tabel metrik.

## Troubleshooting
- tidak connect: periksa COM, address, baud, parity, stop bit, wiring A/B;
- data kosong: pastikan tag PV/SV dipilih dan logging aktif;
- MATLAB `readtable` salah delimiter: cek separator CSV pada editor teks;
- waktu berupa datetime: konversi ke seconds dari waktu awal.

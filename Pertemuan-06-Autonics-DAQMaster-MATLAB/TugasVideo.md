# Tugas Video Pertemuan 6

## Tujuan video
Membuktikan bahwa mahasiswa memahami alur akuisisi data digital, kualitas CSV, sampling, serta perbandingan DAQMaster dengan metode manual P5.

## Isi wajib
1. identitas dan tujuan;
2. diagram `device -> DAQMaster -> CSV -> MATLAB/Python`;
3. tampilkan metadata komunikasi yang digunakan laboratorium;
4. tampilkan device/project DAQMaster dan nilai live;
5. tampilkan trend graph dan raw CSV;
6. jelaskan nama kolom, timestamp, satuan, dan sample interval;
7. jalankan `examples/csv_quality_report.py`;
8. jalankan `examples/analyze_daqmaster.py` atau analisis MATLAB;
9. tampilkan statistik `dt min/median/max`;
10. tunjukkan contoh missing/duplicate data bila ada dan cara mendokumentasikannya;
11. bandingkan minimal satu run P5 dengan satu run P6;
12. jelaskan perbedaan peak/settling bila sampling berbeda;
13. jelaskan raw vs processed data;
14. lakukan satu troubleshooting kasus CSV/header;
15. kesimpulan berbasis metrics dan kualitas data.

## File pendamping
```text
NIM_Nama_P06_raw.csv
NIM_Nama_P06_processed.csv
NIM_Nama_P06_summary.csv
NIM_Nama_P06_trend.png
NIM_Nama_P06_P5_vs_P6.png
```

## Rubrik
- pemahaman DAQ dan metadata: 20%;
- raw data dan audit kualitas: 20%;
- bukti program MATLAB/Python: 20%;
- analisis sampling dan response metrics: 25%;
- troubleshooting dan kesimpulan: 15%.

Video harus memperlihatkan proses analisis nyata, bukan hanya slide atau screenshot hasil akhir.
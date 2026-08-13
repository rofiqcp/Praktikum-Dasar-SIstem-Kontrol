# Tugas Video Pertemuan 5

## Tujuan
Membuktikan pemahaman metode pengamatan manual dan analisis respon temperatur.

## Isi wajib
1. identitas dan tujuan praktikum;
2. diagram blok sistem temperatur;
3. jelaskan PV, SV, error, hysteresis, dan PID secara konseptual;
4. jelaskan metadata yang harus dicatat sebelum membandingkan run;
5. tampilkan template Excel/CSV dan arti setiap kolom;
6. tampilkan minimal tiga dataset;
7. tunjukkan raw data sebelum analisis;
8. jalankan `examples/analyze_manual_response.py`;
9. jalankan `examples/compare_manual_runs.py`;
10. tampilkan grafik PV-SV dan grafik perbandingan;
11. jelaskan rise time, peak, overshoot, settling time, dan steady-state error;
12. bahas keterbatasan sampling stopwatch/missing sample;
13. bandingkan satu run repeatability;
14. jelaskan mengapa P6 beralih ke logging DAQMaster;
15. tutup dengan kesimpulan berbasis angka.

## File pendamping
```text
NIM_Nama_P05_runA.csv
NIM_Nama_P05_runB.csv
NIM_Nama_P05_runC.csv
NIM_Nama_P05_comparison.png
NIM_Nama_P05_summary.csv
```

## Rubrik
- konsep dan diagram: 20%;
- kualitas raw data/metadata: 20%;
- bukti program dijalankan: 20%;
- analisis response metrics: 25%;
- troubleshooting dan kesimpulan: 15%.

## Pengurangan nilai
- hanya membaca materi tanpa menunjukkan proses;
- raw data tidak tersedia;
- grafik tanpa label/satuan;
- membandingkan run yang kondisi awalnya tidak terdokumentasi;
- menyatakan hasil “lebih bagus” tanpa angka pendukung;
- menghapus data anomali tanpa penjelasan.

Gunakan data dari setup laboratorium yang telah disiapkan. Modifikasi instalasi daya bukan bagian tugas video.
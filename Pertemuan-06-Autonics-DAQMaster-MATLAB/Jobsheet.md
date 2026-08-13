# Jobsheet Pertemuan 6 — DAQMaster dan Analisis CSV

## Tujuan
Mahasiswa mendokumentasikan setup akuisisi, mengaudit kualitas CSV, menganalisis data, dan membandingkan hasil digital dengan data manual P5.

## A. Metadata setup
Isi model device, address, baud, parity, stop bit, interface, port, interval logging, nama file, dan waktu eksperimen sesuai konfigurasi laboratorium.

## B. Bukti DAQMaster
Simpan screenshot project/device, nilai live, trend graph, setting logging, dan lokasi raw file.

## C. Audit raw CSV
Catat:
- jumlah baris;
- nama kolom;
- format timestamp;
- delimiter;
- missing values;
- duplicate timestamp;
- satuan;
- interval sample.

Jangan mengedit raw copy.

## D. Analisis sample repository
MATLAB:

```matlab
analyze_daqmaster('sample_data/daq_export.csv')
```

Python:

```bash
python examples/analyze_daqmaster.py sample_data/daq_export.csv
python examples/csv_quality_report.py sample_data/daq_export.csv
```

## E. Analisis data kelompok
Ulangi analisis dengan CSV hasil kelompok. Jika header berbeda dari sample, dokumentasikan mapping kolom.

## F. Statistik sampling
Buat tabel:

| File | N | dt min | dt median | dt max | missing | duplicate |
|---|---:|---:|---:|---:|---:|---:|
| sample | | | | | | |
| kelompok | | | | | | |

## G. Perbandingan run
Gunakan `examples/compare_runs.m` atau script plot sendiri. Semua kurva wajib diberi label dan metadata.

## H. P5 vs P6
Pilih satu dataset P5 dan P6 yang paling comparable. Bandingkan:
- jumlah sampel;
- interval waktu;
- peak;
- overshoot;
- settling time;
- steady-state error;
- missing sample;
- error operator/transkripsi.

## Analisis wajib
1. Mengapa jumlah sampel lebih banyak belum tentu berarti data lebih baik?
2. Apa akibat timestamp tidak monoton?
3. Mengapa raw file harus disimpan terpisah dari processed data?
4. Metric mana yang paling sensitif terhadap interval sampling?
5. Apakah kesimpulan P5 dan P6 sama?
6. Bagaimana membuktikan proses cleaning tidak mengubah makna data?
7. Apa keuntungan audit trail logging digital?

## Troubleshooting
- CSV error: cek delimiter/header.
- Nama kolom berbeda: buat mapping eksplisit.
- Timestamp datetime: konversi ke elapsed seconds.
- Duplicate/missing: hitung dan dokumentasikan sebelum cleaning.
- Data tidak comparable: audit kondisi awal dan metadata.

## Deliverable
1. screenshot DAQMaster;
2. raw CSV;
3. processed CSV bila digunakan;
4. statistik sampling;
5. grafik;
6. response metrics;
7. tabel P5-vs-P6;
8. jawaban analisis;
9. video P6.

## Kriteria selesai
Mahasiswa dapat menjelaskan alur `device -> DAQMaster -> CSV -> analyzer`, menunjukkan raw file, dan mempertahankan keputusan analisis berdasarkan data.
# Jobsheet Pertemuan 7 — MATLAB–Arduino Mega

## Tujuan
Memvalidasi koneksi MATLAB–Arduino, digital I/O dasar, analog input, timestamp, CSV logging, sample interval, filtering, dan kalibrasi.

## A. Connection check
1. Pastikan Support Package tersedia.
2. Jalankan `examples/connection_check.m`.
3. Catat board dan port yang digunakan.
4. Buat object Arduino dengan konfigurasi yang benar.

## B. Digital I/O dasar
Jalankan `examples/led_adc.m` pada indikator low-voltage/built-in yang tersedia pada trainer. Jelaskan alur command dari MATLAB ke pin.

## C. Analog logging
`led_adc.m` juga membaca kanal analog dan membuat `adc_log.csv`.

Catat:
- durasi;
- jumlah sampel;
- range tegangan;
- nama pin;
- satuan.

## D. Sample interval
Jalankan:

```matlab
run('examples/sample_interval_analysis.m')
```

Catat `dt min`, `dt median`, dan `dt max`.

## E. Filtering
Jalankan:

```matlab
run('examples/filter_compare.m')
```

Bandingkan raw dan moving average 5 sampel. Jelaskan noise reduction dan delay/smoothing.

## F. Kalibrasi
Jalankan:

```matlab
run('examples/adc_calibration.m')
```

Kemudian buka `examples/adc_to_temperature_example.m` dan jelaskan bahwa persamaan konversi harus disesuaikan dengan sensor/trainer aktual.

## G. Tabel hasil
| Parameter | Nilai | Satuan |
|---|---:|---|
| jumlah sampel | | sample |
| durasi | | s |
| A0 minimum | | V |
| A0 maksimum | | V |
| dt minimum | | s |
| dt median | | s |
| dt maksimum | | s |
| calibration m | | |
| calibration b | | |

## H. Analisis wajib
1. Mengapa timestamp aktual harus disimpan?
2. Mengapa `pause()` tidak menjamin sample time persis?
3. Apa arti resolusi ADC 10-bit?
4. Mengapa raw data tidak boleh diganti dengan data filtered?
5. Apa trade-off moving average window lebih besar?
6. Mengapa persamaan kalibrasi harus memiliki satuan?
7. Apa risiko extrapolation di luar titik kalibrasi?
8. Mengapa P7 menjadi prerequisite sebelum P9?

## Troubleshooting
- board tidak terdeteksi: cek Support Package, board, port, kabel data, dan port conflict;
- `adc_log.csv` tidak ada: jalankan `led_adc.m` dahulu;
- data tetap: audit pin/range input trainer;
- sampling terlalu lambat: kurangi plotting di dalam loop;
- output filter tampak terlambat: jelaskan efek averaging window.

## Deliverable
Source MATLAB, screenshot koneksi, `adc_log.csv`, histogram interval, grafik raw-vs-filtered, hasil kalibrasi, tabel hasil, jawaban analisis, dan video P7.
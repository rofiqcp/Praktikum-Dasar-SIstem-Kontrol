# Jobsheet Pertemuan 10 — Encoder, RPM, dan Posisi

## Tujuan
Memvalidasi encoder quadrature dan menghasilkan feedback count, posisi, serta RPM yang benar sebelum data tersebut digunakan pada P11 dan P12.

## File yang digunakan
```text
examples/arduino_encoder_stream/arduino_encoder_stream.ino
examples/matlab_monitor_encoder.m
examples/cpr_calibration.m
examples/encoder_math_offline.m
examples/analyze_encoder_log.m
examples/quadrature_state_test.py
```

## A. Pre-test
Jelaskan:
1. PPR dan CPR;
2. decoding x4;
3. rumus posisi;
4. rumus RPM;
5. alasan konvensi arah harus konsisten dari encoder sampai controller.

## B. Pengujian state secara offline
Jalankan:

```bash
python examples/quadrature_state_test.py
```

Catat urutan state untuk arah positif dan negatif. Jelaskan mengapa lookup table dapat menghasilkan nilai 0 pada transisi yang tidak valid atau tidak menunjukkan perpindahan.

## C. Verifikasi telemetry
Gunakan sketch P10 pada trainer laboratorium. Header yang diharapkan:

```text
#PROTO,ENCODER_STREAM,1
#ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Pastikan setiap baris data numerik mempunyai enam kolom dan timestamp terus meningkat.

## D. Kalibrasi CPR
Catat count awal dan count akhir untuk beberapa revolusi referensi.

| Percobaan | Revolusi | Count awal | Count akhir | Delta count | Estimasi CPR |
|---:|---:|---:|---:|---:|---:|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Masukkan data ke `examples/cpr_calibration.m`, kemudian jalankan:

```matlab
run('examples/cpr_calibration.m')
```

Catat nilai rata-rata/median, variasi antarpercobaan, dan apakah CPR mengacu pada shaft motor, shaft encoder, atau output gearbox.

## E. Validasi posisi
Gunakan referensi mekanik yang tersedia pada trainer dan bandingkan dengan:

```text
position_deg = count/CPR*360
```

Catat minimal satu perubahan posisi positif dan satu perubahan posisi negatif. Evaluasi:
- kesalahan skala;
- kesalahan tanda;
- repeatability bila posisi yang sama diulang.

## F. MATLAB monitor
Sesuaikan port komunikasi, kemudian jalankan:

```matlab
run('examples/matlab_monitor_encoder.m')
```

Simpan data yang mempunyai segmen arah positif, diam, dan arah negatif.

## G. Interval sampling dan resolusi RPM
Hitung:

```text
DeltaRPM = 60/(CPR*dt)
```

Bandingkan minimal dua nilai `dt`. Jelaskan kompromi antara respons pengukuran yang cepat dan kuantisasi RPM.

## H. Perbandingan filter
Bandingkan:

| Sinyal | Noise/variasi | Delay | Catatan |
|---|---|---|---|
| rpm_raw | | | |
| rpm_ma | | | |
| rpm_lpf | | | |

Jelaskan mengapa sinyal yang paling halus belum tentu menjadi feedback terbaik untuk loop kontrol yang membutuhkan respons cepat.

## I. Verifikasi matematika secara offline
Jalankan:

```matlab
run('examples/encoder_math_offline.m')
```

Verifikasi hubungan antara count, derajat, perubahan count, `dt`, dan RPM.

## J. Analisis log
Jalankan:

```matlab
run('examples/analyze_encoder_log.m')
```

Laporan minimal memuat:
- count terhadap waktu;
- posisi terhadap waktu;
- RPM raw/MA/LPF;
- statistik interval sampling;
- RPM minimum dan maksimum;
- bukti tanda arah positif dan negatif.

## K. Pertanyaan analisis
1. Mengapa CPR sebaiknya diukur menggunakan beberapa revolusi?
2. Bagaimana gearbox memengaruhi CPR jika posisi diukur pada output shaft?
3. Apa akibatnya jika nilai CPR yang dipakai dua kali lebih besar dari nilai sebenarnya?
4. Mengapa RPM mentah dapat terlihat bertingkat pada kecepatan rendah?
5. Mengapa moving average menambah keterlambatan?
6. Apa arti parameter `alpha` pada LPF?
7. Mengapa posisi unwrapped berguna untuk P12?
8. Apa akibat konvensi tanda yang berbeda antara sensor dan controller?
9. Mengapa timestamp harus diperiksa sebelum menganalisis RPM?
10. Bukti apa yang harus tersedia sebelum feedback dinyatakan siap untuk PID?

## Deliverable
```text
NIM_Nama_P10/
  firmware/
  matlab/
  raw/
  results/
  laporan.pdf
```

## Kriteria kelulusan
- [ ] count bertanda benar;
- [ ] CPR terverifikasi;
- [ ] posisi sesuai skala;
- [ ] RPM positif dan negatif terbaca;
- [ ] perbedaan raw/MA/LPF dapat dijelaskan;
- [ ] log tersimpan;
- [ ] konvensi arah terdokumentasi;
- [ ] tidak ada ketidaksesuaian satuan antara source, telemetry, dan laporan.

## Expected result
Feedback encoder tervalidasi dari sisi skala, waktu, filtering, dan tanda sehingga layak digunakan sebagai input pada P11 dan P12.

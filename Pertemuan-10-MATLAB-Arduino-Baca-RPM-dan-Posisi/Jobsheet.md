# Jobsheet Pertemuan 10 — Encoder, RPM, dan Posisi

## Tujuan
Memvalidasi encoder quadrature dan menghasilkan feedback count, position, serta RPM yang benar sebelum digunakan pada P11/P12.

## File
```text
examples/arduino_encoder_stream/arduino_encoder_stream.ino
examples/matlab_monitor_encoder.m
examples/cpr_calibration.m
examples/encoder_math_offline.m
examples/analyze_encoder_log.m
examples/quadrature_state_test.py
```

## A. Pre-test
Jelaskan PPR, CPR, x4 decoding, rumus posisi, rumus RPM, dan alasan tanda arah harus konsisten.

## B. Offline state test
```bash
python examples/quadrature_state_test.py
```

Catat sequence state untuk arah positif dan negatif serta fungsi nilai 0 pada lookup table.

## C. Verifikasi telemetry
Gunakan sketch P10 pada trainer laboratorium. Header yang diharapkan:

```text
#PROTO,ENCODER_STREAM,1
#ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Pastikan baris numerik mempunyai enam kolom.

## D. Kalibrasi CPR
Catat count awal/akhir untuk beberapa revolusi referensi.

| Trial | Revolutions | Start | End | Delta | CPR estimate |
|---:|---:|---:|---:|---:|---:|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Masukkan data ke `examples/cpr_calibration.m` dan jalankan:

```matlab
run('examples/cpr_calibration.m')
```

Catat apakah CPR mengacu pada motor shaft atau output gearbox.

## E. Validasi posisi
Gunakan referensi mekanik yang tersedia pada trainer dan bandingkan dengan:

```text
position_deg = count/CPR*360
```

Catat minimal satu perubahan positif dan satu negatif. Evaluasi error skala dan tanda.

## F. MATLAB monitor
Sesuaikan port lalu:

```matlab
run('examples/matlab_monitor_encoder.m')
```

Simpan data yang memiliki segmen positif, diam, dan negatif.

## G. Sample interval
Hitung:

```text
DeltaRPM = 60/(CPR*dt)
```

Bandingkan minimal dua nilai `dt` secara analitis atau menggunakan dataset. Jelaskan tradeoff latency vs quantization.

## H. Filter comparison
Bandingkan:

| Sinyal | Noise | Delay | Catatan |
|---|---|---|---|
| rpm_raw | | | |
| rpm_ma | | | |
| rpm_lpf | | | |

Jelaskan mengapa sinyal paling halus belum tentu paling baik untuk feedback loop cepat.

## I. Offline math
```matlab
run('examples/encoder_math_offline.m')
```

Verifikasi hubungan count, degree, delta count, `dt`, dan RPM.

## J. Analisis log
```matlab
run('examples/analyze_encoder_log.m')
```

Laporan minimal:
- count vs time;
- position vs time;
- raw/MA/LPF RPM;
- statistik sample interval;
- min/max RPM;
- tanda arah.

## K. Pertanyaan
1. Mengapa CPR diukur beberapa revolusi?
2. Bagaimana gearbox memengaruhi CPR pada output shaft?
3. Apa akibat CPR dua kali terlalu besar?
4. Mengapa raw RPM bertingkat pada speed rendah?
5. Mengapa moving average menambah delay?
6. Apa arti alpha LPF?
7. Mengapa posisi unwrapped berguna untuk P12?
8. Apa akibat sign convention yang berbeda antara sensor dan controller?
9. Mengapa timestamp harus diperiksa?
10. Bukti apa yang diperlukan sebelum sensor dinyatakan siap untuk PID?

## Deliverable
```text
NIM_Nama_P10/
  firmware/
  matlab/
  raw/
  results/
  laporan.pdf
```

## Acceptance
- [ ] count bertanda benar;
- [ ] CPR terverifikasi;
- [ ] posisi sesuai skala;
- [ ] RPM positif/negatif terbaca;
- [ ] raw/MA/LPF dapat dijelaskan;
- [ ] log tersimpan;
- [ ] konvensi arah terdokumentasi.

## Expected result
Feedback encoder tervalidasi dari sisi skala, waktu, filtering, dan tanda sehingga layak menjadi input P11/P12.
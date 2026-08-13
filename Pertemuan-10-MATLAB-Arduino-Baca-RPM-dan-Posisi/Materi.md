# Pertemuan 10 — MATLAB–Arduino: Encoder, RPM, dan Posisi Motor DC

## Capaian pembelajaran
Mahasiswa mampu:

1. menjelaskan encoder incremental quadrature;
2. membaca state A/B dan menentukan arah;
3. membedakan PPR, CPR, x1/x2/x4 decoding, dan efek gearbox;
4. mengkalibrasi `COUNTS_PER_REV` dari pengukuran;
5. mengubah count menjadi posisi derajat;
6. menghitung RPM dari delta count dan sample interval;
7. menjelaskan quantization error pada RPM;
8. membandingkan raw RPM, moving average, dan low-pass filter;
9. memvalidasi tanda CW/CCW end-to-end;
10. membuat log serial untuk digunakan pada P11/P12.

---

## 1. Mengapa P10 dipisahkan dari PID
P10 sengaja tidak fokus tuning controller. Sebelum closed-loop digunakan, feedback harus benar.

```text
encoder -> count -> CPR -> position
              |
              +-> delta count / delta time -> RPM -> filter
```

Jika tanda, CPR, atau sampling salah, PID P11/P12 dapat terlihat gagal padahal akar masalah ada di feedback.

---

## 2. Encoder incremental quadrature
Encoder A/B menghasilkan dua sinyal digital berbeda fase sekitar 90° electrical.

State yang mungkin:

```text
00, 01, 11, 10
```

Satu arah menghasilkan urutan tertentu; arah berlawanan menghasilkan urutan terbalik. Firmware memakai lookup table 4-state sehingga illegal transition dapat menghasilkan delta 0.

Baseline pin:
- `ENC_A = D2`;
- `ENC_B = D3`.

D2 dan D3 pada Arduino Mega mendukung external interrupt sehingga edge dapat dicatat tanpa polling loop yang lambat.

---

## 3. PPR vs CPR
Istilah vendor berbeda-beda sehingga angka datasheet harus dibaca hati-hati.

- **PPR** dapat berarti pulse per revolution per channel;
- **CPR** pada praktikum berarti jumlah **count hasil decoder** untuk satu putaran pada shaft yang dipakai sebagai referensi.

Jika encoder menghasilkan 100 pulse/rev per channel dan decoder x4, secara teori hasil dapat 400 count/rev. Gearbox dapat mengubah count pada output shaft.

Karena definisi vendor tidak selalu sama, P10 mewajibkan pengukuran manual.

---

## 4. Kalibrasi CPR
Prosedur konseptual:

1. catat count awal;
2. putar shaft referensi sejumlah revolusi yang diketahui;
3. catat count akhir;
4. hitung `abs(delta_count)/revolutions`;
5. ulangi beberapa kali;
6. gunakan median/mean dan catat variasinya.

Lebih dari satu revolusi biasanya mengurangi pengaruh error penempatan tanda mekanik.

Helper:

```matlab
run('examples/cpr_calibration.m')
```

---

## 5. Posisi dari count
Untuk posisi unwrapped:

```text
position_deg = count / CPR * 360
```

Jika count terus bertambah, posisi dapat menjadi lebih dari 360° atau kurang dari 0°. Ini **bukan error**; itu adalah posisi multi-turn.

Jika hanya perlu tampilan satu putaran:

```matlab
wrapped = mod(position_deg,360);
```

P12 menggunakan posisi unwrapped sebagai baseline supaya tidak ada diskontinuitas 359° -> 0° dalam error controller.

---

## 6. Kecepatan dari delta count
Untuk interval `dt`:

```text
delta_count = count[k]-count[k-1]
rpm = delta_count/CPR * 60/dt
```

Tanda RPM mengikuti tanda delta count.

Contoh:

```text
CPR = 600
Delta count = 30
Delta t = 0.05 s
RPM = 30/600 * 60/0.05 = 60 RPM
```

---

## 7. Resolusi RPM dan sample time
Satu count dalam window menghasilkan perubahan RPM minimum kira-kira:

```text
DeltaRPM = 60 / (CPR * dt)
```

Dengan CPR=600 dan dt=0.05 s:

```text
DeltaRPM = 2 RPM/count
```

Jika sample window diperkecil menjadi 0.01 s:

```text
DeltaRPM = 10 RPM/count
```

Artinya sampling lebih cepat tidak otomatis memberi estimasi speed lebih halus. Ada tradeoff antara latency dan quantization.

---

## 8. Raw, moving average, dan LPF
Firmware P10 menghasilkan:

```text
rpm_raw
rpm_ma
rpm_lpf
```

### Raw
Paling cepat tetapi terlihat bertingkat/noisy pada speed rendah.

### Moving average

```text
y[k] = mean(x[k-N+1 ... k])
```

Mengurangi noise tetapi menambah delay dan memori.

### First-order low-pass

```text
y[k] = alpha*x[k] + (1-alpha)*y[k-1]
```

- alpha besar -> lebih responsif;
- alpha kecil -> lebih halus tetapi lebih lambat.

Pada baseline firmware, LPF diterapkan setelah moving average.

---

## 9. Decoder lookup table
Firmware menyimpan state sebelumnya dan state sekarang:

```text
index = previous_state*4 + current_state
```

Lookup table menghasilkan `-1`, `0`, atau `+1`.

Keuntungan:
- arah eksplisit;
- transisi invalid dapat diabaikan;
- mudah diuji dengan test vector.

Gunakan:

```bash
python examples/quadrature_state_test.py
```

untuk memahami transisi tanpa hardware.

---

## 10. Atomic read
`encoderCount` diubah di interrupt. Saat loop utama membaca variabel multi-byte, firmware baseline memakai:

```cpp
noInterrupts();
long c=encoderCount;
interrupts();
```

Tujuannya mengambil snapshot count yang konsisten.

---

## 11. Telemetry protocol P10
Firmware mengirim:

```text
#PROTO,ENCODER_STREAM,1
#ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Baris data:

```text
ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

MATLAB harus mengabaikan baris yang dimulai `#` dan hanya memproses data numerik dengan enam kolom.

---

## 12. MATLAB monitor
`matlab_monitor_encoder.m` membaca serial dan memplot data encoder.

Yang harus diperiksa:
- timestamp meningkat;
- count berubah;
- degree konsisten dengan count;
- RPM mempunyai tanda yang benar;
- raw/MA/LPF menunjukkan tradeoff smoothing.

Analisis offline:

```matlab
run('examples/analyze_encoder_log.m')
```

---

## 13. Validasi arah end-to-end
Definisikan konvensi, misalnya:

```text
CW mekanik = count positif = position positif = RPM positif
CCW mekanik = count negatif = position negatif = RPM negatif
```

Konvensi boleh dibalik, tetapi harus **konsisten** pada:
- encoder;
- MATLAB plot;
- P11 signed speed command;
- P12 signed position target.

Jangan memperbaiki tanda hanya pada grafik bila controller menggunakan tanda yang berbeda.

---

## 14. Error diagnosis
### Count tidak berubah
Periksa channel A/B, common reference, pull-up, dan apakah pin yang digunakan sesuai sketch.

### Count hanya satu arah
Audit sequence quadrature dan state A/B.

### Posisi salah skala
CPR salah atau referensi shaft berbeda dari saat kalibrasi.

### RPM terlalu noisy
Window terlalu pendek, CPR rendah, atau sinyal encoder buruk.

### RPM selalu positif
Tanda delta count hilang pada salah satu tahap.

### Posisi benar tetapi RPM salah
Audit `lastCount`, `delta_count`, `dt`, dan CPR.

---

## 15. Program wajib

```text
examples/arduino_encoder_stream/arduino_encoder_stream.ino
examples/matlab_monitor_encoder.m
examples/cpr_calibration.m
examples/encoder_math_offline.m
examples/analyze_encoder_log.m
examples/quadrature_state_test.py
```

Urutan:

```text
quadrature theory
-> offline state test
-> manual CPR calibration
-> count/position validation
-> RPM raw
-> MA/LPF
-> MATLAB logging
-> sign audit
```

---

## 16. Deliverable data minimum
Catat:
- measured CPR;
- jumlah revolusi kalibrasi;
- error/repeatability CPR;
- sample interval;
- posisi + dan -;
- RPM + dan -;
- raw vs MA vs LPF;
- screenshot serial/MATLAB;
- CSV log.

---

## 17. Jembatan ke P11
P11 tidak boleh dimulai sebelum P10 lulus tiga syarat:

1. count bertanda benar;
2. CPR telah diverifikasi;
3. RPM positif dan negatif terbaca benar.

Pada P11, `rpm_lpf` menjadi feedback untuk PID speed. Karena itu kesalahan P10 akan langsung masuk ke controller.
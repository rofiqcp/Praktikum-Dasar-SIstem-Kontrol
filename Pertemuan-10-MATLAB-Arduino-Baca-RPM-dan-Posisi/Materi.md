# Pertemuan 10 — MATLAB–Arduino: Encoder, RPM, dan Posisi Motor DC

## Capaian pembelajaran
Mahasiswa mampu:

1. menjelaskan encoder incremental quadrature;
2. membaca keadaan kanal A/B dan menentukan arah;
3. membedakan PPR, CPR, decoding x1/x2/x4, dan pengaruh gearbox;
4. menentukan `COUNTS_PER_REV` berdasarkan hasil pengukuran;
5. mengubah count menjadi posisi dalam derajat;
6. menghitung RPM dari perubahan count dan interval sampling;
7. menjelaskan quantization error pada estimasi RPM;
8. membandingkan RPM mentah, moving average, dan low-pass filter;
9. memvalidasi konsistensi tanda CW/CCW dari encoder sampai data MATLAB;
10. menghasilkan log serial yang siap digunakan pada P11 dan P12.

---

## 1. Mengapa P10 dipisahkan dari PID
P10 sengaja tidak berfokus pada tuning controller. Sebelum closed-loop digunakan, feedback harus dibuktikan benar.

```text
encoder -> count -> CPR -> position
              |
              +-> delta count / delta time -> RPM -> filter
```

Jika tanda, CPR, atau interval sampling salah, PID pada P11/P12 dapat terlihat gagal walaupun akar masalah sebenarnya berada pada feedback.

---

## 2. Encoder incremental quadrature
Encoder kanal A dan B menghasilkan dua sinyal digital yang berbeda fase sekitar 90 derajat elektrik.

Keadaan logika yang mungkin:

```text
00, 01, 11, 10
```

Satu arah putaran menghasilkan urutan keadaan tertentu, sedangkan arah sebaliknya menghasilkan urutan yang terbalik. Firmware menggunakan lookup table empat-keadaan sehingga transisi yang tidak valid dapat diabaikan dengan menghasilkan perubahan count sebesar 0.

Baseline pin:
- `ENC_A = D2`;
- `ENC_B = D3`.

D2 dan D3 pada Arduino Mega mendukung external interrupt sehingga perubahan kanal dapat dicatat tanpa bergantung pada polling loop utama.

---

## 3. PPR dan CPR
Istilah pada datasheet vendor tidak selalu seragam sehingga angka spesifikasi harus dibaca dengan hati-hati.

- **PPR** umumnya merujuk pada jumlah pulse per revolution per channel;
- **CPR** pada praktikum ini berarti jumlah **count hasil decoder** untuk satu putaran pada shaft yang digunakan sebagai referensi.

Jika encoder menghasilkan 100 pulse/rev per channel dan decoder menggunakan x4, nilai teoritis dapat menjadi 400 count/rev. Gearbox dapat mengubah jumlah count bila referensi pengukuran berada pada output shaft.

Karena definisi vendor dapat berbeda, P10 mewajibkan verifikasi melalui pengukuran.

---

## 4. Kalibrasi CPR
Langkah konseptual:

1. catat count awal;
2. putar shaft referensi sebanyak jumlah revolusi yang diketahui;
3. catat count akhir;
4. hitung `abs(delta_count)/revolutions`;
5. ulangi beberapa kali;
6. gunakan nilai rata-rata atau median dan catat variasinya.

Menggunakan beberapa revolusi biasanya mengurangi pengaruh kesalahan penempatan tanda mekanik.

Helper:

```matlab
run('examples/cpr_calibration.m')
```

Catat dengan jelas apakah CPR mengacu pada shaft motor, shaft encoder, atau output gearbox.

---

## 5. Posisi dari count
Untuk posisi unwrapped:

```text
position_deg = count / CPR * 360
```

Jika count terus bertambah, posisi dapat lebih besar dari 360 derajat atau lebih kecil dari 0 derajat. Hal ini bukan kesalahan; nilai tersebut menunjukkan posisi multi-turn.

Jika hanya diperlukan tampilan satu putaran:

```matlab
wrapped = mod(position_deg,360);
```

P12 menggunakan posisi unwrapped sebagai baseline agar error controller tidak mengalami diskontinuitas buatan pada batas 359 derajat ke 0 derajat.

---

## 6. Kecepatan dari perubahan count
Untuk interval `dt`:

```text
delta_count = count[k]-count[k-1]
rpm = delta_count/CPR * 60/dt
```

Tanda RPM mengikuti tanda `delta_count`.

Contoh:

```text
CPR = 600
Delta count = 30
Delta t = 0.05 s
RPM = 30/600 * 60/0.05 = 60 RPM
```

---

## 7. Resolusi RPM dan interval sampling
Satu count dalam satu interval pengukuran menghasilkan perubahan RPM minimum kira-kira:

```text
DeltaRPM = 60 / (CPR * dt)
```

Dengan CPR=600 dan `dt=0.05 s`:

```text
DeltaRPM = 2 RPM/count
```

Jika interval diperkecil menjadi `0.01 s`:

```text
DeltaRPM = 10 RPM/count
```

Artinya, sampling yang lebih cepat tidak otomatis menghasilkan estimasi RPM yang lebih halus. Terdapat kompromi antara keterlambatan pengukuran dan kuantisasi.

---

## 8. RPM mentah, moving average, dan LPF
Firmware P10 menghasilkan:

```text
rpm_raw
rpm_ma
rpm_lpf
```

### RPM mentah
Respons paling cepat, tetapi pada kecepatan rendah dapat terlihat bertingkat dan lebih mudah dipengaruhi kuantisasi.

### Moving average

```text
y[k] = mean(x[k-N+1 ... k])
```

Mengurangi variasi data tetapi menambah keterlambatan dan membutuhkan buffer sampel.

### Low-pass filter orde satu

```text
y[k] = alpha*x[k] + (1-alpha)*y[k-1]
```

- `alpha` besar: lebih responsif terhadap perubahan;
- `alpha` kecil: lebih halus tetapi lebih lambat.

Pada firmware baseline, LPF diterapkan setelah moving average. Mahasiswa harus menyadari bahwa dua tahap filtering dapat menambah keterlambatan feedback.

---

## 9. Decoder lookup table
Firmware menyimpan keadaan sebelumnya dan keadaan saat ini:

```text
index = previous_state*4 + current_state
```

Lookup table menghasilkan `-1`, `0`, atau `+1`.

Keuntungan pendekatan ini:
- arah perubahan count terlihat jelas;
- transisi yang tidak valid dapat diabaikan;
- decoder dapat diuji menggunakan test vector tanpa hardware.

Gunakan:

```bash
python examples/quadrature_state_test.py
```

untuk mempelajari urutan transisi secara offline.

---

## 10. Pembacaan atomik count
`encoderCount` diubah di interrupt. Variabel `long` terdiri atas beberapa byte, sehingga loop utama perlu mengambil snapshot yang konsisten.

Firmware baseline menggunakan:

```cpp
noInterrupts();
long c=encoderCount;
interrupts();
```

Tujuannya bukan menghentikan interrupt dalam waktu lama, tetapi memastikan nilai count tidak berubah di tengah proses penyalinan.

---

## 11. Protokol telemetry P10
Firmware mengirim header:

```text
#PROTO,ENCODER_STREAM,1
#ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Baris data numerik berisi enam kolom:

```text
ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Program MATLAB harus mengabaikan baris yang diawali `#` dan hanya memproses data numerik dengan jumlah kolom yang benar.

---

## 12. MATLAB monitor
`matlab_monitor_encoder.m` membaca telemetry serial, menyimpan data, dan membuat grafik.

Hal yang harus diperiksa:
- timestamp meningkat;
- count berubah sesuai gerakan;
- `position_deg` konsisten dengan count dan CPR;
- RPM mempunyai tanda yang sesuai arah;
- raw/MA/LPF menunjukkan perbedaan noise dan keterlambatan.

Analisis offline:

```matlab
run('examples/analyze_encoder_log.m')
```

---

## 13. Validasi arah dari ujung ke ujung
Definisikan satu konvensi arah, misalnya:

```text
CW mekanik = count positif = posisi positif = RPM positif
CCW mekanik = count negatif = posisi negatif = RPM negatif
```

Konvensi boleh dibalik, tetapi harus konsisten pada:
- encoder;
- grafik MATLAB;
- signed speed command pada P11;
- target posisi bertanda pada P12.

Jangan hanya membalik tanda pada grafik bila controller menggunakan konvensi yang berbeda.

---

## 14. Diagnosis kesalahan
### Count tidak berubah
Periksa kanal A/B, ground bersama, pull-up, dan kesesuaian pin dengan sketch.

### Count hanya benar pada satu arah
Audit urutan quadrature dan keadaan kanal A/B.

### Posisi salah skala
CPR salah atau shaft referensi berbeda dari shaft yang digunakan saat kalibrasi.

### RPM terlalu berfluktuasi
Interval pengukuran terlalu pendek, CPR rendah, atau kualitas sinyal encoder kurang baik.

### RPM selalu positif
Tanda `delta_count` hilang pada salah satu tahap perhitungan atau pengolahan data.

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

Urutan belajar:

```text
teori quadrature
-> pengujian state secara offline
-> kalibrasi CPR
-> validasi count dan posisi
-> RPM mentah
-> moving average dan LPF
-> logging MATLAB
-> audit tanda arah
```

---

## 16. Data minimum yang dikumpulkan
Catat:
- CPR hasil pengukuran;
- jumlah revolusi kalibrasi;
- variasi hasil CPR;
- interval sampling;
- posisi positif dan negatif;
- RPM positif dan negatif;
- perbandingan raw, MA, dan LPF;
- screenshot serial/MATLAB;
- CSV log.

---

## 17. Gate menuju P11
P11 tidak boleh dimulai sebelum P10 memenuhi tiga syarat utama:

1. count bertanda benar;
2. CPR telah diverifikasi;
3. RPM positif dan negatif terbaca dengan benar.

Pada P11, `rpm_lpf` digunakan sebagai feedback PID kecepatan. Karena itu setiap kesalahan pada P10 akan langsung memengaruhi controller P11.

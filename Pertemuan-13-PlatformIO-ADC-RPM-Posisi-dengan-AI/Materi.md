# Pertemuan 13 — PlatformIO Arduino Mega: ADC, RPM, Posisi, dan Workflow AI

## Capaian pembelajaran
Setelah praktikum ini mahasiswa mampu:

1. menjelaskan perbedaan workflow MATLAB–Arduino dan firmware PlatformIO;
2. membuat, membangun, mengunggah, dan memonitor project Arduino Mega dari VS Code/PlatformIO;
3. membaca ADC A1 dan mengubahnya menjadi tegangan;
4. membaca encoder quadrature A/B menggunakan interrupt;
5. menjelaskan atomic read pada variabel 32-bit di AVR 8-bit;
6. menghitung posisi dan RPM dari count serta `COUNTS_PER_REV`;
7. membandingkan RPM mentah, moving average, dan low-pass filter;
8. memahami pengaruh interval sampling terhadap resolusi RPM dan keterlambatan feedback;
9. menggunakan protocol serial untuk konfigurasi dan telemetry;
10. menggunakan AI coding assistant dengan proses requirement → review → build → test → analisis, bukan copy-paste.

## 1. Posisi P13 dalam alur semester
P10–P12 menggunakan Arduino dan MATLAB untuk mempelajari encoder serta PID. P13 memindahkan fokus ke firmware C++ yang lebih mandiri.

```text
P10  : validasi encoder/RPM/posisi
P11  : PID kecepatan
P12  : PID posisi
P13  : firmware PlatformIO untuk ADC + encoder + telemetry
P14  : firmware PID suhu + GUI
P15  : firmware PID motor + GUI
```

P13 sengaja belum mengendalikan aktuator. Fokus utamanya adalah kualitas sensor, timing, struktur firmware, komunikasi serial, dan workflow pengembangan.

## 2. Struktur project PlatformIO
Project utama:

```text
examples/mega_io_monitor/
├── platformio.ini
└── src/
    └── main.cpp
```

Konfigurasi target:

```ini
[env:megaatmega2560]
platform = atmelavr
board = megaatmega2560
framework = arduino
monitor_speed = 115200
```

Perintah dasar:

```bash
pio run
pio run -t upload
pio device monitor -b 115200
```

`pio run` harus berhasil sebelum upload dilakukan. Build sukses membuktikan source dapat dikompilasi, tetapi belum membuktikan bahwa rumus, pin, arah encoder, CPR, dan satuannya benar.

## 3. Pin baseline
Firmware P13 menggunakan:

```text
A1 : ADC analog
D2 : encoder A
D3 : encoder B
USB serial : 115200 baud
```

Pin ini harus konsisten dengan trainer, dokumentasi, source, dan laporan.

## 4. ADC Arduino Mega
ADC Arduino Mega memiliki resolusi 10 bit sehingga nilai digital ideal berada pada:

```text
0 ... 1023
```

Dengan referensi tegangan 5 V sebagai baseline contoh:

```text
voltage = adc_raw * 5.0 / 1023.0
```

Resolusi ideal per count:

```text
5 / 1023 ≈ 4.89 mV/count
```

Nilai tersebut merupakan konversi nominal. Untuk pengukuran presisi, tegangan referensi aktual, toleransi sensor, noise, dan rangkaian conditioning tetap perlu dipertimbangkan.

## 5. Encoder quadrature
Encoder A/B mempunyai empat keadaan:

```text
00, 01, 11, 10
```

Firmware menyimpan `prevState`, membaca state baru, lalu menggunakan lookup table 16 elemen:

```text
QDEC[(prevState << 2) | state]
```

Hasil transisi adalah:

```text
-1, 0, atau +1
```

Dengan cara ini count mempunyai tanda sehingga arah putaran dapat dibedakan.

## 6. Interrupt Service Routine
ISR encoder harus singkat. Pada P13 ISR hanya:

1. membaca A/B;
2. membentuk state;
3. mengambil delta dari lookup table;
4. memperbarui `encoderCount`;
5. menyimpan state baru.

Hindari operasi berat di ISR seperti:

- `Serial.print()`;
- `delay()`;
- alokasi memori dinamis;
- parsing String;
- plotting atau perhitungan floating point panjang.

Tujuannya menjaga latensi ISR rendah dan mengurangi peluang edge encoder terlewat.

## 7. Atomic read pada AVR
Arduino Mega menggunakan AVR 8-bit, sedangkan `encoderCount` bertipe 32-bit. Pembacaan variabel tersebut dapat terjadi ketika ISR sedang mengubah sebagian byte.

Karena itu snapshot count dilakukan di critical section:

```cpp
noInterrupts();
int32_t c = encoderCount;
interrupts();
```

Critical section harus sesingkat mungkin.

## 8. CPR dan posisi
Gunakan CPR hasil validasi P10.

```text
position_deg = count / CPR * 360
```

Posisi P13 bersifat unwrapped: nilai dapat melebihi ±360°. Ini berguna untuk melihat total pergerakan tanpa diskontinuitas 359° → 0°.

Command:

```text
CPR,<nilai>
```

memungkinkan nilai CPR diubah tanpa mengompilasi ulang firmware.

## 9. RPM dari perubahan count
Setiap interval sampling:

```text
delta_count = count_now - count_previous
rpm = delta_count / CPR * 60 / dt
```

Resolusi RPM per satu count kira-kira:

```text
DeltaRPM = 60 / (CPR * dt)
```

Artinya interval sampling yang lebih pendek memberi respons lebih cepat tetapi dapat membuat RPM lebih bertingkat pada kecepatan rendah.

## 10. Moving average dan LPF
Firmware menghasilkan tiga sinyal:

```text
rpm_raw
rpm_ma
rpm_lpf
```

Moving average mengurangi variasi cepat dengan merata-ratakan beberapa sampel. LPF eksponensial menggunakan:

```text
rpm_lpf[k] = alpha*rpm_ma[k] + (1-alpha)*rpm_lpf[k-1]
```

Interpretasi `alpha`:

- mendekati 1 → lebih responsif, filtering lebih kecil;
- mendekati 0 → lebih halus, keterlambatan lebih besar.

Command yang tersedia:

```text
MA,<1..16>
ALPHA,<0..1>
TS,<10..300 ms>
```

## 11. ZERO harus mereset state estimator
Perintah:

```text
ZERO,1
```

bukan hanya mengubah `encoderCount` menjadi nol. Implementasi P13 juga mereset:

- `lastCount`;
- buffer moving average;
- jumlah sampel buffer;
- RPM LPF.

Hal ini penting karena jika count di-nol-kan tetapi `lastCount` masih menyimpan nilai lama, satu sampel berikutnya dapat terlihat sebagai lonjakan RPM palsu.

Setelah ZERO, verifikasi bahwa posisi kembali mendekati 0° dan tidak muncul spike RPM yang tidak masuk akal.

## 12. Telemetry P13
Saat boot firmware menampilkan:

```text
#PROTO,IO_MONITOR,2
#ms,adc_raw,voltage,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Baris numerik memiliki delapan kolom:

```text
ms,adc_raw,voltage,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Header yang dimulai `#` merupakan metadata dan tidak diperlakukan sebagai data numerik.

## 13. Command P13
Command utama:

```text
ZERO,1
TS,50
ALPHA,0.25
MA,8
CPR,600
STATUS,1
```

`STATUS,1` menampilkan parameter aktif. Setelah mengubah parameter, gunakan STATUS untuk memastikan firmware menerima nilai yang dimaksud.

## 14. Timing non-blocking
Loop tidak menggunakan `delay()` untuk jadwal telemetry. Firmware memakai `millis()`:

```text
jika now-last >= sampleMs -> ambil sampel
```

Pendekatan ini membuat serial parsing dan pembacaan sensor tetap dapat berlangsung tanpa menghentikan seluruh loop untuk waktu yang panjang.

## 15. Workflow AI yang benar
AI boleh digunakan sebagai pair programmer, tetapi proses engineering tetap harus dapat diaudit.

Urutan minimum:

```text
1. tulis requirement
2. tulis pin map dan satuan
3. minta AI membuat/menjelaskan perubahan
4. review diff
5. periksa ISR, tipe data, timing, dan protocol
6. pio run
7. test fitur satu per satu
8. bandingkan output dengan hitungan manual
9. simpan prompt dan hasil review
10. baru terima perubahan
```

Prompt contoh tersedia pada `PROMPT_AI_CONTOH.md`.

## 16. Hal yang wajib direview dari kode AI
Periksa minimal:

- apakah pin sesuai board;
- apakah ISR terlalu berat;
- apakah variabel bersama ISR dibaca secara atomik;
- apakah ada integer division yang tidak disengaja;
- apakah CPR dan satuan benar;
- apakah `dt` benar-benar dalam detik;
- apakah array filter dapat overflow indeks;
- apakah command mempunyai batas nilai;
- apakah protocol serial berubah tanpa dokumentasi;
- apakah ZERO mereset estimator;
- apakah kode berhasil dikompilasi.

## 17. Pengujian bertahap
Urutan pengujian yang direkomendasikan:

```text
build
-> serial header
-> ADC
-> encoder count
-> arah positif/negatif
-> CPR
-> posisi
-> RPM raw
-> MA
-> LPF
-> command parameter
-> ZERO
-> STATUS
-> review AI
```

Jangan menyimpulkan firmware benar hanya dari satu angka RPM.

## 18. Troubleshooting
### Build gagal
Baca error pertama yang relevan. Periksa syntax, board, framework, nama file, dan dependency.

### Port tidak muncul
Periksa kabel data, driver USB, hak akses port pada Linux, dan apakah port sedang dipakai program lain.

### ADC selalu 0 atau 1023
Periksa sumber sinyal analog, referensi ground, dan pin A1.

### Count tidak berubah
Periksa A/B, pull-up, interrupt pin, dan urutan wiring.

### Count hanya satu arah
Audit lookup table dan urutan A/B.

### Posisi salah skala
CPR atau shaft referensi salah.

### RPM terlalu noisy
Periksa `TS`, CPR, kualitas sinyal, MA, dan LPF.

### Ada spike setelah ZERO
Firmware yang benar harus mereset histori estimator bersama count. Pastikan source terbaru branch `v1` digunakan.

## 19. Program wajib

```text
examples/mega_io_monitor/platformio.ini
examples/mega_io_monitor/src/main.cpp
examples/python_serial_plotter/plot_serial.py
PROMPT_AI_CONTOH.md
```

Project `examples/mega_sensors` dipertahankan sebagai contoh sederhana, sedangkan `mega_io_monitor` adalah baseline praktikum P13 yang digunakan untuk penilaian.

## 20. Hasil yang diharapkan
P13 dinyatakan berhasil jika:

- `pio run` sukses;
- firmware menampilkan protocol yang benar;
- ADC dan voltage berubah secara masuk akal;
- count bertanda benar;
- CPR sesuai P10;
- posisi sesuai skala;
- RPM positif dan negatif dapat dibaca;
- raw/MA/LPF dapat dibandingkan;
- ZERO tidak menghasilkan spike palsu;
- parameter dapat diubah dan diperiksa melalui STATUS;
- mahasiswa dapat menjelaskan satu perubahan/review AI dengan bukti build dan test.

## 21. Jembatan ke P14
P13 membangun fondasi firmware dan telemetry. P14 mempertahankan disiplin PlatformIO, protocol, logging, dan workflow AI, lalu menambahkan PID suhu embedded serta GUI Python.
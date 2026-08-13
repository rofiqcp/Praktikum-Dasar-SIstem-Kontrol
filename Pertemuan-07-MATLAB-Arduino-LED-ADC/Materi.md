# Pertemuan 7 — MATLAB–Arduino Mega: Koneksi, Data I/O, Logging, dan Kalibrasi

## Capaian
Mahasiswa mampu menyiapkan Support Package, mengidentifikasi board/port, membuat object Arduino di MATLAB, membaca data analog, menguji digital I/O dasar pada trainer low-voltage, menyimpan timestamp dan CSV, serta mengevaluasi sample interval dan kalibrasi.

## Alur P7

```text
MATLAB -> USB -> Arduino Mega -> I/O low-voltage
```

P7 adalah tahap validasi toolchain. Fokusnya bukan closed-loop cepat, tetapi koneksi, satuan, logging, dan kualitas data.

## Software
- MATLAB;
- MATLAB Support Package for Arduino Hardware;
- Arduino Mega 2560.

Gunakan Add-On Manager untuk memastikan Support Package tersedia.

## Port dan object Arduino
Periksa port yang tersedia:

```matlab
serialportlist("available")
```

Contoh pembuatan object:

```matlab
a = arduino('COM5','Mega2560');
```

Port disesuaikan dengan komputer masing-masing.

## Digital I/O dasar
Digital output digunakan sebagai uji sederhana bahwa command MATLAB mencapai board. Pada P7 gunakan indikator low-voltage/built-in yang tersedia pada trainer.

## Analog input
Pembacaan analog dari Support Package menghasilkan nilai tegangan. Mahasiswa harus mencatat pin, satuan, dan range yang digunakan.

## ADC dan kuantisasi
Untuk ADC N-bit terdapat `2^N` level. Resolusi teoretis bergantung pada referensi tegangan. Noise dan kuantisasi menyebabkan pembacaan dapat sedikit berubah walaupun input relatif tetap.

## Sampling host-side
MATLAB berjalan di komputer sehingga interval loop dipengaruhi USB, OS, plotting, dan overhead MATLAB. Simpan timestamp aktual untuk setiap sampel.

Setelah logging, hitung:

```matlab
dt = diff(t);
[min(dt) median(dt) max(dt)]
```

Jangan menganggap `pause(0.05)` berarti semua sampel tepat 50 ms.

## Logging CSV
Simpan data sebagai table dengan nama kolom dan satuan yang jelas, misalnya `time_s` dan `voltage_V`. Raw data dipertahankan untuk audit.

## Kalibrasi linear
Dua titik referensi dapat digunakan untuk model:

```text
y = m*x + b
m = (y2-y1)/(x2-x1)
b = y1-m*x1
```

P7 memperkenalkan konsep ini agar P9 tidak langsung menganggap tegangan analog identik dengan besaran fisik.

## Filtering dasar
Moving average dapat dibandingkan dengan raw data:

```matlab
v_ma = movmean(v,5);
```

Filter tidak menggantikan raw data dan dapat menambah delay.

## Program wajib
```text
examples/led_adc.m
examples/adc_to_temperature_example.m
examples/connection_check.m
examples/adc_logger.m
examples/adc_calibration.m
```

Urutan belajar: connection check -> I/O dasar -> logging -> statistik sample interval -> kalibrasi -> filtering.

## Troubleshooting
- board tidak terdeteksi: cek Support Package, port, kabel data, dan aplikasi lain yang memakai port;
- data tidak berubah: periksa pin/configuration trainer dan range input low-voltage;
- plot lambat: log dahulu, plot setelah sampling bila perlu;
- port berubah: verifikasi kembali setelah reconnect.

## Catatan eksperimen
Setiap laporan mencantumkan board, port, pin, satuan, durasi, jumlah sampel, median sample interval, serta konfigurasi kalibrasi.

## Jembatan ke P8/P9
P8 menguji pemahaman P1–P7 dan kesiapan trainer low-voltage. P9 melanjutkan MATLAB–Arduino pada eksperimen temperatur sehingga koneksi, scaling, dan logging P7 harus sudah benar.
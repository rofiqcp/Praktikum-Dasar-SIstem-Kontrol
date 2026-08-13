# Pertemuan 7 — Pengenalan MATLAB–Arduino: LED dan ADC

## Tujuan
Memastikan toolchain MATLAB–Arduino berfungsi sebelum kontrol plant nyata.

## 1. MATLAB Support Package
Install **MATLAB Support Package for Arduino Hardware**.

Object:
```matlab
a = arduino('COM5','Mega2560');
```

Jika autodetect bekerja:
```matlab
a = arduino();
```

## 2. Digital output
LED built-in D13:
```matlab
writeDigitalPin(a,'D13',1);
```

## 3. Analog input
Potensiometer A1:
```matlab
v = readVoltage(a,'A1');
```

Arduino Mega ADC 10-bit secara hardware, tetapi Support Package mengembalikan tegangan.

## 4. Sampling host
MATLAB berjalan di PC, sehingga timing tidak se-deterministik loop MCU. P7 fokus I/O dan visualisasi, bukan PID cepat.

## 5. Eksperimen
- blink;
- duty sederhana dengan pause;
- baca A1;
- plot 10 s;
- konversi voltage ke persen.

## Program
`examples/matlab_arduino_led_adc.m`.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **MATLAB-Arduino LED/ADC**. Program yang harus dibuka dan dipahami:
- `examples/matlab_arduino_led_adc.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
D13 dapat dikendalikan dan A1 menghasilkan grafik tegangan 0–5 V sesuai posisi potensiometer.

## Validasi dan troubleshooting
Jika Arduino tidak terdeteksi, cek support package, board Mega2560, kabel data dan port yang tidak sedang dipakai aplikasi lain.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

# Jobsheet Pertemuan 10

## A. Upload sketch
`examples/arduino_encoder_stream/arduino_encoder_stream.ino`.

## B. Tentukan CPR
1. reset count;
2. putar tepat 1 revolusi;
3. baca count;
4. ulangi 3x;
5. tetapkan CPR.

## C. Arah
Putar CW/CCW. Verifikasi signed.

## D. MATLAB
```matlab
matlab_monitor_encoder
```

## E. Motor
Setelah pembacaan tangan benar, baru hidupkan motor dengan driver/PWM rendah.

## Data wajib
count, position_deg, rpm_raw, rpm_MA, rpm_LPF.

## Pertanyaan
- mengapa RPM raw noisy?
- bagaimana Ts mempengaruhi resolusi?
- apa pengaruh gearbox?

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
Count dan posisi bertanda benar; raw/MA/LPF RPM berubah sesuai arah dan kecepatan.

## Troubleshooting wajib dipahami
Jika arah salah, verifikasi kanal A/B dan konvensi mekanik; jangan membalik tanda di satu bagian saja tanpa audit jalur kontrol.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

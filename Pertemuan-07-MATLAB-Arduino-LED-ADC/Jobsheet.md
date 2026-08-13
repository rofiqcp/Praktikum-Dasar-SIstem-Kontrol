# Jobsheet Pertemuan 7

## Wiring potensiometer
5V—pot—GND, wiper ke A1.

## Langkah
1. Tentukan port.
2. Jalankan script.
3. LED harus blink.
4. Putar potensiometer.
5. Grafik tegangan berubah.
6. Verifikasi 0–5 V secara wajar.

## Modifikasi
Tambahkan threshold:
- A1 > 2.5 V → D13 ON;
- selain itu OFF.

## Hasil
Screenshot Arduino connection dan plot ADC.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
D13 dapat dikendalikan dan A1 menghasilkan grafik tegangan 0–5 V sesuai posisi potensiometer.

## Troubleshooting wajib dipahami
Jika Arduino tidak terdeteksi, cek support package, board Mega2560, kabel data dan port yang tidak sedang dipakai aplikasi lain.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

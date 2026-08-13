# Jobsheet Pertemuan 9

## A. Sensor
Jalankan pembacaan A0 tanpa heater. Bandingkan dengan thermometer referensi.

Catat minimal 3 titik kalibrasi.

## B. SSR dummy
Sebelum heater aktual, gunakan LED/dummy input SSR. Pastikan script STOP mematikan D8.

## C. PID MATLAB host
Edit:
- COM;
- Kp/Ki/Kd;
- SP;
- `MAX_TEMP_C`.

Run:
```matlab
matlab_temp_pid_host
```

## D. Variasi
Lakukan P, PI, PID. Jangan ubah terlalu banyak parameter sekaligus.

## E. Analisis
CSV dan PNG disimpan otomatis. Gunakan `shared/matlab/response_metrics.m`.

## Pertanyaan
1. Mengapa window SSR jauh lebih lambat daripada PWM motor?
2. Apa yang terjadi bila sensor membaca NaN?
3. Mengapa PID host tidak cocok untuk loop motor cepat?
4. Bandingkan Autonics vs Arduino Mega.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
PV mengikuti SP dengan SSR time-proportional dan data eksperimen tersimpan.

## Troubleshooting wajib dipahami
Mulai dengan heater dummy/low-voltage. Jangan menaikkan setpoint sebelum sensor dan batas maksimum terverifikasi.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

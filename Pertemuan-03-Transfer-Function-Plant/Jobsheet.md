# Jobsheet Pertemuan 3

## A. Pemanas air
1. Jalankan model orde satu.
2. Variasikan K dan tau.
3. Catat pengaruh ke nilai akhir dan kecepatan respon.

## B. Motor speed
1. Jalankan step response.
2. Ubah J dua kali lebih besar.
3. Bandingkan rise time.

## C. Motor position
Jelaskan mengapa posisi tidak mempunyai steady-state seperti speed untuk input tegangan step tanpa controller.

## D. Simulink
Jalankan `build_three_plants_simulink.m`, buka `.slx`, jalankan simulation.

## Hasil
- tiga transfer function;
- pole;
- grafik;
- tabel variasi parameter;
- file `.slx` hasil builder.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
Tiga model tampil dengan pole dan step response; builder menghasilkan model Simulink di folder models.

## Troubleshooting wajib dipahami
Jika `tf` atau `stepinfo` tidak dikenal, cek Control System Toolbox. Pastikan satuan parameter konsisten.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

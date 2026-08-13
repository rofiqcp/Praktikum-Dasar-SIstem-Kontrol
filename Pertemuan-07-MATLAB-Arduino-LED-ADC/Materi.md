# Pertemuan 07 — Pengenalan MATLAB–Arduino — Download, LED, dan Baca ADC


## Tujuan
Menyiapkan Arduino Support Package, menghubungkan MATLAB ke Arduino Mega 2560, mengendalikan LED/digital output, membaca ADC A0, dan membuat plot real-time.

## Dua pola penggunaan
1. **MATLAB Support Package / connected I/O:** command dieksekusi dari MATLAB melalui object `arduino`.
2. **Firmware serial bridge:** logic real-time berjalan di Arduino, MATLAB hanya memberi command/logging. Pola kedua dipakai pada praktikum motor karena timing encoder lebih aman dikerjakan oleh interrupt di MCU.

## ADC Mega
ADC 10-bit menghasilkan 0…1023 untuk tegangan referensi yang digunakan board. Fungsi support package `readVoltage` mengembalikan tegangan sehingga lebih mudah dikalibrasi.

## Sampling
Loop PC tidak real-time keras. Ukur waktu dengan `tic/toc` dan jangan mengasumsikan `pause(0.01)` selalu tepat 10 ms. Untuk PID cepat, pindahkan controller ke MCU (P13–P15).

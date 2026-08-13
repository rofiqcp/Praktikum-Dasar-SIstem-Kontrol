# Prompt AI contoh P13

> Saya menggunakan Arduino Mega 2560 + PlatformIO. Pin encoder A=D2, B=D3, ADC=A1. Buat quadrature decoder signed yang aman untuk ISR. Jangan gunakan Serial, String, delay, malloc di ISR. Buat main loop non-blocking. Hitung position degree dan RPM berdasarkan COUNTS_PER_REV yang dapat saya kalibrasi. Tambahkan moving average dan LPF. Serial 115200 CSV. Command ZERO, TS 10..300 ms, ALPHA 0..1, MA 1..16, STATUS. Output saat boot harus pasif. Setelah memberi kode, audit race condition, overflow, dan pembagian integer.

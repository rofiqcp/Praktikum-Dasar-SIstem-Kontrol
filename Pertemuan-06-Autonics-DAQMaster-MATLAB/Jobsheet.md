# Jobsheet Pertemuan 6

## A. Connect DAQMaster
Catat:
- model controller;
- unit address;
- baud;
- parity;
- stop bit;
- converter.

Ambil screenshot PV/SV.

## B. Logging
Pilih cycle logging yang masuk akal untuk plant termal (misalnya 0.5–2 s, mengikuti kemampuan setup).

Simpan CSV.

## C. MATLAB
```matlab
analyze_daqmaster('hasil.csv')
```

Output:
- graph;
- metrics;
- file PNG.

## D. Python alternatif
```bash
python examples/analyze_daqmaster.py hasil.csv
```

## E. Analisis
Bandingkan data manual P5 dengan DAQ P6: sampling, peak, settling, jumlah data, error operator.

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
CSV DAQMaster dapat dibaca dan menghasilkan grafik/metrik yang bisa dibandingkan dengan P5.

## Troubleshooting wajib dipahami
Jika kolom tidak terbaca, ekspor CSV sederhana dan identifikasi nama kolom time/PV/SV. Samakan baud/parity/address dengan controller.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

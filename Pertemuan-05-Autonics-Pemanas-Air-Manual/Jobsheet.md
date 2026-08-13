# Jobsheet Pertemuan 5

## Persiapan
- [ ] volume air dicatat;
- [ ] suhu awal dicatat;
- [ ] sensor terpasang;
- [ ] setpoint diset aman;
- [ ] stopwatch siap;
- [ ] template Excel dibuka;
- [ ] emergency disconnect diketahui.

## A. ON/OFF
Set SV, kemudian lakukan tiga hysteresis berbeda.

Setiap run:
1. tunggu kondisi awal yang ditetapkan;
2. start stopwatch saat control RUN;
3. catat PV setiap 10 s;
4. lanjutkan sampai steady atau waktu maksimum dosen;
5. STOP;
6. simpan file berbeda.

## B. PID
Lakukan minimal:
- P;
- PI;
- PID.

Catat parameter persis.

## C. Analisis
Ekspor sheet menjadi CSV dengan kolom yang kompatibel:

```text
time_s,setpoint_C,temp_C
```

Jalankan:

```bash
python examples/analyze_manual_data.py data.csv
```

## Tabel perbandingan
Run, mode, HYS/Kp/Ki/Kd, rise, overshoot, settling, SSE.

## Pertanyaan
1. Hysteresis mana yang paling stabil?
2. Apa tradeoff hysteresis vs frekuensi switching?
3. Apa pengaruh Ki?
4. Apakah suhu awal mempengaruhi fairness perbandingan?
5. Apakah sampling manual 10 s cukup menangkap peak?

## Bukti yang harus dikumpulkan
- screenshot/terminal bahwa program utama benar-benar dijalankan;
- source/model yang digunakan;
- tabel parameter dan satuan;
- grafik atau output pengukuran;
- minimal satu variasi parameter dan analisisnya;
- kesimpulan yang menghubungkan teori dengan hasil.

## Expected result
Tabel stopwatch lengkap, grafik PV-SV dan metrik respons tersedia.

## Troubleshooting wajib dipahami
Jangan mengubah volume air/daya heater di tengah perbandingan. Catat kondisi awal dan interval stopwatch.

## Pertanyaan sebelum selesai
1. Variabel apa yang menjadi setpoint, process value, error dan control output pada percobaan ini?
2. Apa satuan setiap sinyal utama?
3. Bagian mana yang paling membatasi akurasi/respons?
4. Bagaimana Anda membuktikan hasil bukan kebetulan atau salah skala?
5. Apa kondisi aman yang harus terjadi bila program dihentikan?

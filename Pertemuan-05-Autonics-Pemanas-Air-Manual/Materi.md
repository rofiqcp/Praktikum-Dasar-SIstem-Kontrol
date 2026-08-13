# Pertemuan 05 — Autonics TK4S + Pemanas Air: Pengambilan Data Manual Stopwatch

## Capaian Pembelajaran
- mengoperasikan controller TK4S pada plant pemanas air
- mencatat data manual dengan stopwatch
- membandingkan ON-OFF hysteresis dan PID
- mengolah data eksperimen di Excel/Python

## Materi Inti

Plant suhu diganti menjadi **pemanas air**. Autonics TK4S-T4RN membaca PV temperatur dan mengendalikan heater melalui output kontrol/SSR. Pada pertemuan ini data diambil **manual** menggunakan stopwatch, lalu diketik ke Excel/CSV.

Eksperimen minimum:
1. open-loop/power fixed bila trainer mengizinkan;
2. ON-OFF dengan beberapa hysteresis;
3. PID/time proportional dengan beberapa parameter.

Kolom data: `time_s,setpoint_c,temp_c,output_percent,mode,kp,ki,kd,hysteresis_c`.


## Program yang Wajib Dijalankan
- `examples/template_manual_temperature.csv`
- `examples/analyze_manual_temperature.py`

## Alur Praktikum
1. Pastikan bak berisi air sesuai batas aman plant dan sensor terendam sesuai prosedur trainer.
2. Nyalakan controller tanpa menghubungkan mains secara terbuka.
3. Set suhu target contoh 50 °C.
4. Start stopwatch bersamaan saat percobaan dimulai.
5. Catat PV tiap 5 s atau 10 s pada template CSV/Excel.
6. Ulangi untuk minimal 3 nilai hysteresis.
7. Uji parameter P terlebih dahulu, lalu I, kemudian D secara bertahap.
8. Simpan CSV dan jalankan `examples/analyze_manual_temperature.py data.csv`.
9. Bandingkan overshoot, settling time, dan steady-state error.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.

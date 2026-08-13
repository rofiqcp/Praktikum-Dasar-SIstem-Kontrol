# Jobsheet Pertemuan 9 — MATLAB–Arduino PID Suhu

## Tujuan
Memvalidasi sensor temperatur, memahami PID diskrit yang dihitung di MATLAB, merekam seluruh komponen kontrol, dan membandingkan respons P, PI, dan PID menggunakan data kuantitatif pada trainer laboratorium yang telah disiapkan.

## Prasyarat
- P1–P7 telah selesai;
- MATLAB Support Package for Arduino Hardware tersedia;
- trainer dan sensor telah diverifikasi oleh instruktur;
- tahap awal dilakukan menggunakan simulasi atau dummy output.

## File yang digunakan
```text
examples/temperature_sensor_calibration.m
examples/temp_pid_offline_simulation.m
examples/matlab_temp_pid_host.m
examples/analyze_temp_pid_log.m
examples/build_temp_pid_simulink.m
```

## A. Pre-test
Jawab sebelum praktikum:
1. tuliskan persamaan `e = SP - PV`;
2. jelaskan fungsi komponen P, I, dan D;
3. jelaskan alasan output dibatasi 0–100%;
4. jelaskan integral windup;
5. jelaskan derivative-on-measurement;
6. bedakan sample time kontrol dengan window time-proportional.

## B. Audit data dan I/O
Catat:
- board yang digunakan;
- port komunikasi;
- pin sensor;
- pin command;
- tipe sensor;
- satuan pengukuran;
- rentang sensor;
- alat ukur temperatur referensi;
- batas operasi trainer yang ditetapkan instruktur.

## C. Kalibrasi sensor
Kumpulkan minimal tiga pasangan data `voltage_V` dan `reference_C`, kemudian jalankan:

```matlab
run('examples/temperature_sensor_calibration.m')
```

Catat slope, intercept, residual, dan rentang kalibrasi. Jangan lanjut ke pengujian PID bila skala temperatur belum masuk akal.

Program host P9 menyediakan konversi ideal LM35 sebagai baseline. Jika hasil kalibrasi berbeda, fungsi konversi pada `matlab_temp_pid_host.m` harus disesuaikan dengan hasil kalibrasi sebelum data digunakan sebagai PV.

## D. Simulasi offline
Jalankan:

```matlab
run('examples/temp_pid_offline_simulation.m')
```

Bandingkan empat konfigurasi:
- P;
- PI;
- PID;
- satu konfigurasi yang lebih agresif untuk bahan analisis.

Buat tabel Kp, Ki, Kd, rise time, overshoot, settling time, SSE, dan output kontrol maksimum.

## E. Verifikasi dummy output
Gunakan indikator atau dummy output pada trainer. Periksa secara visual bahwa perintah 0%, sekitar 50%, dan 100% menghasilkan proporsi waktu aktif yang sesuai. Pastikan penghentian program mengembalikan command ke kondisi aman sesuai prosedur trainer.

## F. Konfigurasi program
Buka `examples/matlab_temp_pid_host.m` dan dokumentasikan parameter berikut:

```text
PORT, SP, KP, KI, KD, TS, WINDOW_S, MAX_TEMP_C, RUN_TIME_S
```

Pastikan fungsi konversi sensor sesuai dengan sensor yang digunakan. Konversi `voltage*100` hanya merupakan baseline untuk karakteristik sensor tertentu dan tidak boleh dianggap berlaku untuk semua sensor.

## G. Pengujian P
Gunakan `Ki=0` dan `Kd=0`. Simpan:
- CSV;
- PNG;
- response metrics;
- temperatur awal;
- sample time nominal;
- parameter controller.

## H. Pengujian PI
Pertahankan kondisi pengujian semirip mungkin dengan pengujian P, lalu tambahkan Ki secara bertahap. Analisis perubahan SSE, overshoot, dan komponen integral.

## I. Pengujian PID
Tambahkan Kd hanya bila data menunjukkan kebutuhan damping. Analisis apakah komponen D memperbaiki respons atau justru memperbesar pengaruh noise pengukuran.

## J. Analisis CSV
`examples/analyze_temp_pid_log.m` otomatis mencari file `temp_*.csv` terbaru pada folder `examples/output`. Jalankan:

```matlab
run('examples/analyze_temp_pid_log.m')
```

Grafik minimal yang dianalisis:
1. SP dan PV;
2. error;
3. P, I, dan D;
4. output PID dalam persen;
5. status command.

## K. Tabel perbandingan
| Parameter | P | PI | PID |
|---|---:|---:|---:|
| temperatur awal | | | |
| SP | | | |
| Kp | | | |
| Ki | | | |
| Kd | | | |
| Ts | | | |
| window | | | |
| rise time | | | |
| overshoot | | | |
| settling time | | | |
| SSE | | | |
| output maksimum | | | |

Jika kondisi awal berbeda jauh, tuliskan keterbatasan tersebut dan jangan membandingkan metrik seolah-olah semua run memiliki kondisi yang sama.

## L. Perbandingan dengan P5/P6
Pilih satu run Autonics dari P5/P6 dengan kondisi yang paling mendekati P9. Bandingkan:
- response metrics;
- kualitas logging;
- keterlihatan algoritma;
- timing controller;
- kemudahan perubahan parameter.

Jangan menyimpulkan salah satu platform selalu lebih baik. Jelaskan kelebihan dan keterbatasannya sesuai tujuan implementasi.

## M. Review source
Praktikan harus mampu menunjukkan bagian program yang:
- membaca sensor;
- mengubah pembacaan sensor menjadi PV;
- menghitung error;
- menghitung P, I, dan D;
- melakukan anti-windup;
- membatasi output;
- membentuk command time-proportional;
- melakukan cleanup ketika program berhenti.

## Pertanyaan analisis
1. Mengapa output pemanas hanya berada pada rentang 0–100%?
2. Mengapa overshoot pada plant termal dapat turun secara lambat?
3. Mengapa kontrol dari host MATLAB masih sesuai untuk praktikum termal, tetapi tidak dapat dianggap hard real-time?
4. Mengapa Ki dapat memperkecil SSE tetapi juga meningkatkan overshoot?
5. Pada kondisi apa Kd tidak memberikan manfaat yang berarti?
6. Mengapa kalibrasi sensor harus dilakukan sebelum tuning?
7. Apa perbedaan `TS` nominal dengan interval sampling aktual?
8. Mengapa raw CSV harus tetap disimpan?
9. Apa kelebihan Autonics dibanding MATLAB–Arduino dan sebaliknya?
10. Bukti apa yang menunjukkan hasil eksperimen dapat direproduksi?

## Deliverable
```text
NIM_Nama_P09/
  source/
  raw/
  results/
  screenshots/
  laporan.pdf
```

Minimal berisi:
- data kalibrasi;
- hasil pengujian P, PI, dan PID;
- grafik;
- response metrics;
- tabel perbandingan;
- source yang digunakan;
- kesimpulan berbasis data.

## Expected result
Mahasiswa mampu menjelaskan rantai `sensor -> PV -> error -> PID -> output terbatas`, menunjukkan tiga pengujian yang terdokumentasi, dan memilih parameter kontrol berdasarkan data eksperimen.

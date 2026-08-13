# Tugas Video Pertemuan 11 — PID Kecepatan Motor DC

## Tujuan
Membuktikan bahwa mahasiswa memahami closed-loop kecepatan dari setpoint sampai feedback encoder dan mampu menilai kualitas respons menggunakan data, bukan hanya menunjukkan motor berputar.

## Struktur wajib video

### 1. Pembukaan
Tampilkan nama/NIM, tujuan P11, dan diagram blok:

```text
SP RPM -> error -> PID -> output bertanda -> motor -> encoder -> RPM terfilter -> PV
```

Jelaskan hubungan P10 dengan P11 dan alasan CPR serta tanda RPM harus sudah benar sebelum PID digunakan.

### 2. Feedback kecepatan
Jelaskan:
- count encoder;
- delta count;
- sample interval;
- perhitungan RPM;
- moving average;
- low-pass filter;
- pengaruh filter terhadap noise dan keterlambatan.

### 3. PID diskrit
Jelaskan persamaan yang digunakan:

```text
P = Kp*e
I_candidate = I + Ki*e*dt
D = -Kd*(PV-PVprev)/dt
u = sat(P+I+D)
```

Jelaskan derivative-on-measurement, saturasi output, dan conditional anti-windup.

### 4. Source review
Buka `examples/arduino_speed_pid/arduino_speed_pid.ino` dan tunjukkan bagian yang menangani:
- encoder;
- RPM terfilter;
- error;
- P/I/D;
- anti-windup;
- batas output;
- arah output positif dan negatif;
- RUN/STOP;
- heartbeat/host timeout;
- telemetry.

### 5. MATLAB supervisor/logger
Buka `examples/matlab_speed_pid_experiment.m` dan jelaskan fungsi MATLAB sebagai pengirim parameter sekaligus pencatat data. Tunjukkan kolom telemetry yang disimpan ke CSV.

### 6. P, PI, dan PID
Tampilkan minimal tiga konfigurasi:
- P;
- PI;
- PID atau PD bila Kd digunakan untuk damping.

Untuk setiap konfigurasi sebutkan Kp, Ki, Kd, batas output, CPR, sample interval, dan kondisi beban.

### 7. Respons arah positif dan negatif
Tampilkan minimal satu respons setpoint positif dan satu respons setpoint negatif. Jangan menyimpulkan kontrol dua arah sudah benar hanya karena encoder dapat membaca RPM negatif.

Bandingkan:
- rise time;
- settling time;
- overshoot;
- steady-state error;
- output maksimum;
- kecenderungan saturasi.

### 8. Analisis data
Gunakan `ANALISIS_DATA.md` dan jalankan `examples/analyze_speed_pid_log.m` pada data yang sesuai. Tampilkan:
- SP vs RPM;
- error;
- P/I/D;
- output controller;
- bagian yang mengalami saturasi.

### 9. Uji kondisi berhenti
Jelaskan fungsi STOP dan host timeout. Tunjukkan bukti bahwa sistem kembali ke state berhenti ketika eksperimen selesai atau komunikasi supervisor dihentikan sesuai prosedur trainer laboratorium.

### 10. Kesimpulan
Sebutkan:
- konfigurasi yang memberikan hasil paling layak menurut data;
- perbedaan respons arah positif dan negatif;
- pengaruh filter;
- pengaruh saturasi;
- satu keterbatasan eksperimen;
- satu perbaikan yang akan dilakukan pada pengujian berikutnya.

## Bukti yang harus tersedia
- source firmware dan MATLAB terlihat di video;
- data mentah CSV;
- grafik hasil analisis;
- tabel P/PI/PID;
- parameter CPR, sample interval, Kp, Ki, Kd, dan batas output;
- data arah positif dan negatif;
- penjelasan anti-windup;
- penjelasan STOP/host timeout;
- kesimpulan berdasarkan metrik.

## File pendamping
```text
NIM_Nama_P11/
  source/
  raw/
  results/
  screenshots/
  video_link.txt
```

## Rubrik
| Aspek | Bobot |
|---|---:|
| pemahaman feedback dan filter | 15% |
| pemahaman PID dan anti-windup | 20% |
| penjelasan source dan telemetry | 20% |
| bukti eksperimen dua arah | 15% |
| analisis data dan response metrics | 20% |
| kesimpulan dan keterbatasan | 10% |

## Kesalahan yang mengurangi nilai
- hanya menunjukkan motor berputar tanpa data;
- tidak menunjukkan arah negatif;
- tidak mencantumkan CPR atau sample interval;
- mengubah beberapa parameter sekaligus tanpa penjelasan;
- menyebut tuning terbaik tanpa metrik;
- mengabaikan saturasi;
- tidak menjelaskan anti-windup;
- tidak menyimpan CSV atau grafik hasil analisis.

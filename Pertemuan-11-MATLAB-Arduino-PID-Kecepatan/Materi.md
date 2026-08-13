# Pertemuan 11 — MATLAB–Arduino PID Kecepatan Motor DC

## Capaian pembelajaran
Mahasiswa mampu membentuk kontrol kecepatan closed-loop dari feedback P10, menjelaskan setpoint bertanda, PID diskrit, filtering, saturasi, anti-windup, heartbeat, state berhenti, tuning P/PI/PID, dan menganalisis respons dua arah.

## 1. Syarat dari P10
P11 dimulai hanya setelah:
- CPR terverifikasi;
- count dan posisi mempunyai tanda yang konsisten;
- RPM positif dan negatif dapat dibaca;
- perbedaan RPM raw, moving average, dan LPF dipahami.

Kesalahan feedback tidak boleh ditutupi dengan tuning gain. Jika CPR atau tanda salah, controller akan menerima informasi plant yang salah.

## 2. Struktur loop

```text
SP_rpm -> error -> PID -> output bertanda -> plant motor -> encoder -> filter RPM -> PV
```

Error:

```text
e[k] = SP[k] - PV[k]
```

Output controller dibatasi oleh `MAXPWM` pada arah positif maupun negatif.

## 3. Output bertanda dan konvensi arah
Konvensi arah firmware harus sama dengan konvensi encoder pada P10. Kemampuan sensor membaca RPM negatif belum membuktikan bahwa closed-loop arah negatif sudah benar.

Audit arah dilakukan secara berurutan:

```text
setpoint -> error -> output PID -> arah respons plant -> encoder count -> tanda RPM
```

Jika salah satu tahap menggunakan konvensi berbeda, sistem dapat gagal pada satu arah walaupun sensor tampak bekerja.

## 4. Feedback kecepatan
Firmware menghitung:
1. perubahan count;
2. RPM mentah;
3. moving average;
4. low-pass filter;
5. RPM terfilter sebagai PV PID.

Parameter yang wajib dicatat:

```text
COUNTS_PER_REV
SAMPLE_MS
moving-average window
LPF alpha
```

Nilai `COUNTS_PER_REV` pada contoh harus disesuaikan dengan hasil verifikasi P10.

## 5. PID diskrit

```text
P = Kp*e
I_candidate = I + Ki*e*dt
D = -Kd*(PV-PVprev)/dt
u = sat(P+I+D)
```

Komponen D menggunakan derivative-on-measurement sehingga perubahan setpoint tidak langsung menimbulkan derivative kick sebesar derivative-on-error.

### Interpretasi
- `Kp` menentukan kuatnya koreksi terhadap error saat ini;
- `Ki` mengakumulasi error dan membantu mengurangi steady-state error;
- `Kd` memberi efek peredaman terhadap perubahan feedback;
- `u` dibatasi agar sesuai dengan rentang output yang digunakan pada eksperimen.

## 6. Anti-windup
Integral tidak selalu diperbarui. Firmware menggunakan conditional integration.

Integral diperbarui jika:
- output sebelum saturasi masih berada di dalam batas; atau
- error membantu membawa output kembali dari kondisi saturasi.

Integral ditahan jika output sudah mencapai batas dan error masih mendorong lebih jauh ke arah batas tersebut.

Mahasiswa wajib dapat menunjukkan bagian implementasi ini pada source firmware dan menghubungkannya dengan grafik term I.

## 7. Saturasi
`MAXPWM` menjadi batas output eksperimen.

Jika terlalu kecil:
- target mungkin tidak tercapai;
- error dapat menetap besar;
- output dapat terus berada pada batas.

Jika terlalu besar:
- respons dapat menjadi lebih agresif;
- overshoot dapat meningkat;
- perbedaan mekanik dua arah dapat semakin terlihat.

Tuning harus dibaca bersama grafik output agar kondisi saturasi tidak tersembunyi.

## 8. Arsitektur MATLAB–Arduino
Pada P11 PID dihitung di Arduino. MATLAB berfungsi sebagai supervisor dan logger:
- mengirim setpoint dan parameter;
- membaca telemetry;
- menyimpan CSV;
- membuat grafik;
- menghitung response metrics.

Arsitektur ini berbeda dengan P9, ketika PID dihitung di MATLAB. Perbedaan ini penting karena timing loop P11 lebih banyak ditentukan oleh firmware.

## 9. Heartbeat dan state berhenti
Firmware mempunyai host timeout. Jika heartbeat hilang ketika sistem sedang berada pada state RUN, output dikembalikan ke kondisi berhenti dan status timeout dilaporkan melalui serial.

MATLAB juga menggunakan mekanisme cleanup untuk mengembalikan eksperimen ke state berhenti ketika script selesai atau dihentikan.

Tujuannya adalah membuat state kontrol eksplisit dan dapat diaudit dari source maupun telemetry.

## 10. Telemetry

```text
#PROTO,SPEED_PID,1
#ms,sp,rpm,error,P,I,D,pid_pwm,count
```

Sembilan kolom tersebut memungkinkan audit terhadap:
- SP;
- PV/RPM;
- error;
- P, I, dan D;
- output PID;
- encoder count.

Urutan dan satuan kolom harus konsisten antara firmware, MATLAB logger, analyzer, dan laporan.

## 11. Tuning bertahap
### P
Set `Ki=0` dan `Kd=0`. Amati tracking, steady-state error, dan saturasi.

### PI
Tambahkan Ki secara bertahap. Amati perubahan SSE, overshoot, dan akumulasi integral.

### PID
Tambahkan Kd hanya bila data menunjukkan kebutuhan peredaman. Filtering RPM menambah keterlambatan sehingga Kd tidak selalu memperbaiki hasil.

Ubah satu kelompok parameter dalam satu waktu dan simpan metadata lengkap untuk setiap dataset.

## 12. Respons positif dan negatif
Minimal bandingkan satu step positif dan satu step negatif dengan besar setpoint yang sebanding.

Profil yang dapat digunakan untuk latihan analisis:

```text
0 -> +SP -> 0 -> -SP -> 0
```

Response metrics dihitung per segmen setpoint, bukan satu kali untuk seluruh profil multi-setpoint.

## 13. Asimetri arah
Respons positif dan negatif dapat berbeda karena:
- friction;
- backlash gearbox;
- karakteristik driver;
- supply;
- kondisi beban;
- perbedaan mekanik dua arah.

Karena itu kedua arah harus dilaporkan sebelum menyimpulkan bahwa controller telah bekerja dengan baik.

## 14. Simulasi
Jalankan terlebih dahulu:

```matlab
run('examples/speed_pid_simulation.m')
```

Kemudian builder Simulink:

```matlab
run('examples/build_motor_speed_pid_simulink.m')
```

Simulasi digunakan untuk memahami gain, saturasi, anti-windup, dan bentuk respons sebelum menganalisis data plant.

## 15. Analisis log

```matlab
run('examples/analyze_speed_pid_log.m')
```

Analisis minimum:
- SP dan RPM;
- error;
- P, I, dan D;
- output PID;
- jumlah sampel arah positif dan negatif;
- interval sampling;
- output absolut maksimum;
- kondisi saturasi;
- response metrics untuk segmen yang jelas.

Gunakan `ANALISIS_DATA.md` untuk tabel perbandingan dan pertanyaan analisis yang lebih lengkap.

## 16. Troubleshooting dari ujung ke ujung
### Feedback benar tetapi salah satu arah tidak mengikuti SP
Audit tanda pada SP, error, output PID, respons plant, encoder count, dan RPM.

### Target sulit tercapai
Periksa saturasi, beban/friction, CPR, dan batas output sebelum mengubah semua gain.

### RPM terlalu berfluktuasi
Audit count mentah, CPR, interval sampling, moving average, LPF, dan keterlambatan filter.

### Overshoot besar setelah saturasi
Audit Ki, kondisi integral, dan conditional anti-windup.

### Sistem berhenti tidak terduga
Periksa timestamp dan pesan timeout pada telemetry.

## 17. Program wajib

```text
examples/arduino_speed_pid/arduino_speed_pid.ino
examples/matlab_speed_pid_experiment.m
examples/matlab_speed_pid_profile.m
examples/speed_pid_simulation.m
examples/analyze_speed_pid_log.m
examples/build_motor_speed_pid_simulink.m
```

`examples/pid_speed_matlab.m` dipertahankan hanya sebagai compatibility entry point agar tautan materi lama tetap bekerja. Workflow resmi P11 menggunakan `matlab_speed_pid_experiment.m`.

Urutan belajar:

```text
validasi feedback P10
-> simulasi offline
-> review source
-> P
-> PI
-> PID/PD
-> respons positif dan negatif
-> analisis per segmen
-> kesimpulan berbasis metrik
```

## 18. Parameter laporan
Catat:
- CPR;
- interval sampling;
- Kp, Ki, Kd;
- `MAXPWM`;
- SP;
- parameter filter;
- kondisi beban;
- rise time;
- settling time;
- overshoot;
- SSE;
- output absolut maksimum;
- hasil arah positif dan negatif;
- kejadian timeout bila ada.

## 19. Jembatan ke P12
P11 mengontrol kecepatan. P12 menggunakan encoder count sebagai dasar posisi, menambahkan referensi nol, dan mempertahankan konsep output bertanda, saturasi, anti-windup, telemetry, logging, dan response metrics.

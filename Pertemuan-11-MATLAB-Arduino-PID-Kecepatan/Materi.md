# Pertemuan 11 — MATLAB–Arduino PID Kecepatan Motor DC

## Capaian pembelajaran
Mahasiswa mampu membentuk closed-loop speed dari feedback P10, menjelaskan signed setpoint, PID diskrit, filtering, saturation, anti-windup, heartbeat, STOP, tuning P/PI/PID, dan menganalisis respon dua arah.

## 1. Gate dari P10
P11 dimulai hanya setelah:
- CPR terverifikasi;
- count dan posisi memiliki tanda konsisten;
- RPM positif/negatif terbaca;
- raw/MA/LPF dipahami.

Kesalahan feedback tidak boleh ditutup dengan tuning gain.

## 2. Struktur loop

```text
SP_rpm -> error -> PID -> signed control -> plant motor -> encoder -> RPM filter -> PV
```

Error:

```text
e[k] = SP[k]-PV[k]
```

Output controller baseline dibatasi oleh `MAXPWM` dalam arah positif maupun negatif.

## 3. Signed control dan konvensi arah
Konvensi arah firmware harus sama dengan konvensi encoder P10. Sensor mampu membaca RPM negatif belum membuktikan closed-loop arah negatif sudah benar. Audit harus dilakukan dari setpoint, error, output PID, respons plant, sampai tanda RPM.

## 4. Feedback speed
Firmware menghitung:
1. delta count;
2. raw RPM;
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

CPR contoh harus disesuaikan dengan hasil P10.

## 5. PID diskrit

```text
P = Kp*e
I_candidate = I + Ki*e*dt
D = -Kd*(PV-PVprev)/dt
u = sat(P+I+D)
```

Derivative-on-measurement mengurangi derivative kick saat SP berubah.

## 6. Anti-windup
Integral ditahan bila candidate output sudah saturasi dan error masih mendorong lebih jauh ke saturation. Integral boleh berubah bila output belum saturasi atau error membantu controller kembali ke range valid.

Mahasiswa wajib menunjukkan implementasi ini di source firmware.

## 7. Saturation
`MAXPWM` menjadi batas eksperimen. Bila terlalu kecil, target dapat tidak tercapai; bila terlalu besar, respon menjadi lebih agresif. Tuning harus dibaca bersama grafik output sehingga saturation tidak tersembunyi.

## 8. Arsitektur MATLAB–Arduino
Pada P11 PID dihitung di Arduino. MATLAB bertindak sebagai supervisor/logger:
- mengirim gain dan setpoint;
- RUN/STOP;
- heartbeat;
- membaca telemetry;
- membuat grafik;
- menyimpan CSV/PNG;
- menghitung metrics.

Ini berbeda dengan P9, ketika PID dihitung di MATLAB host.

## 9. Heartbeat dan STOP
Firmware mempunyai host timeout. Jika heartbeat hilang ketika RUN, control output kembali ke kondisi stop dan status fault dikirim melalui serial. MATLAB juga memakai cleanup agar mencoba mengirim STOP saat script berakhir.

Tujuannya adalah membuat state control eksplisit dan dapat diaudit.

## 10. Telemetry

```text
#PROTO,SPEED_PID,1
#ms,sp,rpm,error,P,I,D,pid_pwm,count
```

Sembilan kolom tersebut memungkinkan audit SP, PV, error, P/I/D, output, dan encoder count.

## 11. Tuning bertahap
### P
Set Ki=0 dan Kd=0. Amati tracking, error residual, dan saturation.

### PI
Tambahkan Ki kecil. Amati SSE, overshoot, dan akumulasi integral.

### PID
Tambahkan Kd hanya bila data menunjukkan kebutuhan damping. Filtering RPM dapat menambah delay sehingga Kd tidak selalu memperbaiki hasil.

Ubah satu kelompok parameter secara terstruktur dan simpan setiap run dengan metadata lengkap.

## 12. Positive dan negative response
Minimal bandingkan satu step positif dan satu step negatif. Profile yang direkomendasikan untuk analisis:

```text
0 -> +SP -> 0 -> -SP -> 0
```

Hitung response metrics per segment, bukan satu kali untuk seluruh multi-setpoint profile.

## 13. Asimetri arah
Respon positif dan negatif dapat berbeda karena friction, gearbox, driver, supply, atau load. Laporkan kedua arah sebelum menyimpulkan controller sudah baik.

## 14. Simulasi
Jalankan terlebih dahulu:

```matlab
run('examples/speed_pid_simulation.m')
```

Kemudian builder Simulink:

```matlab
run('examples/build_motor_speed_pid_simulink.m')
```

Simulasi dipakai untuk memahami gain, saturation, dan anti-windup sebelum membaca data plant.

## 15. Analisis log

```matlab
run('examples/analyze_speed_pid_log.m')
```

Analisis minimal:
- SP vs RPM;
- error;
- P/I/D;
- output PID;
- persentase sample yang saturated;
- jumlah sample RPM positif/negatif;
- satu response metric segment yang jelas.

## 16. Troubleshooting end-to-end
### Feedback benar tetapi salah satu arah tidak mengikuti SP
Audit sign pada SP, error, PID output, arah plant, encoder count, dan RPM.

### Target sulit tercapai
Periksa saturation, load/friction, CPR, dan limit output sebelum mengubah semua gain.

### RPM noisy
Audit raw count, CPR, sample time, moving average, LPF, dan delay filter.

### Overshoot besar setelah saturation
Audit Ki serta conditional anti-windup.

### Sistem berhenti tidak terduga
Periksa telemetry untuk event host timeout.

## 17. Program wajib

```text
examples/arduino_speed_pid/arduino_speed_pid.ino
examples/matlab_speed_pid_experiment.m
examples/matlab_speed_pid_profile.m
examples/speed_pid_simulation.m
examples/analyze_speed_pid_log.m
examples/build_motor_speed_pid_simulink.m
```

Urutan belajar:

```text
P10 feedback gate
-> offline simulation
-> source review
-> P
-> PI
-> PID
-> positive/negative response
-> profile
-> metrics
```

## 18. Parameter laporan
- CPR;
- sample time;
- Kp/Ki/Kd;
- MAXPWM;
- SP;
- filter baseline;
- kondisi load;
- rise/settling/overshoot/SSE;
- maximum absolute output;
- hasil arah positif/negatif;
- event timeout bila ada.

## 19. Jembatan ke P12
P11 mengontrol kecepatan. P12 menggunakan encoder count sebagai posisi, menambahkan reference ZERO, dan mempertahankan konsep signed control, saturation, anti-windup, heartbeat, logging, dan response metrics.
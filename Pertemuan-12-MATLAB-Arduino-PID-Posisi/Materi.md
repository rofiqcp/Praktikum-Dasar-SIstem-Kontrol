# Pertemuan 12 — MATLAB–Arduino PID Posisi Motor DC

## Capaian pembelajaran
Mahasiswa mampu menjelaskan closed-loop posisi, reference zero, posisi unwrapped, error sudut, PID diskrit, saturation, anti-windup, derivative-on-measurement, telemetry, dan response metrics; serta menyusun project evidence P12 secara terstruktur.

## 1. Hubungan P10–P12
P10 menghasilkan feedback:

```text
encoder count -> position_deg
```

P11 menggunakan turunan count sebagai speed. P12 kembali menggunakan posisi langsung sebagai PV:

```text
SP_deg -> error -> PID -> plant -> encoder count -> position_deg -> PV
```

Karena posisi berasal dari count, CPR dan sign P10 harus sudah valid.

## 2. Position feedback
Baseline:

```text
position_deg = count / COUNTS_PER_REV * 360
```

Firmware P12 menggunakan posisi **unwrapped**, sehingga nilai dapat melewati ±360°. Ini menghindari diskontinuitas buatan di batas 0/360°.

## 3. Reference ZERO
Perintah `ZERO` pada firmware menetapkan current encoder count sebagai referensi nol software.

Hal penting:
- zero software bukan homing mekanik;
- zero bukan limit switch;
- zero tidak membuktikan ruang gerak mekanik aman;
- reference harus dicatat sebelum setiap dataset.

## 4. Error posisi

```text
e[k] = SP_deg[k] - position_deg[k]
```

Jika SP dan position menggunakan unwrapped coordinate yang sama, error tidak memerlukan wrapping tambahan.

Untuk sistem rotary 0–360° yang benar-benar membutuhkan shortest-path, error modular harus didefinisikan secara berbeda. Itu bukan baseline P12.

## 5. PID diskrit

```text
P = Kp*e
I_candidate = I + Ki*e*dt
D = -Kd*(position-position_prev)/dt
u = sat(P+I+D)
```

Derivative-on-measurement memberi damping berdasarkan laju perubahan posisi tanpa derivative kick besar ketika SP berubah.

## 6. Mengapa Ki sering dimulai dari nol
Position loop memiliki integrator mekanik alami melalui hubungan speed ke position. Pada banyak setup, P/PD sudah dapat mencapai target cukup dekat. Ki ditambahkan bila terdapat error residual akibat friction/dead-zone, tetapi terlalu besar dapat menambah overshoot dan windup.

## 7. Saturation dan target jauh
Error posisi dapat besar bila target jauh dari current position. Akibatnya output controller cepat mencapai limit. Analisis P12 harus menunjukkan:
- maximum absolute output;
- durasi saturation;
- pengaruh Kp/Ki/Kd;
- apakah error akhir turun setelah keluar dari saturation.

## 8. Anti-windup
Firmware baseline memakai conditional integration yang sama seperti P11. Integral tidak terus bertambah ketika output sudah saturasi dan error masih mendorong ke saturation.

## 9. Telemetry P12

```text
#PROTO,POSITION_PID,1
#ms,sp_deg,pos_deg,error,P,I,D,pid_pwm,count
```

Telemetry memungkinkan audit:
- setpoint;
- position;
- error;
- P/I/D;
- output;
- raw encoder count.

## 10. MATLAB supervisor/logger
`matlab_position_pid_experiment.m` melakukan:
- membuka serial;
- memastikan state stop sebelum konfigurasi;
- mengirim ZERO;
- mengirim gain/setpoint;
- heartbeat;
- logging;
- CSV/PNG;
- response metrics;
- cleanup STOP.

Mahasiswa harus memahami urutannya, bukan hanya menjalankan script.

## 11. Tuning bertahap
### P
Mulai Ki=0, Kd=0. Amati rise, overshoot, SSE, dan saturation.

### PD
Tambahkan Kd bila dibutuhkan untuk damping.

### PID
Tambahkan Ki kecil hanya bila error residual konsisten dan dapat dibuktikan dari beberapa run.

## 12. Positive dan negative target
P12 harus menganalisis target bertanda positif dan negatif relatif terhadap zero yang sama. Ini menguji konsistensi coordinate, sign, dan controller.

Metrics dihitung per step.

## 13. Multi-target trajectory
Project P12 menggunakan trajectory konseptual:

```text
0 -> +90 -> -90 -> +45 -> 0
```

Tujuannya bukan mencari gerakan tercepat, tetapi membuktikan reference, sign, repeatability, dan logging.

Gunakan `examples/position_reference_profile.m` untuk membuat tabel reference trajectory offline.

## 14. Repeatability
Lakukan target yang sama lebih dari sekali. Bandingkan:
- final position;
- absolute final error;
- peak error;
- settling time;
- apakah zero berubah.

Repeatability sering lebih informatif daripada satu grafik yang terlihat bagus.

## 15. Simulasi dan Simulink
Offline exercise:

```matlab
run('examples/position_pid_offline.m')
```

Builder:

```matlab
run('examples/build_motor_position_pid_simulink.m')
```

Simulasi digunakan untuk memahami struktur closed-loop dan saturation tanpa bergantung pada plant fisik.

## 16. Analisis log

```matlab
run('examples/analyze_position_pid_log.m')
```

Analisis minimal:
- SP vs position;
- error;
- P/I/D;
- control output;
- final error;
- maximum overshoot;
- sample interval;
- count range.

## 17. Troubleshooting
### Position tidak kembali ke nilai yang sama
Audit CPR, mechanical backlash, zero reference, missed count, dan repeatability.

### Sign target dan feedback tidak konsisten
Audit coordinate convention dari P10 sampai P12.

### Overshoot besar
Audit Kp, Kd, Ki, saturation, dan mechanical inertia.

### Error residual
Audit friction/dead-zone dan baru kemudian evaluasi Ki.

### Grafik meloncat sekitar 0/360°
Pastikan apakah data wrapped atau unwrapped. Jangan mencampur kedua coordinate tanpa transformasi eksplisit.

### Stop tidak terduga
Periksa telemetry dan heartbeat timeout.

## 18. P12 sebagai project checkpoint
P12 mengganti `TugasVideo.md` dengan `Project.md`. Deliverable project bukan hanya video, tetapi paket data dan source yang membuktikan:
- feedback benar;
- zero terdokumentasi;
- target positif/negatif dianalisis;
- PID dapat dijelaskan;
- data dapat direproduksi;
- STOP/timeout dipahami.

## 19. Program wajib

```text
examples/arduino_position_pid/arduino_position_pid.ino
examples/matlab_position_pid_experiment.m
examples/position_pid_offline.m
examples/position_reference_profile.m
examples/analyze_position_pid_log.m
examples/build_motor_position_pid_simulink.m
```

## 20. Jembatan ke P13
P12 menyelesaikan rangkaian MATLAB–Arduino. P13 memindahkan fokus ke PlatformIO dan workflow embedded yang lebih dekat ke firmware production. Semua konsep CPR, sign, PID, saturation, logging, dan fault state tetap digunakan.
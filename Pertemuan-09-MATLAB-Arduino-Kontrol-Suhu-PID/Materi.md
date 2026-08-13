# Pertemuan 9 — MATLAB–Arduino Mega Kontrol Suhu PID

## Capaian pembelajaran
Setelah praktikum ini mahasiswa mampu:

1. menjelaskan perbedaan controller Autonics pada P5–P6 dengan PID yang dihitung sendiri;
2. membuat rantai pengukuran temperatur `sensor -> tegangan -> kalibrasi -> PV`;
3. menghitung PID diskrit di MATLAB;
4. menerapkan saturasi 0–100% dan anti-windup;
5. menjelaskan derivative-on-measurement;
6. mengubah output PID menjadi time-proportional command untuk SSR/dummy output;
7. mencatat timestamp, PV, SP, error, P, I, D, output, dan status command;
8. menghitung rise time, settling time, overshoot, dan steady-state error;
9. membandingkan hasil Arduino/MATLAB dengan Autonics P5–P6;
10. menjelaskan batas host-side control dan alasan P14 memindahkan PID ke MCU.

---

## 1. Hubungan P5–P9
Pada P5–P6 controller temperatur adalah Autonics. Mahasiswa mengubah SV dan parameter controller, tetapi algoritma internal tidak terlihat penuh.

Pada P9 blok controller dibuat eksplisit:

```text
SP -> error -> PID MATLAB -> 0..100% -> time proportional -> output D8
 ^                                                        |
 |                                                        v
 +------ PV <- kalibrasi <- A0 <- sensor <- plant suhu ---+
```

Tujuan utama P9 bukan mengejar tuning paling cepat, tetapi memahami seluruh jalur pengukuran dan kontrol.

---

## 2. Plant dan I/O baseline
Baseline trainer:

- `A0` : input temperatur;
- `D8` : command output SSR/dummy;
- Arduino Mega 2560;
- MATLAB Support Package for Arduino Hardware;
- plant pemanas air yang telah disiapkan laboratorium atau dummy low-voltage untuk tahap awal.

P9 tidak memberikan prosedur instalasi sisi daya. Gunakan trainer laboratorium yang sudah tervalidasi dan ikuti `../SAFETY.md`.

---

## 3. Sensor: tegangan bukan temperatur
MATLAB membaca:

```matlab
voltage = readVoltage(a,'A0');
```

Nilai tersebut baru menjadi temperatur setelah fungsi kalibrasi diterapkan.

Contoh ideal LM35:

```text
T [degC] = 100 * V
```

Tetapi praktikum wajib membedakan:

```text
raw voltage -> sensor model -> calibration -> temperature
```

Jangan langsung memperlakukan `V*100` sebagai ground truth bila sensor, conditioning, atau referensi berbeda.

### Kalibrasi linear
Gunakan minimal tiga titik referensi bila memungkinkan. Model sederhana:

```text
T = m V + b
```

Dengan beberapa pasangan data, MATLAB dapat menggunakan:

```matlab
p = polyfit(voltage_V, reference_C, 1);
T = polyval(p, voltage_V);
```

Simpan slope, offset, residual, dan sumber thermometer referensi.

---

## 4. Error kontrol

```text
e[k] = SP[k] - PV[k]
```

Untuk plant heating:
- error positif berarti temperatur masih di bawah target;
- error negatif berarti PV berada di atas target.

Controller P9 hanya mempunyai output heating `0..100%`, sehingga ia tidak dapat memberikan pendinginan aktif. Ini harus dipahami saat membaca overshoot.

---

## 5. PID diskrit
Bentuk praktikum:

```text
P[k] = Kp e[k]
I[k] = I[k-1] + Ki e[k] Ts
D[k] = -Kd (PV[k]-PV[k-1]) / Ts
u[k] = sat(P[k]+I[k]+D[k], 0, 100)
```

Derivative memakai perubahan measurement sehingga perubahan setpoint tidak langsung menimbulkan derivative kick sebesar derivative-on-error.

### Interpretasi
- `Kp` memperbesar aksi berdasarkan error sekarang;
- `Ki` mengakumulasi error dan membantu mengurangi SSE;
- `Kd` memberi damping terhadap perubahan PV, tetapi sensitif terhadap noise;
- output dibatasi karena actuator selalu memiliki range fisik.

---

## 6. Anti-windup
Jika raw output >100%, menambah integral positif lagi tidak membantu actuator. Karena itu script memakai conditional integration:

- integral diizinkan bila output belum saturasi;
- atau bila error mendorong controller keluar dari saturasi.

Mahasiswa wajib dapat menunjukkan bagian ini di `matlab_temp_pid_host.m`.

---

## 7. Sampling time host-side
Nilai nominal `TS` dipakai untuk merencanakan loop, tetapi komputer bukan sistem hard real-time. USB, OS, plotting, dan MATLAB dapat menyebabkan jitter.

Karena plant termal lambat, host-side control masih berguna untuk pembelajaran. Namun catat waktu aktual pada log dan jangan mengklaim timing deterministik.

P14 memindahkan control loop ke MCU untuk implementasi yang lebih deterministic.

---

## 8. Time-proportional output
PID menghasilkan persentase. Untuk window `Tw`:

```text
ON_time = (u/100) * Tw
OFF_time = Tw - ON_time
```

Contoh `Tw=2 s`:

| PID output | ON | OFF |
|---:|---:|---:|
| 0% | 0 s | 2 s |
| 25% | 0.5 s | 1.5 s |
| 50% | 1 s | 1 s |
| 100% | 2 s | 0 s |

Time-proportional berbeda dari PWM motor berfrekuensi tinggi. Window harus dipilih sesuai plant dan perangkat output laboratorium.

---

## 9. Failsafe software
`matlab_temp_pid_host.m` mempunyai beberapa lapis proteksi software:

- output D8 dibuat OFF saat start;
- `onCleanup` mencoba mematikan D8 bila script berhenti;
- nilai sensor invalid memicu error;
- nilai melewati `MAX_TEMP_C` memicu STOP;
- setelah loop selesai output dibuat OFF.

Proteksi software tidak menggantikan proteksi hardware independen pada trainer.

---

## 10. Tahapan tuning
Gunakan kondisi awal yang comparable.

### Run 1 — P
Set `Ki=0`, `Kd=0`.

Amati:
- rise time;
- error steady-state;
- saturasi output.

### Run 2 — PI
Tambahkan Ki kecil.

Amati:
- perubahan SSE;
- overshoot;
- waktu pemulihan integral.

### Run 3 — PID
Tambahkan Kd hanya bila data menunjukkan manfaat.

Amati noise term D dan damping.

Jangan mengubah Kp, Ki, Kd, volume, temperatur awal, dan setpoint sekaligus.

---

## 11. Response metrics
Gunakan istilah yang konsisten sepanjang semester:

- delay time;
- rise time;
- peak time;
- maximum overshoot;
- settling time;
- steady-state error.

Helper repository:

```text
shared/matlab/response_metrics.m
shared/matlab/save_response_plot.m
```

Untuk plant heating tanpa cooling aktif, interpretasi settling setelah overshoot harus mempertimbangkan pendinginan pasif plant.

---

## 12. Simulasi sebelum hardware
Jalankan:

```matlab
run('examples/temp_pid_offline_simulation.m')
```

Tujuannya memeriksa:
- tanda error;
- saturasi;
- efek Kp/Ki/Kd;
- bentuk output time-proportional secara konseptual.

Kemudian generate Simulink:

```matlab
run('examples/build_temp_pid_simulink.m')
```

Builder membuat `models/temp_pid_water_heater.slx` bila MATLAB/Simulink tersedia.

---

## 13. Analisis data eksperimen
Output `matlab_temp_pid_host.m` memuat:

```text
time_s,temp_C,sp_C,error,P,I,D,pid_pct,ssr
```

Analisis ulang dengan:

```matlab
run('examples/analyze_temp_pid_log.m')
```

Pertanyaan yang wajib dijawab:
1. kapan output mencapai saturasi?
2. kapan integral mulai dominan?
3. apakah D memperbaiki respon atau hanya menambah noise?
4. apakah temperatur awal antar-run comparable?
5. apakah overshoot disebabkan gain, delay thermal, atau keduanya?

---

## 14. Perbandingan Autonics vs MATLAB–Arduino

| Aspek | Autonics P5/P6 | MATLAB–Arduino P9 |
|---|---|---|
| algoritma PID | internal controller | terlihat di source |
| tuning | parameter controller | parameter script |
| logging | manual/DAQMaster | MATLAB langsung |
| timing | controller dedicated | host PC + USB |
| fleksibilitas | sesuai fitur unit | sangat fleksibel |
| tujuan praktikum | industrial controller | memahami implementasi algoritma |

Jangan menyimpulkan satu platform selalu lebih baik; konteks implementasi berbeda.

---

## 15. Program wajib

```text
examples/matlab_temp_pid_host.m
examples/matlab_temp_pid.m
examples/temp_pid_offline_simulation.m
examples/temperature_sensor_calibration.m
examples/analyze_temp_pid_log.m
examples/build_temp_pid_simulink.m
```

Urutan yang direkomendasikan:

```text
kalibrasi sensor
-> offline simulation
-> dummy output verification
-> P
-> PI
-> PID
-> metrics
-> bandingkan dengan P5/P6
```

---

## 16. Kesalahan umum
1. Menganggap tegangan A0 otomatis sama dengan temperatur.
2. Mengubah beberapa gain sekaligus.
3. Tidak mencatat temperatur awal.
4. Tidak menyimpan raw CSV.
5. Menggunakan setpoint di luar batas trainer.
6. Mengabaikan saturasi output.
7. Menganggap `pause(TS)` sama dengan real-time deterministic.
8. Menginterpretasikan derivative tanpa melihat noise sensor.
9. Membandingkan P9 dengan P5/P6 pada kondisi awal berbeda.

---

## 17. Jembatan ke P10
P9 menyelesaikan closed-loop plant termal. P10 kembali membuka loop dan fokus pada sensor encoder motor. Ini disengaja: sebelum PID motor digunakan pada P11/P12, count, CPR, arah, posisi, RPM, sample time, dan filtering harus sudah valid.
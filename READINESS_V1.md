# Readiness Record — Branch v1

Dokumen ini mencatat status kesiapan repository untuk digunakan sebagai paket praktikum 16 pertemuan.

## Status

```text
Branch : v1
Status : SOFTWARE/STRUCTURE VALIDATED
```

Kesiapan fisik setiap trainer tetap harus mengikuti pemeriksaan laboratorium sebelum dipakai mahasiswa.

## 1. Struktur semester
Validator memeriksa:

- P1 sampai P16 tersedia;
- setiap pertemuan mempunyai `Materi.md` dan `Jobsheet.md`;
- P1–P7, P9–P11, P13–P15 mempunyai `TugasVideo.md`;
- P8, P12, P16 menggunakan `Project.md` dan tidak menggunakan `TugasVideo.md`;
- dokumen wajib tidak terpotong menjadi placeholder sangat pendek.

## 2. Referensi source
Validator memeriksa source penting yang disebut pada materi/jobsheet, termasuk MATLAB, Arduino, PlatformIO, Python, Node, Simulink builder, worksheet, dan shared helper.

Referensi source di dalam backtick pada dokumen wajib juga diperiksa agar file yang disebut benar-benar tersedia. File `.slx` hasil generate dikecualikan karena dibuat oleh builder MATLAB.

## 3. Python
Seluruh file `.py` diperiksa menggunakan `py_compile`.

Unit test `shared/python/test_response_metrics.py` dijalankan pada GitHub Actions.

## 4. Encoder
GitHub Actions menjalankan:

```text
P10 quadrature_state_test.py
```

Sketch encoder P10 juga dikompilasi untuk Arduino Mega.

Perbaikan readiness yang sudah diterapkan:

- P11 ZERO mereset count dan state estimator speed;
- P12 ZERO selalu menjadi transisi state berhenti sebelum reference diubah;
- P13 ZERO mereset count, `lastCount`, moving-average history, dan LPF;
- P15 ZERO mereset reference dan seluruh speed-estimator history.

Tujuan perubahan ini adalah mencegah delta-count/RPM palsu setelah reference encoder diubah.

## 5. Arduino sketch P10–P12
GitHub Actions mengompilasi:

```text
P10 arduino_encoder_stream.ino
P11 arduino_speed_pid.ino
P12 arduino_position_pid.ino
```

Target compile adalah Arduino Mega 2560.

## 6. PlatformIO P13–P15
GitHub Actions membangun:

```text
P13 mega_io_monitor
P14 mega_temp_pid
P15 mega_motor_pid
```

Build harus tetap hijau sebelum perubahan baru dianggap siap digunakan.

## 7. Protocol
Readiness validator menjaga marker protocol utama:

```text
P13 : #PROTO,IO_MONITOR,2
P14 : #PROTO,TEMP_PID,2
P15 : #PROTO,MOTOR_PID,3
```

GUI/logger harus tetap menggunakan jumlah kolom dan satuan yang sesuai dengan firmware.

## 8. Simulink
Repository tidak menyimpan model `.slx` sebagai satu-satunya source kebenaran. Model dibuat dari script builder yang dapat diaudit:

```text
P3  build_three_plants_simulink.m
P4  build_pid_manual_simulink.m
P9  build_temp_pid_simulink.m
P11 build_motor_speed_pid_simulink.m
P12 build_motor_position_pid_simulink.m
```

Bangun seluruh model dengan:

```matlab
build_all_slx
```

Runtime MATLAB/Simulink tidak tersedia pada GitHub Actions repository ini, sehingga builder diperiksa sebagai source tetapi eksekusi `.slx` harus diverifikasi pada komputer laboratorium yang memiliki MATLAB/Simulink.

## 9. Model dan satuan
P9/P11/P12 builder telah diselaraskan dengan model P3:

- thermal plant: `35/(120s+1)` dengan input normalized;
- motor speed: `0.01/[0.005 0.06 0.1001]`;
- motor position: model speed ditambah integrator posisi;
- konversi PWM/tegangan dan rad/s↔RPM atau rad↔degree dibuat eksplisit pada builder terkait.

## 10. Data dan response metrics
Shared helper tersedia untuk MATLAB dan Python.

Metrik utama:

- delay time;
- rise time;
- peak time;
- overshoot;
- settling time;
- steady-state error.

Untuk data multi-setpoint, analisis harus dilakukan per segmen step yang jelas.

## 11. GUI
P14 dan P15 mempunyai mode:

```bash
python app.py --demo
```

Mode demo digunakan untuk memeriksa GUI, parsing internal, plotting, logging, dan workflow sebelum menggunakan trainer.

Python syntax GUI diperiksa otomatis. Runtime GUI penuh tetap memerlukan dependency dari `requirements.txt` dan lingkungan desktop.

## 12. P16 acceptance
P16 menyediakan:

```text
Materi.md
Jobsheet.md
Project.md
examples/final_smoke_test.py
examples/node_serial_logger/
```

Smoke test mengirim state pasif, membaca protocol/telemetry, dan menyimpan JSON sebagai evidence komunikasi.

## 13. Perintah validasi utama
Dari root repository:

```bash
python validate_repo.py
```

Untuk melihat build otomatis, buka workflow `validate-repository` pada branch `v1`.

## 14. Hal yang tetap memerlukan verifikasi laboratorium
Automated CI tidak dapat membuktikan kondisi fisik berikut:

- sensor yang dipasang pada trainer benar dan terkalibrasi;
- CPR encoder fisik sama dengan nilai konfigurasi;
- arah mekanik sesuai konvensi course;
- kondisi catu/driver/trainer;
- batas mekanik plant;
- respons termal aktual;
- response closed-loop aktual pada hardware.

Karena itu sebelum sesi praktikum, instruktur tetap menjalankan `RUN_CHECKLIST.md`, `SAFETY.md`, dan jobsheet per pertemuan.

## 15. Definition of ready
Branch `v1` dapat dinyatakan siap dari sisi repository bila:

```text
validate_repo.py PASS
GitHub Actions validate-repository SUCCESS
P10-P12 compile PASS
P13-P15 build PASS
quadrature test PASS
response metrics test PASS
Node syntax PASS
```

Setelah itu kesiapan satu meja/trainer ditentukan oleh pemeriksaan fisik laboratorium dan run checklist per perangkat.

# Jobsheet Pertemuan 11 — PID Kecepatan Motor DC

> Analisis kuantitatif, tabel P/PI/PID, audit saturasi, pengaruh filter, dan perbandingan dua arah dijelaskan lebih lengkap pada `ANALISIS_DATA.md`.

## Tujuan
Menggunakan feedback RPM yang telah tervalidasi pada P10 untuk menganalisis kontrol kecepatan closed-loop, respons arah positif dan negatif, pengaruh P/I/D, saturasi, anti-windup, dan kualitas telemetry.

## Prasyarat P10
Sebelum melanjutkan, pastikan:
- CPR telah diverifikasi;
- count mempunyai tanda yang konsisten;
- RPM positif dan negatif terbaca dengan benar;
- pengaruh moving average dan LPF sudah dipahami.

Kesalahan feedback tidak boleh ditutupi dengan mengubah gain PID.

## File utama
```text
examples/arduino_speed_pid/arduino_speed_pid.ino
examples/matlab_speed_pid_experiment.m
examples/matlab_speed_pid_profile.m
examples/pid_response_offline.m
examples/speed_pid_simulation.m
examples/analyze_speed_pid_log.m
examples/build_motor_speed_pid_simulink.m
ANALISIS_DATA.md
```

## A. Review teori
Jelaskan:
1. `error = SP - PV`;
2. peran Kp, Ki, Kd;
3. derivative-on-measurement;
4. saturasi output bertanda;
5. conditional anti-windup;
6. pengaruh filter RPM terhadap loop kontrol.

## B. Simulasi offline
Jalankan:

```matlab
run('examples/speed_pid_simulation.m')
```

Ubah satu parameter pada satu waktu dan amati perubahan respons, error, dan output. Simpan hasil yang akan digunakan sebagai pembanding konsep dengan data eksperimen.

## C. Audit source
Buka firmware utama dan identifikasi bagian yang menangani:
- encoder;
- perhitungan RPM;
- filter feedback;
- error;
- P, I, dan D;
- anti-windup;
- batas output;
- telemetry;
- RUN/STOP;
- host timeout.

## D. Konfigurasi eksperimen
Catat sebelum setiap dataset:
- CPR;
- sample interval;
- Kp;
- Ki;
- Kd;
- setpoint;
- batas output;
- kondisi beban;
- kondisi awal RPM.

## E. Perbandingan P, PI, dan PID
Buat minimal tiga dataset yang dapat dibandingkan:
- P: Ki=0 dan Kd=0;
- PI: tambahkan Ki secara bertahap;
- PID/PD: gunakan Kd hanya bila data menunjukkan kebutuhan peredaman.

Untuk setiap dataset analisis:
- rise time;
- overshoot;
- settling time;
- steady-state error;
- output maksimum;
- kecenderungan saturasi.

## F. Respons dua arah
Gunakan satu setpoint positif dan satu setpoint negatif dengan besar yang sebanding. Bandingkan hasilnya secara terpisah.

Feedback yang dapat membaca RPM negatif belum cukup untuk membuktikan kontrol arah negatif benar. Audit hubungan antara setpoint, error, output controller, arah gerak, dan tanda RPM.

## G. Profile offline
Jalankan:

```matlab
run('examples/matlab_speed_pid_profile.m')
```

Gunakan profil tersebut untuk memahami segmentasi data `0 -> positif -> 0 -> negatif -> 0`. Response metrics harus dihitung per segmen, bukan untuk seluruh profil sekaligus.

## H. Analisis log
Setelah data tersedia, jalankan:

```matlab
run('examples/analyze_speed_pid_log.m')
```

Grafik minimum:
1. SP dan RPM;
2. error;
3. P, I, dan D;
4. output controller.

Lengkapi tabel dan pertanyaan pada `ANALISIS_DATA.md`.

## I. Audit saturasi
Catat kapan nilai absolut output mendekati batas. Jelaskan:
- apakah saturasi hanya terjadi pada awal respons;
- apakah saturasi berlangsung lama;
- bagaimana term I berperilaku saat saturasi;
- apakah error turun setelah keluar dari saturasi.

## J. Perbandingan filter
Hubungkan hasil dengan P10. Jelaskan apakah LPF membuat feedback lebih stabil, tetapi juga menambah keterlambatan yang memengaruhi respons PID.

## K. Pertanyaan analisis
1. Mengapa respons arah positif dan negatif dapat berbeda?
2. Mengapa Ki dapat mengurangi SSE tetapi menambah overshoot?
3. Mengapa Kd sensitif terhadap kualitas feedback?
4. Mengapa output yang selalu saturasi membuat perbandingan gain menjadi kurang bermakna?
5. Bagaimana membedakan kesalahan tanda dari tuning yang buruk?
6. Mengapa response metrics harus dihitung per segmen setpoint?
7. Apa bukti bahwa hasil eksperimen dapat direproduksi?
8. Parameter apa saja yang harus dipertahankan tetap ketika dua tuning dibandingkan?

## Deliverable
- source yang digunakan;
- raw CSV;
- grafik;
- tabel P/PI/PID;
- metadata eksperimen;
- analisis arah positif dan negatif;
- hasil `ANALISIS_DATA.md`;
- kesimpulan berbasis data.

## Kriteria kelulusan
- [ ] CPR dan tanda feedback telah tervalidasi;
- [ ] parameter eksperimen terdokumentasi;
- [ ] P, PI, dan PID/PD dibandingkan;
- [ ] respons positif dan negatif dianalisis;
- [ ] saturasi dan anti-windup dijelaskan;
- [ ] CSV dan grafik tersedia;
- [ ] source dapat dijelaskan;
- [ ] kesimpulan menggunakan metrik respons.

## Expected result
Mahasiswa mampu menjelaskan hubungan `SP -> error -> PID -> output -> plant -> feedback RPM`, menunjukkan respons dua arah, dan menilai tuning berdasarkan data kuantitatif.

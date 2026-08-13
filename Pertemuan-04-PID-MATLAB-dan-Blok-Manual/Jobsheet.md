# Jobsheet Pertemuan 4 — PID MATLAB dan PID Manual Simulink

## Tujuan
Mahasiswa mampu membandingkan P, PI, PID, melakukan tuning bertahap, menghitung karakteristik respon, serta membangun PID dari blok dasar di Simulink.

## Persiapan
1. Selesaikan P3 dan pastikan memahami `Gth`, `Gspeed`, dan `Gpos`.
2. Masuk ke folder P4.
3. Pastikan Control System Toolbox dan Simulink tersedia.
4. Baca `Materi.md`.

## Percobaan 1 — P controller
Gunakan plant:

```matlab
s=tf('s');
G=35/(120*s+1);
```

Uji `Kp` = 0.05, 0.10, 0.20, 0.40 dengan `Ki=Kd=0`.

Untuk setiap kasus:

```matlab
C=pid(Kp,0,0);
T=feedback(C*G,1);
info=stepinfo(T);
ess=abs(1-dcgain(T));
```

Isi tabel:

| Kp | RiseTime | SettlingTime | Overshoot | ess | Catatan |
|---:|---:|---:|---:|---:|---|
| 0.05 | | | | | |
| 0.10 | | | | | |
| 0.20 | | | | | |
| 0.40 | | | | | |

## Percobaan 2 — PI controller
Pilih satu `Kp` dari Percobaan 1 lalu uji beberapa `Ki`, misalnya 0.001, 0.003, 0.005, 0.010.

Catat perubahan:
- error steady-state;
- rise time;
- settling time;
- overshoot.

Jelaskan mengapa penambahan integral mengubah error akhir.

## Percobaan 3 — PID
Dengan `Kp` dan `Ki` yang dipilih, uji `Kd` bertahap. Jangan mengubah tiga gain sekaligus.

Bandingkan P, PI, dan PID pada satu figure. Jalankan juga:

```matlab
run('examples/pid_comparison.m')
```

## Percobaan 4 — Gain sweep otomatis
Jalankan:

```matlab
run('examples/pid_gain_sweep.m')
```

Tentukan satu konfigurasi yang paling masuk akal menurut kelompok. Alasan harus memakai metrics dan bentuk respon, bukan hanya “grafiknya paling bagus”.

## Percobaan 5 — `pidtune`
Gunakan:

```matlab
[Cauto,infoTune]=pidtune(G,'PID');
Tauto=feedback(Cauto*G,1);
step(Tauto,600); grid on;
stepinfo(Tauto)
```

Bandingkan gain hasil `pidtune` dengan gain manual kelompok.

| Metode | Kp | Ki | Kd | Rise | Settling | Overshoot | ess |
|---|---:|---:|---:|---:|---:|---:|---:|
| Manual | | | | | | | |
| pidtune | | | | | | | |

## Percobaan 6 — PID manual di Simulink
Jalankan:

```matlab
run('examples/build_pid_manual_simulink.m')
```

Buka file `.slx` hasil builder dan identifikasi:
- Step;
- Sum error;
- cabang P;
- cabang I + Integrator;
- cabang D;
- Sum P+I+D;
- plant;
- feedback;
- Scope.

Gambar ulang diagram blok pada laporan.

## Percobaan 7 — Verifikasi manual vs built-in
Buat dua jalur simulasi dengan gain sama:
1. PID Controller block;
2. PID manual P+I+D.

Plot kedua output pada satu Scope atau To Workspace. Hitung selisih maksimum kedua kurva.

Jika berbeda, periksa:
- struktur derivative;
- initial condition integrator;
- filter derivative;
- solver dan sample time;
- parameter gain.

## Percobaan 8 — Apply ke motor speed
Load model P3 atau jalankan kembali `plant_transfer_functions.m`, lalu pasang controller pada `Gspeed`.

Mulai dari gain kecil, lakukan eksperimen bertahap, dan catat hasil. Jangan menyalin gain pemanas air secara langsung.

## Percobaan 9 — Apply ke motor position
Gunakan `Gpos` dan buat closed-loop posisi. Bandingkan respon open-loop posisi P3 dengan closed-loop pada P4.

Jawab:
1. Mengapa closed-loop posisi dapat menuju target sedangkan open-loop step posisi terus berubah?
2. Apa pengaruh integrator yang sudah terdapat pada plant posisi?

## Challenge
Pilih satu:
1. bandingkan derivative ideal dan filtered derivative;
2. buat script yang mencari kombinasi gain terbaik dari grid kecil berdasarkan settling time dan overshoot;
3. simpan hasil semua eksperimen menjadi table CSV;
4. tambahkan Saturation block pada model manual dan jelaskan perbedaan respon.

## Hasil yang dikumpulkan
- tabel P sweep;
- tabel PI sweep;
- tabel PID;
- grafik perbandingan P/PI/PID;
- hasil `pidtune`;
- screenshot PID manual Simulink;
- verifikasi manual vs built-in;
- satu hasil motor speed atau position;
- challenge bila dikerjakan.

## Pertanyaan analisis
1. Mengapa P dapat menyisakan error akhir?
2. Mengapa Ki membantu mengurangi error akhir?
3. Kapan Ki terlalu besar menjadi masalah pada respon?
4. Mengapa derivative ideal kurang realistis untuk sinyal noisy?
5. Apa makna `feedback(C*G,1)`?
6. Mengapa gain tidak boleh disalin antarplant?
7. Mengapa manual block harus dibandingkan dengan built-in?
8. Apa hubungan PID kontinu P4 dengan PID digital pada firmware?

## Checklist
- [ ] P sweep selesai;
- [ ] PI sweep selesai;
- [ ] PID diuji;
- [ ] `stepinfo` dicatat;
- [ ] `pidtune` dibandingkan;
- [ ] builder `.slx` berjalan;
- [ ] PID manual diperiksa blok per blok;
- [ ] manual vs built-in diverifikasi;
- [ ] minimal satu plant motor diuji secara simulasi;
- [ ] kesimpulan berbasis data.

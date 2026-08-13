# Pertemuan 4 — PID MATLAB dan Blok PID Manual

## 1. Tujuan
Membandingkan PID bawaan MATLAB/Simulink dengan implementasi P+I+D yang dirangkai sendiri.

## 2. Closed-loop
Untuk controller `C(s)` dan plant `G(s)`:

`T(s)=C(s)G(s)/(1+C(s)G(s))`

## 3. P, PI, PID
MATLAB:

```matlab
C = pid(Kp,Ki,Kd);
T = feedback(C*G,1);
step(T)
```

## 4. Blok manual
PID dapat dibangun dari:
- Sum error `SP-PV`;
- Gain Kp;
- Integrator 1/s dan Gain Ki;
- Derivative/filter dan Gain Kd;
- Sum P+I+D;
- Saturation.

Untuk real embedded, derivative murni dihindari; gunakan filtered derivative atau derivative on measurement.

## 5. Anti-windup
Jika output dibatasi 0–100% atau -255..255, integral harus dicegah terus tumbuh di arah saturasi. P14/P15 menerapkan conditional integration.

## 6. Tuning eksperimen
Mulai aman:
1. Ki=0, Kd=0.
2. Naikkan Kp.
3. Tambahkan Ki sedikit.
4. Tambahkan Kd jika perlu damping/noise masih terkendali.
5. Catat hasil dengan metrik, bukan hanya “kelihatan bagus”.

## Program
- `pid_comparison.m`
- `pid_discrete_antiwindup.m`
- `build_pid_manual_simulink.m`

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **PID MATLAB dan blok manual**. Program yang harus dibuka dan dipahami:
- `pid_comparison.m`
- `pid_discrete_antiwindup.m`
- `build_pid_manual_simulink.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Kurva P/PI/PID dapat dibandingkan dan blok P/I/D manual terbentuk di Simulink.

## Validasi dan troubleshooting
Jika simulasi divergen, kecilkan gain; cek tanda feedback dan saturasi sebelum menyimpulkan tuning.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

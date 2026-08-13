# Pertemuan 9 — MATLAB–Arduino Mega Kontrol Suhu PID

P5/P6 memakai controller Autonics. P9 mengganti controller dengan Arduino Mega sehingga mahasiswa melihat sendiri sensor → error → PID → SSR.

## 1. Hardware
Baseline:
- sensor temperatur analog `A0`;
- SSR command `D8`;
- Arduino Mega;
- heater water plant.

Untuk LM35: `T(°C)=V*100`. Jika sensor berbeda, ubah fungsi konversi dan kalibrasi.

## 2. Mengapa SSR memakai time-proportional
PID menghasilkan 0–100%. SSR/heater tidak harus diberi PWM cepat. Gunakan window misalnya 2 s:

`on_time = output_percent/100 * window`

Contoh output 25% → ON 0.5 s dari window 2 s.

## 3. PID diskrit di MATLAB
`matlab_temp_pid_host.m` menjalankan PID di PC:
- MATLAB membaca A0;
- menghitung PID;
- mengendalikan D8.

Ini cocok untuk pembelajaran karena semua term P/I/D terlihat.

## 4. Keterbatasan host control
Loop MATLAB/USB tidak hard real-time. Karena plant termal lambat, ini masih sesuai praktikum. Untuk implementasi embedded yang lebih deterministic, P14 memindahkan PID ke MCU.

## 5. Failsafe
Script:
- output OFF sebelum mulai;
- `onCleanup` mematikan SSR saat script berhenti/error;
- temperature invalid → STOP;
- over-temperature → STOP;
- Ctrl+C/exception → cleanup.

Tetap gunakan thermal protection hardware independen.

## 6. Tuning
Mulai dengan heater dummy/plant aman.
1. Kp saja.
2. tambah Ki.
3. tambah Kd bila perlu.
4. catat data.
5. bandingkan dengan Autonics P5/P6.

## 7. Simulink
`build_temp_pid_simulink.m` membuat model simulasi `temp_pid_water_heater.slx`. Model ini tidak mengaktifkan hardware; digunakan untuk latihan struktur loop.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **MATLAB-Arduino PID suhu**. Program yang harus dibuka dan dipahami:
- `matlab_temp_pid_host.m`
- `build_temp_pid_simulink.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
PV mengikuti SP dengan SSR time-proportional dan data eksperimen tersimpan.

## Validasi dan troubleshooting
Mulai dengan heater dummy/low-voltage. Jangan menaikkan setpoint sebelum sensor dan batas maksimum terverifikasi.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

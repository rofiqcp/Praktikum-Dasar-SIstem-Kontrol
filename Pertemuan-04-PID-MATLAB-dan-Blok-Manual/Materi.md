# Pertemuan 04 — MATLAB PID dan PID Block Buat Sendiri

## Capaian Pembelajaran
- memahami closed-loop PID
- membandingkan P/PI/PID
- membangun PID dari blok dasar
- menganalisis efek saturasi dan anti-windup

## Materi Inti

Pertemuan ini menerapkan P, PI, PD dan PID pada plant pemanas air dan motor. Selain memakai block PID bawaan, mahasiswa **membangun PID sendiri** dari jalur P + I + D sehingga memahami setiap komponen.

### Closed-loop
`T(s)=C(s)G(s)/(1+C(s)G(s))`.

### Manual PID block
- P: `Kp*e`
- I: `Ki * 1/s * e`
- D praktis: derivative dengan low-pass filter agar tidak memperkuat noise berlebihan
- Saturation untuk batas actuator
- Anti-windup diperlukan saat output jenuh.

Script `build_pid_manual_simulink.m` membuat model Simulink dari nol secara programatik, sehingga tidak bergantung pada file `.slx` binary.


## Program yang Wajib Dijalankan
- `examples/pid_comparison.m`
- `examples/build_pid_manual_simulink.m`

## Alur Praktikum
1. Jalankan `pid_comparison.m` untuk pemanas air.
2. Uji P, PI, PID dan bandingkan `stepinfo`.
3. Jalankan `build_pid_manual_simulink.m`.
4. Buka model `pid_manual_water_heater.slx` yang dihasilkan.
5. Tunjukkan jalur P, I, D dan Sum.
6. Ubah gain dan amati Scope.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

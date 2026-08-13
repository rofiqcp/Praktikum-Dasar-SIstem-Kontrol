# Pertemuan 09 — Jobsheet — PID Suhu MATLAB–Arduino


1. Kalibrasi A0 terhadap alat ukur referensi.
2. Jalankan `matlab_temp_pid.m` dengan output SSR **dummy LED dulu**.
3. Verifikasi duty 0, 25, 50, 100% pada indikator.
4. Set over-temperature limit yang aman.
5. Sambungkan plant heater yang disetujui.
6. Mulai gain kecil; log SP, PV, P, I, D, PID, SSR.
7. Simpan CSV dan grafik.
8. Bandingkan dengan data Autonics P5/P6.

**Stop segera** jika sensor invalid atau temperatur melewati limit.

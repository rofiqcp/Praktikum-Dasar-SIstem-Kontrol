# Jobsheet Pertemuan 05 — Autonics TK4S + Pemanas Air: Pengambilan Data Manual Stopwatch

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Pastikan bak berisi air sesuai batas aman plant dan sensor terendam sesuai prosedur trainer.
2. Nyalakan controller tanpa menghubungkan mains secara terbuka.
3. Set suhu target contoh 50 °C.
4. Start stopwatch bersamaan saat percobaan dimulai.
5. Catat PV tiap 5 s atau 10 s pada template CSV/Excel.
6. Ulangi untuk minimal 3 nilai hysteresis.
7. Uji parameter P terlebih dahulu, lalu I, kemudian D secara bertahap.
8. Simpan CSV dan jalankan `examples/analyze_manual_temperature.py data.csv`.
9. Bandingkan overshoot, settling time, dan steady-state error.


## C. Data yang Dicatat
- setpoint dan parameter controller;
- waktu sampling;
- process variable/kecepatan/posisi;
- output controller;
- delay time, rise time, peak time, settling time, overshoot, steady-state error bila relevan.

## D. Verifikasi
- [ ] Program dapat start tanpa error.
- [ ] Input/setpoint dapat diubah.
- [ ] Output plant berubah sesuai command.
- [ ] Feedback terbaca.
- [ ] Grafik/data tersimpan.
- [ ] Ada pembahasan karakteristik respon.

## E. Pertanyaan Analisis
1. Apa input, controller, actuator, plant, sensor dan feedback pada percobaan?
2. Apa perbedaan open-loop dan closed-loop pada kasus ini?
3. Apa efek menaikkan Kp?
4. Kapan integral membantu dan kapan menimbulkan windup?
5. Apa peran derivative/filter terhadap noise dan overshoot?


> **Safety lab:** gunakan plant tegangan rendah bila memungkinkan. Untuk pemanas mains, mahasiswa hanya bekerja pada sisi kontrol low-voltage; wiring mains dilakukan petugas kompeten di dalam enclosure berproteksi.

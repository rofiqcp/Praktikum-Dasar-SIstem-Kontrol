# Jobsheet Pertemuan 08 — Project UTS — PCB Arduino Mega Control Trainer

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Freeze pin map.
2. Selesaikan schematic dan ERC.
3. Selesaikan PCB dan DRC.
4. Review power/ground dan kapasitor decoupling.
5. Fabrikasi/assembly atau prototype.
6. Jalankan program bring-up.
7. Rekam acceptance test.


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

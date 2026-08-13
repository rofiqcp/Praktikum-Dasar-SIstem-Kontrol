# Jobsheet Pertemuan 01 — Dasar Sistem Kontrol, PID, dan Briefing Project PCB

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Jalankan `examples/control_basics.py`.
2. Bandingkan open-loop, P, PI dan PID pada model termal sederhana.
3. Ubah Kp/Ki/Kd dan catat efeknya.
4. Gambar diagram blok untuk pemanas air dan motor DC.
5. Buat draft blok diagram PCB semester: Arduino Mega, sensor suhu, SSR input, L293D, encoder A/B, supply dan konektor.
6. Tentukan pin awal dan buat tabel I/O.


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

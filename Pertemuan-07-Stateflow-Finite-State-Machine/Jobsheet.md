# Jobsheet Pertemuan 07 — Finite State Machine dengan Stateflow MATLAB/Simulink

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Jalankan `examples/fsm_examples.m` dan amati trace state pada Command Window.
2. Ubah urutan event MP3 player dan cek state akhir.
3. Ubah durasi lampu traffic light dan plot hasilnya.
4. Uji input turning signal Left/Right/Off.
5. Jalankan `examples/build_traffic_light_stateflow.m` jika Stateflow tersedia.
6. Buka model `.slx` yang dibuat dan inspeksi state, transition, dan `after(...,sec)`.
7. Buat satu state FAULT tambahan dan jelaskan kondisi masuk/keluarnya.


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

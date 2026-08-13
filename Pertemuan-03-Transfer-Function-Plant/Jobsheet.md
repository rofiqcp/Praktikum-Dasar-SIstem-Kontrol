# Jobsheet Pertemuan 03 — MATLAB Transfer Function: Pemanas Air, Motor DC Kecepatan dan Posisi

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Jalankan `examples/plant_transfer_functions.m`.
2. Amati tiga plot: pemanas air, motor speed, motor position.
3. Ubah parameter termal K dan tau.
4. Ubah J, b, R, L, Kt motor dan amati pole/respon.
5. Jalankan notebook Colab `examples/colab/plant_transfer_function.ipynb` sebagai pembanding Python.
6. Jelaskan mengapa transfer posisi mempunyai integrator tambahan.


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

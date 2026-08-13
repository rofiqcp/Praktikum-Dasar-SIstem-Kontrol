# Jobsheet Pertemuan 15 — Node.js Serial DAQ dan Dashboard Kontrol

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Install Node.js LTS.
2. Masuk ke `examples/node_serial_logger`.
3. Jalankan `npm install`.
4. Jalankan `node index.js COM5 115200` (ubah port).
5. Buka `http://localhost:3000`.
6. Jalankan plant motor atau heater dan lihat data terbaru.
7. Pastikan `data_log.csv` bertambah.
8. Jelaskan perbedaan logging Python, DAQMaster dan Node.js.


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

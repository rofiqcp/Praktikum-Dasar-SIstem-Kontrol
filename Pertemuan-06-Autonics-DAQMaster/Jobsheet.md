# Jobsheet Pertemuan 06 — Autonics TK4S + Pemanas Air: DAQMaster

## A. Persiapan
- Baca `Materi.md`.
- Pastikan software/hardware sesuai topik sudah tersedia.
- Buat folder hasil sendiri, jangan mengubah contoh sebelum contoh dasar berhasil dijalankan.

## B. Langkah Kerja
1. Hubungkan converter komunikasi trainer ke PC sesuai manual lab.
2. Buka DAQMaster dan tambahkan device Autonics TK4.
3. Pilih interface/port yang benar lalu Connect.
4. Tambahkan channel PV, SV dan MV/output bila tersedia.
5. Set logging interval konstan.
6. Uji 3 hysteresis pada SV 50 °C.
7. Uji PID: cari P terbaik, tambah I, lalu D. Simpan minimal 10 dataset/variasi parameter.
8. Export CSV.
9. Jalankan `examples/analyze_daqmaster_export.py export.csv`.
10. Bandingkan ketelitian timestamp manual vs DAQMaster.


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


## Dataset contoh untuk uji program
Sebelum memakai ekspor DAQMaster asli, jalankan analyzer dengan `examples/daq_export_sample.csv` agar alur analisis dapat diverifikasi tanpa hardware.

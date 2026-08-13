# Project / Responsi Akhir P16

## A. Deliverable final
Kumpulkan satu folder/ZIP berisi:

```text
NIM_Nama_P16/
├── README.md
├── hardware/
│   ├── foto_pcb.jpg
│   ├── foto_wiring_suhu.jpg
│   └── foto_wiring_motor.jpg
├── p14_temperature/
│   ├── firmware/
│   ├── gui/
│   ├── run.csv
│   ├── run.xlsx
│   └── graph.jpg
├── p15_motor/
│   ├── firmware/
│   ├── gui/
│   ├── speed.csv
│   ├── speed.xlsx
│   ├── speed.jpg
│   ├── position.csv
│   └── position.jpg
└── acceptance/
    ├── smoke_test.json
    └── checklist.md
```

## B. Pertanyaan responsi
1. Gambarkan loop kontrol suhu P14.
2. Mengapa SSR memakai control window?
3. Apa akibat control window terlalu pendek/panjang?
4. Jelaskan anti-windup pada source.
5. Mengapa derivative-on-measurement dipakai?
6. Bagaimana fault suhu invalid dideteksi?
7. Apa fungsi heartbeat GUI?
8. Apa yang terjadi jika USB terlepas saat RUN?
9. Bagaimana quadrature decoder menentukan arah?
10. Apa bedanya PPR dan CPR pada konteks decoder?
11. Turunkan rumus RPM dari delta count.
12. Mengapa RPM raw berisik pada kecepatan rendah?
13. Bandingkan MA dan LPF.
14. Jelaskan hubungan alpha dengan lag/noise.
15. Bagaimana PWM signed dipetakan ke D5/D6?
16. Mengapa D5 dan D6 tidak boleh aktif bersamaan pada desain ini?
17. Bedakan feedback speed dan position.
18. Mengapa encoder di-zero saat masuk mode position?
19. Mengapa mode switch harus stop dahulu?
20. Jelaskan mekanisme stall detection dan keterbatasannya.
21. Apa risiko Kp terlalu besar?
22. Apa risiko Ki terlalu besar?
23. Apa risiko Kd terlalu besar pada encoder noisy?
24. Apa arti overshoot dan settling time?
25. Bagaimana menghitung steady-state error?
26. Mengapa sampling yang berubah membuat tuning berubah?
27. Apa yang harus divalidasi setelah AI mengubah firmware?
28. Apa perbedaan build sukses dan sistem kontrol yang benar?
29. Sebutkan minimal lima interlock keselamatan trainer.
30. Jelaskan urutan commissioning dari board kosong sampai closed-loop.

## C. Kriteria lulus fungsi
- firmware P14/P15 build dan upload;
- tidak ada aktuator aktif saat boot;
- STOP mematikan output;
- telemetry parse stabil;
- suhu terkendali tanpa melewati batas konfigurasi;
- speed dua arah;
- position dua arah dalam batas mekanik;
- export data lengkap;
- mahasiswa dapat menjelaskan source dan grafik.

## D. Penilaian yang disarankan
- konsep dan tanya jawab 25%;
- hardware/wiring/safety 20%;
- firmware 20%;
- GUI & data acquisition 15%;
- eksperimen/tuning/analisis 15%;
- dokumentasi 5%.

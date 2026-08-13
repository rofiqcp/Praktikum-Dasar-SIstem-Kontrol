# Bank Soal Responsi P1–P7

Gunakan sebagai pool pertanyaan acak. Dosen dapat meminta jawaban lisan, tulisan singkat, interpretasi grafik, atau modifikasi source.

## P1 — Dasar sistem kontrol
1. Gambarkan open-loop dan closed-loop.
2. Jelaskan SP, PV, error, controller, actuator, plant, dan feedback.
3. Apa perbedaan disturbance dan noise?
4. Apa efek Kp terlalu kecil dan terlalu besar?
5. Mengapa integral membantu steady-state error?
6. Apa itu integral windup?
7. Mengapa derivative sensitif noise?
8. Apa fungsi saturation?
9. Jelaskan rise time, overshoot, settling time, SSE.
10. Mengapa sample time harus dicatat?

## P2 — MATLAB
11. Bedakan scalar, vector, dan matrix.
12. Bedakan `*` dan `.*`.
13. Apa fungsi logical indexing?
14. Mengapa preallocation penting?
15. Buat vector waktu dan sinyal sinus.
16. Apa beda script dan function?
17. Bagaimana menyimpan table ke CSV?
18. Apa arti NaN?
19. Mengapa plot harus memiliki label/satuan?
20. Jelaskan simulasi Euler orde satu.

## P3 — Transfer function
21. Definisikan transfer function.
22. Apa arti initial condition nol pada definisi transfer function?
23. Apa itu pole dan zero?
24. Apa hubungan pole dan dinamika respon?
25. Turunkan `K/(tau*s+1)` dari persamaan orde satu.
26. Apa arti `K` dan `tau`?
27. Mengapa pada `t=tau` orde satu mencapai sekitar 63.2%?
28. Jelaskan persamaan elektrik motor DC.
29. Jelaskan persamaan mekanik motor DC.
30. Mengapa model posisi memiliki integrator tambahan?
31. Apa fungsi `dcgain`?
32. Kapan `stepinfo` tidak tepat untuk ditafsirkan secara langsung?
33. Bagaimana mengestimasi gain orde satu dari data step?
34. Apa perbedaan model dan plant fisik?

## P4 — PID MATLAB/Simulink
35. Tulis bentuk ideal PID.
36. Apa fungsi `feedback()`?
37. Bandingkan P, PI, PD, PID.
38. Mengapa Ki dapat memperbesar overshoot?
39. Mengapa Kd sering diberi filter?
40. Apa yang dilakukan `pidtune` secara umum?
41. Mengapa hasil tuning otomatis tetap harus diverifikasi?
42. Gambarkan PID manual menggunakan blok P+I+D.
43. Bagaimana membuktikan blok manual setara dengan controller built-in?
44. Apa akibat saturation pada integral?
45. Apa hubungan P4 dengan implementasi embedded?

## P5 — Data manual
46. Apa arti PV dan SV pada dataset?
47. Mengapa hysteresis dibutuhkan pada ON/OFF?
48. Apa dampak sampling stopwatch yang terlalu jarang?
49. Mengapa raw data tidak boleh diedit diam-diam?
50. Apa itu repeatability?
51. Metadata apa yang harus sama sebelum dua run dibandingkan?
52. Bagaimana missing sample dicatat?
53. Mengapa peak terukur bisa lebih rendah dari peak sebenarnya?
54. Apa sumber human error pada pencatatan manual?

## P6 — DAQMaster/data digital
55. Jelaskan alur device–DAQ–CSV–analysis.
56. Parameter komunikasi apa yang harus didokumentasikan?
57. Apa itu timestamp monoton?
58. Mengapa duplicate timestamp perlu diperiksa?
59. Bedakan raw dan processed data.
60. Apa fungsi statistik `dt min/median/max`?
61. Mengapa jumlah sampel lebih banyak belum tentu berarti kualitas lebih baik?
62. Bagaimana menangani header CSV yang berbeda?
63. Bandingkan kelebihan/kekurangan manual dan digital logging.
64. Apa yang harus diperiksa sebelum interpolasi missing data?

## P7 — MATLAB–Arduino
65. Apa fungsi Support Package?
66. Mengapa port harus diverifikasi?
67. Apa bedanya analog dan digital I/O?
68. Jelaskan kuantisasi ADC.
69. Mengapa loop MATLAB tidak deterministik seperti loop MCU?
70. Mengapa timestamp aktual harus disimpan?
71. Apa fungsi `diff(t)` pada analisis sampling?
72. Mengapa raw data harus tetap disimpan setelah filtering?
73. Jelaskan kalibrasi `y=m*x+b`.
74. Apa risiko extrapolation di luar dua titik kalibrasi?
75. Mengapa P7 menjadi prerequisite P9?

## Soal integrasi
76. Hubungkan P3 model orde satu dengan data P5/P6.
77. Bagaimana data P6 dapat digunakan untuk memperbarui model P3?
78. Mengapa sample time memengaruhi PID digital?
79. Apa yang terjadi bila satuan sensor salah tetapi grafik terlihat halus?
80. Buat workflow lengkap dari raw data sampai keputusan tuning.
81. Jika dua run mempunyai settling time berbeda, apa saja penyebab selain gain controller?
82. Jelaskan hubungan encoder P7/project PCB dengan praktikum motor berikutnya.
83. Mengapa pin map harus konsisten antara PCB, firmware, dan dokumentasi?
84. Beri contoh bukti yang lebih kuat daripada pernyataan “alat sudah bekerja”.
85. Kapan sebuah project seharusnya berstatus HOLD?

## Soal diagnosis cepat
Dosen dapat memberikan:
- grafik tanpa label;
- CSV dengan timestamp ganda;
- script MATLAB tanpa preallocation;
- transfer function dengan denominator salah;
- PID dengan output saturasi;
- pin map yang tidak konsisten;
- laporan tanpa raw data.

Mahasiswa diminta menyebutkan masalah, dampak, dan langkah verifikasi yang tepat.
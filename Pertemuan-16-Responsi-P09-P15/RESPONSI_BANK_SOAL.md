# Responsi Bank Soal P16

Bank soal ini digunakan untuk tanya jawab akhir P9–P15. Penguji dapat memilih soal secara acak dan meminta praktikan menunjuk source, data, atau grafik yang mendukung jawabannya.

## P9 — PID suhu MATLAB–Arduino
1. Apa perbedaan SP, PV, dan error?
2. Mengapa kalibrasi sensor dilakukan sebelum tuning?
3. Jelaskan pengaruh Kp yang terlalu kecil dan terlalu besar.
4. Mengapa Ki dapat mengurangi steady-state error?
5. Apa risiko Ki terlalu besar?
6. Mengapa derivative-on-measurement dipakai?
7. Apa arti output PID 0–100%?
8. Apa tujuan saturasi?
9. Apa tujuan anti-windup?
10. Mengapa timing MATLAB host tidak dianggap hard real-time?
11. Apa beda control interval dan output window?
12. Mengapa raw CSV perlu disimpan?

## P10 — Encoder, RPM, dan posisi
13. Jelaskan prinsip encoder quadrature A/B.
14. Apa beda PPR dan CPR dalam praktikum ini?
15. Mengapa decoder x4 dapat menghasilkan count lebih banyak daripada pulse satu channel?
16. Turunkan rumus posisi dari count dan CPR.
17. Turunkan rumus RPM dari delta count dan delta waktu.
18. Mengapa satuan `dt` harus diperhatikan?
19. Apa pengaruh CPR salah dua kali lebih besar?
20. Mengapa RPM mentah terlihat bertingkat pada speed rendah?
21. Apa fungsi moving average?
22. Apa fungsi LPF?
23. Bagaimana alpha memengaruhi noise dan delay?
24. Mengapa variabel count 32-bit dibaca atomik pada AVR 8-bit?
25. Apa arti transisi QDEC bernilai nol?
26. Bagaimana membuktikan tanda positif dan negatif konsisten?

## P11 — PID kecepatan
27. Gambarkan loop PID speed.
28. Mengapa feedback speed menggunakan RPM terfilter?
29. Apa risiko filter terlalu lambat?
30. Apa arti output PID bertanda?
31. Mengapa respons arah positif dan negatif perlu dibandingkan?
32. Bagaimana saturation memengaruhi interpretasi tuning?
33. Kapan integral seharusnya ditahan oleh anti-windup?
34. Apa fungsi heartbeat?
35. Apa yang harus diaudit bila feedback dapat negatif tetapi kontrol arah negatif gagal?
36. Mengapa metrics sebaiknya dihitung per segmen step?
37. Mengapa ZERO perlu mereset state estimator RPM?

## P12 — PID posisi
38. Apa beda feedback speed dan position?
39. Jelaskan `position_deg = count/CPR*360`.
40. Apa beda software zero dan homing mekanik?
41. Apa beda wrapped dan unwrapped position?
42. Mengapa position loop sering dapat dimulai dengan Ki=0?
43. Apa fungsi Kd pada kontrol posisi?
44. Bagaimana friction/dead-zone dapat menghasilkan residual error?
45. Mengapa repeatability perlu diuji?
46. Mengapa ZERO dilakukan dalam state berhenti?
47. Apa akibat mengubah reference saat controller masih aktif?

## P13 — PlatformIO dan workflow AI
48. Apa fungsi `platformio.ini`?
49. Apa beda build dan upload?
50. Mengapa ISR harus singkat?
51. Mengapa `Serial.print()` tidak ditempatkan di ISR encoder?
52. Apa fungsi `volatile`?
53. Mengapa firmware menggunakan scheduling non-blocking?
54. Apa fungsi command `STATUS`?
55. Apa yang harus diperiksa setelah AI mengubah source?
56. Mengapa compile sukses belum membuktikan algoritma benar?
57. Apa bukti bahwa sebuah perubahan AI telah diverifikasi?

## P14 — PID suhu embedded dan GUI
58. Apa perbedaan utama arsitektur P9 dan P14?
59. Apa fungsi GUI bila PID sudah dihitung di MCU?
60. Jelaskan protocol `TEMP_PID`.
61. Apa arti state STOP, RUN, dan FAULT?
62. Apa fungsi heartbeat antara GUI dan firmware?
63. Mengapa GUI demo tidak boleh dianggap sebagai model identifikasi plant nyata?
64. Data apa saja yang wajib direkam untuk menganalisis PID suhu?
65. Mengapa satu file multi-setpoint perlu dianalisis per segmen?
66. Bagaimana membedakan masalah sensor dari masalah tuning?

## P15 — PID motor embedded dan GUI
67. Jelaskan protocol `MOTOR_PID`.
68. Apa beda mode SPEED dan POSITION?
69. Mengapa output motor bertanda?
70. Apa fungsi `MAXPWM`?
71. Mengapa PWM dua arah tidak boleh aktif bersamaan pada implementasi baseline?
72. Apa fungsi ZERO pada mode position?
73. Mengapa ZERO juga perlu membersihkan histori estimator RPM?
74. Apa tujuan stall detection?
75. Apa keterbatasan stall detection sederhana berbasis command tinggi dan encoder tidak bergerak?
76. Mengapa mode switch dilakukan dalam state stop?
77. Data apa yang harus dibandingkan untuk menilai asimetri dua arah?
78. Mengapa raw, MA, dan LPF tetap disimpan walaupun PID memakai LPF?

## Integrasi dan debugging
79. Apa beda program berhasil compile dengan sistem kontrol tervalidasi?
80. Jika posisi salah skala tetapi arah benar, apa yang pertama diaudit?
81. Jika GUI tidak menampilkan telemetry, apa urutan pemeriksaannya?
82. Jika output terus saturasi, faktor apa saja yang perlu diperiksa?
83. Jika sistem berhenti sendiri, informasi apa yang dicari pada telemetry?
84. Mengapa satuan harus ditulis pada parameter dan grafik?
85. Bagaimana membedakan bug feedback dari gain PID yang buruk?
86. Mengapa source yang menghasilkan dataset harus disimpan bersama data?
87. Apa arti reproducibility pada praktikum kontrol?
88. Mengapa fault tidak boleh sekadar di-clear tanpa mencari penyebabnya?
89. Jelaskan alur requirement → source → build → data → metrics → conclusion.
90. Sebutkan tiga bukti yang membuat klaim “sistem sudah bekerja” lebih kuat daripada pengamatan visual saja.

## Panduan penilaian singkat
Jawaban dinilai layak bila praktikan:

- menggunakan istilah dan satuan yang benar;
- dapat menghubungkan konsep dengan source atau data sendiri;
- tidak mencampur PPR/CPR, speed/position, atau host/embedded timing;
- mampu menjelaskan sebab-akibat, bukan hanya definisi;
- dapat menunjukkan langkah audit ketika diberi gejala kesalahan.

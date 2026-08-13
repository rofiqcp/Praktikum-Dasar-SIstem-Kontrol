# Pertemuan 09 — PWM dan Baca Encoder Motor DC dengan Simulink

## Capaian Pembelajaran
- mengontrol PWM dua arah
- membaca encoder quadrature
- mengintegrasikan Simulink dan Arduino Mega

## Materi Inti

Materi menghubungkan MATLAB/Simulink dengan Arduino Mega 2560 untuk PWM motor dan pembacaan encoder. PWM mengatur rata-rata tegangan efektif motor, sedangkan encoder dua kanal menyediakan posisi, arah dan kecepatan.

Konvensi hardware materi: PWM pin **5 dan 6**, encoder pin **2 dan 3**. Simulink menghasilkan command, Arduino menggerakkan motor, encoder kembali sebagai feedback.


## Program yang Wajib Dijalankan
- `examples/build_pwm_encoder_model.m`

## Alur Praktikum
1. Install Simulink Support Package for Arduino Hardware.
2. Pilih target Arduino Mega 2560 dan serial 115200.
3. Buat PWM constant lalu monitor-and-tune.
4. Buat slider command -255..255 dengan pemetaan CW/CCW.
5. Baca encoder A/B.
6. Hitung posisi count dan kecepatan.
7. Jalankan `examples/build_pwm_encoder_model.m` untuk membuat skeleton model.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

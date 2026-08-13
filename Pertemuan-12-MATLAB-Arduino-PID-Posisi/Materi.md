# Pertemuan 12 — MATLAB–Arduino PID Posisi Motor DC

## 1. Loop position
`SP_deg → error_deg → PID → signed PWM → motor → encoder position_deg`

Posisi menggunakan encoder count langsung; tidak perlu diferensiasi untuk feedback utama, sehingga noise speed tidak dominan seperti P11.

## 2. Zero
Sebelum closed-loop, tetapkan posisi referensi: `ZERO,1`.

Zero software bukan limit switch. Jangan menganggap zero aman secara mekanik tanpa prosedur homing yang benar.

## 3. Saturasi
Position PID dapat memerintahkan PWM tinggi jika target jauh. Mulai `MAXPWM` rendah.

## 4. Integral
Pada position loop, integral sering kecil/0 terlebih dahulu. Jika mekanik memiliki friction/dead-zone, sedikit Ki dapat menghilangkan error residual tetapi meningkatkan overshoot/windup.

## 5. Derivative
Derivative on measurement/position membantu damping tetapi encoder quantization dapat menambah noise. Filter bila perlu.

## 6. Project
P12 adalah checkpoint project, sehingga `TugasVideo.md` diganti `Project.md`.

## 7. MATLAB
Firmware menjalankan PID. MATLAB mengirim target/gain dan merekam step response.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **PID posisi**. Program yang harus dibuka dan dipahami:
- `arduino_position_pid/arduino_position_pid.ino`
- `matlab_position_pid_experiment.m`
- `build_motor_position_pid_simulink.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Target sudut positif/negatif tercapai tanpa hard-stop dan STOP mematikan kedua arah.

## Validasi dan troubleshooting
Zero encoder sebelum eksperimen, mulai MAXPWM rendah, dan jangan gunakan target di luar ruang gerak mekanik.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

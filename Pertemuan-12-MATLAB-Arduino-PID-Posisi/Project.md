# Project P12 — PID Posisi Motor DC

## Tujuan
Membuktikan PCB trainer dapat melakukan closed-loop position dua arah dengan bukti data terukur.

## Deliverable
- firmware;
- MATLAB logger;
- parameter CPR;
- wiring;
- step +90, -90, dan target lain;
- CSV;
- PNG;
- Kp/Ki/Kd;
- response metrics;
- fault/STOP demonstration.

## Acceptance
- [ ] zero dapat dilakukan;
- [ ] +target bergerak arah benar;
- [ ] -target bergerak arah benar;
- [ ] PWM CW/CCW tidak aktif bersamaan;
- [ ] STOP mematikan motor;
- [ ] error akhir dicatat;
- [ ] overshoot dan settling dianalisis;
- [ ] mekanik tidak mencapai hard-stop pada eksperimen normal.

## Tantangan tambahan
Buat trajectory: `0 → +90 → -90 → +45 → 0`.

## Matriks percobaan minimum
Lakukan sekurangnya empat run: +90°, -90°, +45°, dan satu trajectory multi-target. Untuk setiap run catat Kp/Ki/Kd, MAXPWM, CPR, sample time, rise time, peak time, settling time, overshoot dan SSE.

## Bukti teknis
- screenshot upload/serial;
- foto arah motor dan encoder;
- CSV/PNG hasil MATLAB;
- source final;
- penjelasan anti-windup;
- uji host timeout/STOP;
- analisis mengapa gain yang dipilih aman terhadap hard-stop.

## Review source saat responsi
Praktikan harus dapat menunjukkan baris yang menghitung posisi, error, P/I/D, saturasi, PWM arah, ZERO dan STOP.

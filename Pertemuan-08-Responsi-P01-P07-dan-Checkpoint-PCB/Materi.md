# Pertemuan 8 — Responsi P1–P7 dan Checkpoint PCB

Pertemuan ini bukan materi baru. Fokusnya membuktikan bahwa fondasi teori, MATLAB, Autonics, DAQ, MATLAB–Arduino, dan hardware trainer sudah dipahami.

## Cakupan tanya jawab
- P1: closed-loop, PID, anti-windup.
- P2: MATLAB.
- P3: transfer function.
- P4: PID block manual.
- P5: Autonics manual.
- P6: DAQMaster.
- P7: MATLAB–Arduino.

## Checkpoint PCB
PCB minimal sudah:
- assembled;
- lolos visual;
- lolos continuity;
- rail low-voltage benar;
- LED/ADC/encoder input/PWM dummy/SSR dummy dapat diuji.

Gunakan `../../HARDWARE_PCB_SPEC.md`.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **responsi P1-P7 dan PCB checkpoint**. Program yang harus dibuka dan dipahami:
- `examples/pcb_bringup/pcb_bringup.ino`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Mahasiswa dapat menjawab konsep serta membuktikan continuity/power/I-O low-voltage trainer.

## Validasi dan troubleshooting
Tidak ada TugasVideo P8. Aktuator aktual boleh diganti dummy load saat bring-up awal.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

# Pertemuan 8 — Responsi P1–P7 dan Checkpoint PCB

## Tujuan
P8 bukan materi baru. P8 adalah gate akademik dan engineering sebelum semester masuk ke implementasi closed-loop berbasis Arduino.

Mahasiswa harus membuktikan dua hal:
1. memahami konsep P1–P7;
2. mempunyai desain/trainer PCB yang terdokumentasi dan layak melanjutkan tahap pengujian low-voltage.

## Cakupan responsi
### P1 — Dasar sistem kontrol
- open-loop vs closed-loop;
- setpoint, PV, error, feedback, disturbance;
- P, I, D;
- saturasi dan anti-windup;
- rise time, overshoot, settling time, SSE.

### P2 — MATLAB
- vector/matrix;
- indexing;
- plotting;
- table/CSV;
- loop dan preallocation;
- simulasi Euler.

### P3 — Transfer function
- definisi `G(s)`;
- pole/zero/DC gain;
- model pemanas orde satu;
- motor speed;
- motor position dan integrator;
- `step`, `stepinfo`;
- identifikasi orde satu.

### P4 — PID MATLAB/Simulink
- `feedback()`;
- P/PI/PID;
- pengaruh gain;
- `pidtune` sebagai alat bantu;
- blok P+I+D manual;
- saturasi dan validasi model.

### P5 — Data manual
- PV/SV;
- hysteresis;
- metadata eksperimen;
- stopwatch;
- repeatability;
- response metrics.

### P6 — DAQMaster
- alur data acquisition;
- konfigurasi yang harus dicatat;
- raw vs processed data;
- timestamp/missing data;
- perbandingan manual vs digital.

### P7 — MATLAB–Arduino
- Support Package;
- board/port;
- digital/analog I/O dasar;
- ADC dan kuantisasi;
- timestamp host-side;
- CSV logging;
- kalibrasi.

## Format responsi
Responsi dapat dilakukan dalam station:

1. **Station teori kontrol** — pertanyaan P1–P4.
2. **Station data** — interpretasi dataset P5–P6.
3. **Station MATLAB–Arduino** — jelaskan source P7 dan hasil pengukuran.
4. **Station PCB review** — schematic/layout/BOM/checklist.

Mahasiswa tidak hanya menghafal definisi. Dosen dapat memberikan grafik, potongan kode, atau dataset lalu meminta diagnosis.

## Checkpoint PCB
Pada P8, fokus penilaian adalah desain dan verifikasi low-voltage. Review minimal mencakup:
- schematic lengkap dan dapat dibaca;
- pin map konsisten dengan repository;
- power/net labeling jelas;
- konektor dan test point terdokumentasi;
- BOM sesuai schematic;
- layout mempunyai reference designator;
- jalur sensor/logic dapat ditelusuri;
- tidak ada net penting yang menggantung tanpa alasan;
- hasil continuity inspection terdokumentasi;
- power-on test hanya mengikuti prosedur lab yang telah disetujui.

## Pin map project semester
Gunakan satu sumber kebenaran yang sama di schematic, firmware, laporan, dan label PCB:

| Fungsi | Arduino Mega |
|---|---|
| encoder A | D2 |
| encoder B | D3 |
| motor command A | D5 |
| motor command B | D6 |
| temperature output control | D8 |
| temperature analog input | A0 |
| auxiliary analog input | A1 |

Jika desain kelompok berbeda karena revisi yang disetujui dosen, perubahan harus dicatat secara eksplisit dan semua source diperbarui konsisten.

## Design review questions
Mahasiswa harus dapat menjawab:
- dari mana setiap sinyal berasal dan menuju ke mana?
- apa level/satuan sinyal?
- apa kondisi output saat reset?
- bagaimana membedakan ground logic dan supply plant pada dokumentasi?
- test point mana yang dipakai saat troubleshooting?
- bagaimana mengetahui dua net tidak tertukar?
- bagaimana firmware mengetahui arah encoder?
- bagian desain mana yang paling berisiko salah assembly?

## Evidence-based checkpoint
Status PCB tidak cukup disebut “sudah jadi”. Bukti harus berupa:
- schematic PDF/image;
- layout screenshot;
- BOM;
- Gerber;
- foto top/bottom;
- pin map;
- inspection checklist;
- continuity log;
- low-voltage bring-up log dari prosedur lab;
- daftar issue dan corrective action.

## Status checkpoint
Gunakan klasifikasi:
- **PASS** — memenuhi gate P8;
- **PASS WITH ACTIONS** — dapat lanjut setelah action minor yang tercatat;
- **HOLD** — ada masalah yang harus diselesaikan sebelum tahap berikutnya.

## File pendukung
- `Project.md`
- `RESPONSI_BANK_SOAL.md`
- `PCB_REVIEW_CHECKLIST.md`
- `../HARDWARE_PCB_SPEC.md`
- `../SAFETY.md`

## Hasil akhir P8
Mahasiswa memiliki bukti bahwa konsep P1–P7 dikuasai dan project PCB mempunyai status review yang jelas. Issue yang belum selesai menjadi action list sebelum P9.
# Jobsheet P16 — Responsi dan Final Acceptance Test

## Tujuan
Melakukan pemeriksaan akhir seluruh jalur P9–P15 dan memastikan mahasiswa dapat menunjukkan bukti source, komunikasi, data, analisis, serta pemahaman konsep.

## File utama

```text
Materi.md
Project.md
RESPONSI_BANK_SOAL.md
FINAL_ACCEPTANCE_CHECKLIST.md
examples/final_smoke_test.py
```

## A. Persiapan bukti
Sebelum responsi, siapkan:

- source P9–P15 yang benar-benar digunakan;
- screenshot build sukses;
- data raw CSV;
- grafik;
- metrics;
- parameter tuning;
- P12 Project;
- hasil P14;
- hasil P15;
- prompt/review AI penting;
- smoke test P16.

Gunakan nama file yang jelas agar penguji dapat menelusuri source → data → kesimpulan.

## B. Pemeriksaan repository
Jalankan dari root repository:

```bash
python validate_repo.py
```

Catat hasilnya. Jika validator gagal, selesaikan error sebelum responsi.

Pemeriksaan minimum:

- P1–P16 ada;
- struktur `TugasVideo.md`/`Project.md` benar;
- program penting tersedia;
- Python dapat dikompilasi;
- tidak ada placeholder wajib.

## C. Smoke test serial

```bash
python Pertemuan-16-Responsi-P09-P15/examples/final_smoke_test.py --port COM5 --seconds 8
```

Linux contoh:

```bash
python Pertemuan-16-Responsi-P09-P15/examples/final_smoke_test.py --port /dev/ttyACM0 --seconds 8
```

Script memastikan state `RUN,0`, mengirim heartbeat/status, membaca protocol, menghitung jumlah telemetry, dan menyimpan JSON.

Isi hasil yang harus diperiksa:

```text
proto
telemetry_lines
field_counts
sample
pass
```

Smoke test tidak menggantikan acceptance function P14/P15; ia hanya memeriksa komunikasi dasar dalam state pasif.

## D. Station 1 — Konsep PID
Penguji meminta mahasiswa menjelaskan:

- error;
- P;
- I;
- D;
- derivative-on-measurement;
- saturation;
- anti-windup;
- rise time;
- overshoot;
- settling time;
- SSE.

Mahasiswa harus menghubungkan konsep dengan satu dataset sendiri.

## E. Station 2 — Sensor dan satuan
Tunjukkan:

- ADC → voltage;
- temperature conversion;
- encoder A/B;
- CPR;
- count → degree;
- delta count → RPM;
- raw/MA/LPF;
- sign positif/negatif.

Penguji dapat memberikan nilai sederhana untuk dihitung manual.

## F. Station 3 — Source firmware
Penguji memilih source P13/P14/P15 dan meminta mahasiswa menunjukkan:

- pin mapping;
- ISR;
- atomic read;
- command parser;
- PID update;
- saturation;
- anti-windup;
- heartbeat;
- STOP;
- fault;
- telemetry.

Mahasiswa harus menjelaskan fungsi baris, bukan sekadar menunjuk lokasi.

## G. Station 4 — Data dan diagnosis
Pilih satu CSV hasil praktikum.

Tunjukkan:

- metadata;
- SP;
- PV;
- error;
- P/I/D;
- output;
- fault bila ada;
- response metrics.

Penguji kemudian memberi satu gejala, misalnya:

- RPM selalu positif;
- posisi salah skala;
- output saturasi terus;
- GUI tidak parse data;
- sistem berhenti karena timeout.

Mahasiswa menjelaskan urutan audit untuk menemukan akar masalah.

## H. Station 5 — P12 Project
Tunjukkan:

- CPR;
- reference zero;
- target positif;
- target negatif;
- P/PD/PID comparison;
- repeatability;
- raw CSV;
- grafik;
- worksheet analisis.

Project dinilai dari kualitas evidence dan penjelasan, bukan hanya target tercapai.

## I. Station 6 — P14
Tunjukkan bukti:

- firmware build;
- GUI demo;
- protocol;
- logging;
- P/PI/PID comparison;
- response metrics;
- STOP/RUN/FAULT;
- heartbeat.

Jika pengujian trainer dilakukan, gunakan bukti dari prosedur laboratorium yang telah dijalankan; responsi tidak memerlukan improvisasi fault fisik.

## J. Station 7 — P15
Tunjukkan:

- firmware build;
- GUI demo;
- encoder signed;
- CPR;
- ZERO;
- speed positif/negatif;
- position positif/negatif atau dua target valid;
- raw/MA/LPF;
- PID terms;
- logging;
- fault/state.

Periksa bahwa source terbaru branch `v1` mereset estimator ketika ZERO sehingga tidak membawa histori RPM lama ke reference baru.

## K. Station 8 — Workflow AI
Tampilkan satu perubahan AI yang paling signifikan.

Format jawaban:

```text
Requirement:
Prompt:
Risiko yang diperiksa:
Perubahan yang diusulkan:
Review manual:
Build/test:
Keputusan akhir:
```

Penguji dapat meminta mahasiswa menunjukkan bagian yang ditolak atau diperbaiki dari jawaban AI.

## L. Final acceptance checklist
Isi `FINAL_ACCEPTANCE_CHECKLIST.md` bersama penguji.

Status hanya:

```text
PASS
REVISI
```

Jika REVISI, tulis bukti yang kurang dan tindakan koreksi yang diperlukan.

## M. Arsip final
Struktur yang direkomendasikan:

```text
NIM_Nama_P16/
  README.md
  source/
  hardware/
  p12_project/
  p14_temperature/
  p15_motor/
  ai_review/
  acceptance/
    smoke_test.json
    final_acceptance_checklist.md
  response/
```

## N. Gate lulus
- [ ] `validate_repo.py` PASS;
- [ ] source dapat ditunjukkan;
- [ ] data mentah tersedia;
- [ ] response metrics dapat dijelaskan;
- [ ] CPR dan sign benar;
- [ ] P12 project lengkap;
- [ ] P14 evidence lengkap;
- [ ] P15 evidence lengkap;
- [ ] smoke test valid;
- [ ] mahasiswa lulus tanya jawab konsep;
- [ ] mahasiswa dapat melakukan diagnosis berbasis data;
- [ ] workflow AI dapat dipertanggungjawabkan.

## Expected result
Pada akhir P16 tidak ada lagi bagian sistem yang hanya dianggap benar karena “terlihat jalan”. Setiap klaim utama harus mempunyai pasangan source, data, dan penjelasan.
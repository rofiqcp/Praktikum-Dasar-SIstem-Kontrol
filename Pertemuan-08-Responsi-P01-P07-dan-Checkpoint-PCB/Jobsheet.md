# Jobsheet Pertemuan 8 — Responsi P1–P7 dan Checkpoint PCB

## Format kegiatan
P8 dibagi menjadi empat station. Setiap kelompok membawa laptop, seluruh source P1–P7, dataset, dan dokumen project PCB.

## Station 1 — Teori kontrol P1–P4
Dosen memilih pertanyaan acak dari `RESPONSI_BANK_SOAL.md`. Mahasiswa harus mampu:
- menggambar diagram closed-loop;
- menjelaskan P/I/D;
- membaca grafik step response;
- menjelaskan transfer function;
- membedakan model speed/position;
- menjelaskan hasil `stepinfo`;
- menjelaskan PID built-in vs blok manual.

### Bukti minimum
- satu script MATLAB dijalankan;
- satu grafik dianalisis;
- satu persamaan diterangkan tanpa membaca jawaban.

## Station 2 — Data P5–P6
Mahasiswa membuka satu raw dataset manual dan satu raw dataset digital.

Wajib menjelaskan:
- metadata;
- sample interval;
- missing/duplicate data;
- peak;
- settling time;
- SSE;
- mengapa dua dataset layak/tidak layak dibandingkan.

## Station 3 — MATLAB–Arduino P7
Mahasiswa menunjukkan:
- Support Package/toolchain;
- source yang digunakan;
- bukti board/port;
- satu CSV hasil logging;
- statistik sample interval;
- konsep kalibrasi.

Pengujian menggunakan trainer low-voltage sesuai SOP laboratorium.

## Station 4 — PCB review
Gunakan `PCB_REVIEW_CHECKLIST.md` dan `Project.md`.

Review:
1. schematic;
2. pin map;
3. BOM;
4. layout;
5. Gerber;
6. foto assembly bila tersedia;
7. inspection/continuity log;
8. bring-up log dari prosedur lab;
9. issue list;
10. corrective action.

## Tabel issue
| ID | Temuan | Severity | Action | PIC | Status |
|---|---|---|---|---|---|
| PCB-01 | | Minor/Major/Hold | | | Open/Closed |

## Penilaian yang disarankan
| Bagian | Bobot |
|---|---:|
| teori P1–P4 | 30% |
| data P5–P6 | 20% |
| MATLAB–Arduino P7 | 20% |
| PCB checkpoint | 30% |

## Status akhir
Dosen memberi salah satu:
- PASS;
- PASS WITH ACTIONS;
- HOLD.

`HOLD` berarti issue wajib diselesaikan sebelum project digunakan pada tahap praktikum berikutnya.

## Deliverable P8
- lembar jawaban responsi;
- screenshot/source yang diminta station;
- raw dataset P5/P6;
- dokumentasi P7;
- package project PCB;
- `PCB_REVIEW_CHECKLIST.md` yang sudah diisi;
- issue/action list;
- `Project.md` checklist.

## Catatan
P8 tidak menggunakan `TugasVideo.md`. Penilaian dilakukan melalui responsi, demonstrasi terarah, dokumentasi, dan checkpoint project.
# Project P8 — PCB Control Trainer Checkpoint

## Tujuan project P8
P8 adalah design-review gate. Tujuannya memastikan schematic, layout, BOM, pin map, assembly evidence, dan hasil pemeriksaan low-voltage sudah cukup rapi sebelum trainer dipakai pada pertemuan berikutnya.

## Deliverable wajib
1. schematic source + PDF/image;
2. PCB layout source + screenshot;
3. BOM;
4. Gerber/fabrication output;
5. pin map;
6. foto top/bottom bila board sudah dirakit;
7. `PCB_REVIEW_CHECKLIST.md` terisi;
8. continuity/inspection log;
9. bring-up log dari prosedur laboratorium;
10. issue list + corrective action;
11. README singkat revisi PCB.

## Pin map baseline
| Fungsi | Pin |
|---|---|
| encoder A | D2 |
| encoder B | D3 |
| motor command A | D5 |
| motor command B | D6 |
| temperature control output | D8 |
| temperature analog input | A0 |
| auxiliary analog input | A1 |

Jika ada revisi resmi, lampirkan tabel perubahan dan pastikan schematic, source, label PCB, serta dokumentasi menggunakan mapping yang sama.

## Review schematic
- [ ] semua connector diberi nama;
- [ ] semua IC mempunyai reference designator;
- [ ] supply/net label jelas;
- [ ] pin Arduino yang dipakai sesuai tabel;
- [ ] input analog dapat ditelusuri sampai connector/test point;
- [ ] encoder A/B dapat ditelusuri;
- [ ] output digital dapat ditelusuri;
- [ ] tidak ada net penting yang menggantung tanpa alasan;
- [ ] nilai komponen sesuai BOM;
- [ ] catatan desain/revisi tersedia.

## Review layout
- [ ] footprint sesuai komponen;
- [ ] orientation marker jelas;
- [ ] connector mudah diidentifikasi;
- [ ] test point dapat diakses;
- [ ] reference designator tidak menutupi pad penting;
- [ ] net class dan clearance mengikuti aturan desain yang digunakan;
- [ ] tidak ada unrouted net;
- [ ] ground/supply routing ditinjau;
- [ ] file fabrication berhasil dihasilkan.

## Review assembly
- [ ] visual inspection top/bottom;
- [ ] tidak ada solder bridge yang terlihat;
- [ ] polaritas/orientasi komponen diperiksa;
- [ ] connector tidak tertukar;
- [ ] board dibersihkan dan diberi label revisi;
- [ ] setiap temuan diberi ID issue.

## Review continuity dan low-voltage
Pemeriksaan dilakukan sesuai SOP laboratorium. Catat hasil pass/fail, alat ukur, tanggal, dan operator. Project P8 tidak mengajarkan modifikasi instalasi daya berbahaya.

## Issue severity
- **Minor**: dokumentasi/label/rapi yang tidak mengubah fungsi dasar.
- **Major**: kesalahan yang dapat membuat fungsi I/O tidak sesuai.
- **Hold**: kondisi yang membuat board tidak boleh dilanjutkan ke pengujian berikutnya sampai diperbaiki.

## Tabel issue/action
| ID | Area | Temuan | Severity | Corrective action | PIC | Evidence close | Status |
|---|---|---|---|---|---|---|---|
| PCB-01 | | | | | | | |

## Acceptance gate
### PASS
Tidak ada issue Major/Hold terbuka dan dokumentasi lengkap.

### PASS WITH ACTIONS
Ada action minor yang tidak menghalangi tahap berikutnya, dengan PIC dan due action jelas.

### HOLD
Ada issue Major/Hold yang belum terselesaikan atau bukti review tidak cukup.

## Penilaian project
| Komponen | Bobot |
|---|---:|
| schematic dan pin-map consistency | 25% |
| layout dan fabrication package | 20% |
| BOM/assembly documentation | 15% |
| inspection dan test evidence | 20% |
| issue handling/corrective action | 10% |
| kemampuan menjelaskan desain | 10% |

## Struktur folder pengumpulan
```text
P08_Project_NIM_Nama/
  schematic/
  pcb/
  gerber/
  bom/
  photos/
  test-log/
  issue-list/
  README.md
```

## README project minimal
- versi/revisi PCB;
- tanggal;
- pin map;
- daftar fungsi;
- status PASS/PASS WITH ACTIONS/HOLD;
- issue terbuka;
- perubahan sejak P1;
- rencana menuju P9–P15.

## Kriteria akhir
Project P8 dinyatakan siap lanjut hanya setelah reviewer dapat menelusuri hubungan `requirement -> schematic -> PCB -> pin map -> evidence` tanpa menebak.
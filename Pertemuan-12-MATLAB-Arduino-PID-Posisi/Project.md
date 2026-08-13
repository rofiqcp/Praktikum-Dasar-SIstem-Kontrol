# Project P12 — PID Posisi Motor DC

## Tujuan
Membuktikan bahwa PCB trainer dan perangkat lunak pendukung mampu menghasilkan data kontrol posisi dua arah yang dapat dianalisis, dijelaskan, dan direproduksi.

## Berkas yang dikumpulkan
- source firmware yang digunakan;
- MATLAB logger/analyzer;
- nilai CPR dan shaft referensi;
- diagram koneksi yang sesuai dengan trainer;
- data target positif, target negatif, dan satu target tambahan;
- raw CSV;
- grafik PNG;
- nilai Kp, Ki, dan Kd;
- response metrics;
- `WORKSHEET_ANALISIS.md` yang telah diisi;
- bukti penanganan kondisi berhenti dan timeout sesuai workflow praktikum.

## Metadata setiap pengujian
Setiap dataset harus menyimpan atau mendokumentasikan:
- nama file;
- tanggal/waktu;
- CPR;
- referensi nol;
- target posisi;
- Kp, Ki, Kd;
- batas output;
- interval sampling;
- posisi awal;
- kondisi beban;
- catatan kejadian penting selama pengujian.

## Kriteria penerimaan
- [ ] referensi nol dijelaskan dan dicatat;
- [ ] target positif menghasilkan data dengan tanda yang konsisten;
- [ ] target negatif menghasilkan data dengan tanda yang konsisten;
- [ ] tidak ada ketidaksesuaian skala antara count, CPR, dan posisi;
- [ ] error akhir dicatat;
- [ ] overshoot dan settling time dianalisis;
- [ ] kondisi saturasi dibahas;
- [ ] repeatability dievaluasi menggunakan target yang sama lebih dari satu kali;
- [ ] raw CSV dan grafik hasil analisis tersedia;
- [ ] source yang menghasilkan data dapat ditunjukkan saat responsi.

## Rangkaian target untuk analisis
Gunakan rangkaian target konseptual:

```text
0 -> +90 -> -90 -> +45 -> 0
```

Tujuan rangkaian tersebut adalah mengevaluasi referensi, konsistensi tanda, respons pada beberapa target, dan repeatability. Response metrics dihitung per segmen target, bukan untuk seluruh rangkaian sekaligus.

## Matriks percobaan minimum
Lakukan sekurangnya empat dataset yang dapat dianalisis:

| Dataset | Target | Kp | Ki | Kd | Batas output | Rise | Overshoot | Settling | SSE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | +90 deg | | | | | | | | |
| 2 | -90 deg | | | | | | | | |
| 3 | +45 deg | | | | | | | | |
| 4 | target berulang/trajectory | | | | | | | | |

Jika kondisi awal atau beban berbeda, perbedaan tersebut harus disebutkan pada analisis.

## Analisis wajib
1. Jelaskan hubungan count, CPR, dan posisi dalam derajat.
2. Jelaskan referensi nol yang digunakan.
3. Bandingkan respons target positif dan negatif.
4. Bandingkan minimal dua konfigurasi controller.
5. Jelaskan pengaruh saturasi terhadap hasil tuning.
6. Jelaskan apakah integral diperlukan untuk mengurangi error residual.
7. Analisis repeatability.
8. Identifikasi minimal satu keterbatasan eksperimen.
9. Berikan satu usulan perbaikan yang dapat diuji pada eksperimen berikutnya.

## Bukti teknis
- screenshot proses komunikasi atau pencatatan data;
- CSV/PNG hasil MATLAB;
- source final;
- tabel parameter dan satuan;
- penjelasan anti-windup;
- penjelasan state berhenti/timeout;
- hasil `WORKSHEET_ANALISIS.md`;
- kesimpulan berbasis response metrics.

## Review source saat responsi
Praktikan harus mampu menunjukkan bagian program yang menghitung atau menangani:
- encoder count;
- posisi;
- setpoint dan error;
- P, I, dan D;
- anti-windup;
- saturasi;
- telemetry;
- referensi nol;
- state berhenti.

## Kesimpulan project
Project dinilai berhasil bila data dan source dapat menjawab tiga pertanyaan utama:
1. Apakah posisi dihitung dengan skala dan tanda yang benar?
2. Apakah controller dapat dijelaskan berdasarkan data, bukan hanya berdasarkan pengamatan visual?
3. Apakah hasil dapat diulang dengan referensi dan parameter yang terdokumentasi?

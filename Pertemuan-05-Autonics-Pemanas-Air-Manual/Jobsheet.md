# Jobsheet Pertemuan 5 — Data Manual Temperature Controller

## Tujuan
Mahasiswa membuat dataset manual yang dapat dibandingkan, kemudian menghitung karakteristik respon menggunakan Excel, Python, dan MATLAB.

## A. Siapkan lembar kerja
Gunakan copy dari `templates/template_pengamatan_pemanas_air.xlsx`. Isi metadata sebelum pengamatan: ID run, mode, target, nilai awal, interval pencatatan, kondisi plant, dan parameter yang diberikan pengajar.

## B. Dataset baseline
Catat kolom minimum:

```text
time_s,setpoint_C,temperature_C,notes
```

Gunakan waktu aktual. Jika satu sampel terlewat, tandai sebagai missing; jangan membuat nilai pengganti.

## C. Dataset perbandingan
Buat minimal tiga dataset dengan satu parameter eksperimen yang berbeda. Semua variabel lain didokumentasikan agar perbandingan dapat dipertanggungjawabkan.

| Run | Mode | Parameter | PV awal | SV | Interval | Catatan |
|---|---|---|---:|---:|---:|---|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |

## D. Repeatability
Ulangi salah satu konfigurasi. Periksa apakah bentuk respon dan metrics cukup mirip.

## E. Analisis Python
```bash
python examples/analyze_manual_response.py data_run.csv
python examples/compare_manual_runs.py runA.csv runB.csv runC.csv
```

## F. Analisis MATLAB
```matlab
run('examples/analyze_manual_response.m')
```

## G. Tabel hasil
| Run | Rise | Peak | Overshoot | Settling | SSE | Jumlah sampel |
|---|---:|---:|---:|---:|---:|---:|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |

## H. Analisis wajib
1. Run mana yang paling cepat menuju target?
2. Run mana yang memiliki overshoot terbesar?
3. Apakah interval pencatatan manual cukup untuk mengukur peak?
4. Seberapa konsisten run repeatability?
5. Apa sumber ketidakpastian terbesar dari pencatatan stopwatch?
6. Mengapa metadata kondisi awal penting?
7. Apa manfaat logging digital yang akan digunakan pada P6?

## I. Troubleshooting data
- Header CSV harus konsisten.
- Waktu harus monoton naik.
- PV/SV harus numerik dan memiliki satuan.
- Missing sample dicatat, bukan disembunyikan.
- Jika run berbeda jauh, periksa metadata sebelum membuat kesimpulan.

## Deliverable
1. seluruh raw data;
2. tabel metadata;
3. grafik setiap run;
4. grafik perbandingan;
5. response metrics;
6. jawaban analisis;
7. video sesuai `TugasVideo.md`.

Praktikum menggunakan setup laboratorium yang telah disiapkan. Perubahan instalasi daya bukan bagian dari jobsheet ini.
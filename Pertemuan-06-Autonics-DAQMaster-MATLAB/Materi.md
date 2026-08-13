# Pertemuan 6 — DAQMaster + Analisis MATLAB/Python

## Capaian
Mahasiswa mampu memahami alur akuisisi data digital, mendokumentasikan konfigurasi komunikasi laboratorium, memeriksa kualitas CSV, mengimpor data ke MATLAB/Python, dan membandingkan logging digital dengan pencatatan manual P5.

## Alur data

```text
perangkat -> interface komunikasi -> DAQMaster -> CSV -> analisis
```

P6 menekankan bahwa banyak data belum tentu berarti data berkualitas.

## Parameter yang dicatat
- model perangkat;
- ID/address;
- baud rate;
- parity dan stop bit;
- interface/converter;
- port komputer;
- interval logging;
- nama file raw.

Gunakan konfigurasi yang telah ditentukan laboratorium dan dokumentasikan setting yang dipakai.

## Workflow umum
1. buka project DAQMaster yang sesuai;
2. verifikasi nilai dan satuan yang tampil;
3. tampilkan trend graph;
4. aktifkan logging;
5. simpan raw log;
6. ekspor CSV;
7. simpan screenshot konfigurasi;
8. analisis copy data tanpa mengubah raw file.

Nama menu dapat berbeda menurut versi DAQMaster.

## Kualitas data
Periksa:
- timestamp monoton;
- duplicate timestamp;
- missing sample;
- kolom numerik;
- satuan;
- interval sampling;
- perubahan parameter yang tidak terdokumentasi.

## Statistik sampling
Untuk timestamp `t[k]`, hitung:

`dt[k] = t[k]-t[k-1]`

Laporkan minimum, median, maksimum, dan jumlah sampel. Perbedaan interval yang besar dapat memengaruhi interpretasi peak dan settling time.

## Struktur folder data
Gunakan pola:

```text
raw/        file asli
processed/  data yang sudah dinormalisasi
results/    grafik dan metrics
```

Raw data tidak diedit.

## MATLAB

```matlab
analyze_daqmaster('hasil.csv')
```

Analisis mencakup import tabel, pemetaan kolom waktu/PV/SV, plot, statistik interval, dan response metrics.

## Python alternatif

```bash
python examples/analyze_daqmaster.py hasil.csv
```

## Perbandingan run

```matlab
run('examples/compare_runs.m')
```

Setiap kurva harus memiliki label run dan metadata yang jelas.

## P5 vs P6
| Aspek | Manual | DAQ |
|---|---|---|
| interval | dipengaruhi operator | lebih konsisten |
| jumlah sampel | sedikit | lebih banyak |
| transcription error | lebih mungkin | lebih rendah |
| timestamp | kasar | lebih detail |
| setup komunikasi | tidak diperlukan | harus terdokumentasi |

## Eksperimen wajib
1. Analisis satu sample CSV repository.
2. Analisis minimal satu CSV hasil laboratorium.
3. Hitung statistik sampling.
4. Buat grafik dan metrics.
5. Bandingkan satu dataset P5 dan satu dataset P6 yang paling comparable.
6. Tulis sumber ketidakpastian pada kedua metode.

## Troubleshooting
- File tidak terbaca: periksa delimiter dan header.
- Nama kolom berbeda: buat mapping eksplisit.
- Timestamp datetime: ubah menjadi elapsed seconds.
- Missing data: hitung dan dokumentasikan sebelum memilih metode cleaning.
- Data tidak comparable: audit metadata dan kondisi awal.

## File wajib
- `examples/analyze_daqmaster.m`
- `examples/analyze_daqmaster.py`
- `examples/compare_runs.m`
- `sample_data/daq_export.csv`

## Jembatan ke P7
P6 menyelesaikan tahap data acquisition dari perangkat laboratorium. P7 memperkenalkan Arduino Mega sebagai perangkat I/O yang diakses langsung dari MATLAB sehingga mahasiswa memahami alur host–hardware sebelum masuk praktikum closed-loop berikutnya.
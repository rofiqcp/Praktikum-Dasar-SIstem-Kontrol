# Jobsheet Pertemuan 13 — PlatformIO ADC, Encoder, RPM, Posisi, dan AI

## Tujuan
Mahasiswa membangun dan memvalidasi firmware sensor Arduino Mega menggunakan PlatformIO, kemudian melakukan review terhadap satu perubahan berbantuan AI dengan bukti build dan data.

## Prasyarat
- P10 telah memvalidasi CPR dan arah encoder;
- P11/P12 telah mengenalkan penggunaan feedback motor;
- VS Code dan PlatformIO tersedia;
- Python tersedia bila menggunakan serial plotter;
- trainer laboratorium digunakan sesuai `../SAFETY.md`.

## File utama

```text
examples/mega_io_monitor/platformio.ini
examples/mega_io_monitor/src/main.cpp
examples/python_serial_plotter/plot_serial.py
PROMPT_AI_CONTOH.md
```

## A. Pre-test
Jawab sebelum praktikum:

1. Apa beda compile, upload, dan serial monitor?
2. Mengapa `encoderCount` diberi `volatile`?
3. Mengapa pembacaan variabel 32-bit perlu critical section pada AVR 8-bit?
4. Tuliskan rumus posisi dari count dan CPR.
5. Tuliskan rumus RPM dari delta count dan `dt`.
6. Apa pengaruh `TS` terhadap resolusi RPM?
7. Apa beda moving average dan LPF?
8. Mengapa AI output tetap harus di-review dan di-build?

## B. Audit project
Buka `examples/mega_io_monitor` dan identifikasi:

- board;
- framework;
- monitor baud;
- `ADC_PIN`;
- `ENC_A`;
- `ENC_B`;
- nilai CPR awal;
- interval sampling;
- alpha LPF;
- jumlah sampel moving average.

Catat nilai tersebut pada laporan sebelum mengubah apa pun.

## C. Build

```bash
cd Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_io_monitor
pio run
```

Bukti wajib:

- terminal menunjukkan build sukses;
- environment `megaatmega2560` benar;
- tidak ada error compile.

Jika build gagal, catat error pertama yang relevan dan tindakan koreksinya.

## D. Upload dan serial protocol
Setelah build sukses, lakukan upload sesuai trainer laboratorium kemudian monitor serial:

```bash
pio run -t upload
pio device monitor -b 115200
```

Header yang diharapkan:

```text
#PROTO,IO_MONITOR,2
#ms,adc_raw,voltage,count,position_deg,rpm_raw,rpm_ma,rpm_lpf
```

Catat apakah jumlah kolom data numerik selalu delapan.

## E. Uji ADC A1
Amati beberapa kondisi input analog yang disediakan trainer.

Catat minimal lima sampel:

| Sampel | ADC raw | Voltage | Perkiraan manual | Selisih |
|---:|---:|---:|---:|---:|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Gunakan:

```text
V = ADC * 5 / 1023
```

untuk memeriksa apakah konversi firmware konsisten dengan hitungan manual.

## F. Uji encoder bertanda
Gerakkan encoder pada dua arah yang didefinisikan oleh trainer.

Catat:

| Arah | Count awal | Count akhir | Delta count | Tanda posisi | Tanda RPM |
|---|---:|---:|---:|---:|---:|
| arah positif | | | | | |
| arah negatif | | | | | |

Acceptance:

- satu arah menghasilkan count positif;
- arah sebaliknya menghasilkan count negatif;
- tanda posisi dan RPM mengikuti count.

## G. Verifikasi CPR
Gunakan nilai hasil P10 sebagai referensi awal.

Kirim:

```text
CPR,<nilai_hasil_P10>
STATUS,1
```

Pastikan STATUS menampilkan nilai CPR yang benar.

Bandingkan satu putaran referensi dengan perubahan posisi sekitar 360°.

## H. Uji ZERO
Sebelum ZERO, simpan beberapa sampel RPM dan count. Kemudian kirim:

```text
ZERO,1
```

Yang harus terjadi:

- count kembali mendekati 0;
- posisi kembali mendekati 0°;
- histori RPM dibersihkan;
- tidak muncul lonjakan RPM palsu akibat `lastCount` lama.

Jika spike besar muncul setelah ZERO, jangan lanjut ke analisis filter sebelum source diperiksa.

## I. Uji interval sampling
Bandingkan minimal tiga konfigurasi:

```text
TS,20
TS,50
TS,100
```

Untuk setiap nilai, catat:

| TS | Resolusi teoretis RPM/count | Noise RPM raw | Respons | Catatan |
|---:|---:|---|---|---|
| 20 ms | | | | |
| 50 ms | | | | |
| 100 ms | | | | |

Gunakan:

```text
DeltaRPM = 60/(CPR*dt)
```

untuk menjelaskan hasil.

## J. Moving average dan LPF
Uji minimal:

```text
MA,1
MA,8
MA,16
ALPHA,0.1
ALPHA,0.25
ALPHA,0.8
```

Tidak semua kombinasi harus diuji. Pilih minimal tiga konfigurasi yang memungkinkan perbandingan jelas.

Isi tabel:

| MA | Alpha | Raw noise | MA delay | LPF delay | Kesimpulan |
|---:|---:|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

## K. Python serial plotter
Jalankan contoh plotter bila lingkungan Python siap:

```bash
python examples/python_serial_plotter/plot_serial.py
```

Jika port perlu diubah, dokumentasikan perubahan yang dilakukan. Plotter bersifat alat bantu; raw serial tetap harus dapat dijelaskan tanpa GUI.

## L. Review source
Praktikan harus menunjukkan bagian source yang menangani:

- `platformio.ini`;
- pin mapping;
- QDEC;
- ISR;
- atomic count snapshot;
- CPR;
- posisi;
- RPM;
- MA;
- LPF;
- command parser;
- ZERO;
- STATUS;
- telemetry.

## M. Tugas AI
Gunakan `PROMPT_AI_CONTOH.md` sebagai pola. Pilih satu pekerjaan rendah risiko, misalnya:

- meminta AI menjelaskan race condition pada encoder;
- meminta AI mereview rumus RPM dan satuan;
- meminta AI mereview logic reset ZERO;
- meminta AI memperjelas komentar/fungsi tanpa mengubah protocol;
- meminta AI membuat test vector quadrature offline.

Bukti yang dikumpulkan:

```text
requirement awal
prompt
jawaban/perubahan AI
diff sebelum-sesudah
hasil review manual
hasil pio run
hasil pengujian
keputusan: diterima / direvisi / ditolak
```

Jangan menerima perubahan hanya karena compile sukses.

## N. Pertanyaan analisis
1. Mengapa build sukses belum membuktikan CPR benar?
2. Apa yang terjadi jika `COUNTS_PER_REV` dua kali terlalu besar?
3. Mengapa sampling lebih cepat dapat menghasilkan RPM yang lebih kasar?
4. Mengapa filter yang terlalu halus dapat buruk untuk closed-loop cepat?
5. Mengapa `lastCount` harus ikut di-reset saat ZERO?
6. Apa keuntungan lookup table quadrature dibanding hanya membaca satu channel?
7. Mengapa `Serial.print` tidak ditempatkan di ISR?
8. Apa arti transisi QDEC bernilai 0?
9. Bagaimana membedakan bug sensor dari bug plotting?
10. Apa bukti bahwa perubahan AI benar-benar telah diverifikasi?

## O. Deliverable

```text
NIM_Nama_P13/
  source/
  build/
  raw/
  results/
  ai_review/
  screenshots/
  laporan.pdf
```

Minimal berisi:

- source yang dipakai;
- screenshot build sukses;
- header protocol;
- data ADC;
- data encoder dua arah;
- nilai CPR;
- perbandingan TS;
- perbandingan filter;
- bukti ZERO;
- prompt dan review AI;
- kesimpulan.

## P. Gate kelulusan
- [ ] `pio run` sukses;
- [ ] protocol sesuai;
- [ ] ADC valid;
- [ ] count bertanda benar;
- [ ] CPR terverifikasi;
- [ ] posisi sesuai skala;
- [ ] RPM positif/negatif valid;
- [ ] raw/MA/LPF dapat dijelaskan;
- [ ] ZERO tidak membuat spike palsu;
- [ ] command STATUS bekerja;
- [ ] review AI memiliki bukti build dan test.

## Expected result
Mahasiswa dapat mempertanggungjawabkan jalur data dari ADC/encoder sampai telemetry PlatformIO dan dapat menunjukkan satu workflow AI yang diverifikasi secara engineering.
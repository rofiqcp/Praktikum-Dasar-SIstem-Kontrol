# Jobsheet Pertemuan 1 — Dasar Sistem Kontrol dan Requirement PCB

## Tujuan
1. Mengidentifikasi elemen closed-loop.
2. Membandingkan open-loop dan closed-loop.
3. Mengamati pengaruh P, PI, dan PID.
4. Mengamati pengaruh perubahan plant.
5. Menyusun requirement awal PCB trainer.

## Persiapan
Install Python dependency bila belum tersedia:

```bash
python -m pip install numpy matplotlib
```

Masuk ke folder P1 dan jalankan:

```bash
python examples/control_basics.py
```

## Percobaan 1 — Baseline
Buka `examples/output/pid_basics.png`.

Catat:

| Item | Open-loop | Closed-loop |
|---|---|---|
| Ada feedback? | | |
| Output menuju SP? | | |
| Aksi berubah karena error? | | |
| Catatan | | |

Jelaskan mengapa kedua respon berbeda.

## Percobaan 2 — P rendah dan P tinggi
Buka `examples/control_basics.py`. Simpan nilai awal, lalu ubah **satu parameter pada satu waktu**.

Kasus yang disarankan:

| Kasus | KP | KI | KD |
|---|---:|---:|---:|
| P rendah | 0.6 | 0 | 0 |
| P sedang | 2.0 | 0 | 0 |
| P tinggi | 4.0 | 0 | 0 |

Setelah setiap perubahan, jalankan kembali program dan simpan screenshot dengan nama berbeda.

Catat:
- kecepatan respon;
- error akhir;
- overshoot bila ada;
- bentuk kurva.

## Percobaan 3 — PI dan PID
Uji minimal:

| Controller | KP | KI | KD |
|---|---:|---:|---:|
| PI | 2.0 | 0.35 | 0 |
| PID | 2.0 | 0.35 | 0.20 |

Bandingkan dengan P saja. Jelaskan fungsi integral dan derivative berdasarkan hasil yang terlihat.

## Percobaan 4 — Parameter sweep otomatis
Kembalikan `control_basics.py` ke baseline, lalu jalankan:

```bash
python examples/pid_parameter_sweep.py
```

Buka:

```text
examples/output/pid_parameter_sweep.png
```

Program menampilkan beberapa konfigurasi pada satu grafik agar perbedaan lebih mudah dibandingkan.

## Percobaan 5 — Perubahan plant
Ubah konstanta berikut pada `control_basics.py`:

```text
PLANT_K
TAU
```

Uji minimal:

| Kasus | PLANT_K | TAU |
|---|---:|---:|
| Baseline | 1.0 | 5.0 |
| Gain lebih kecil | 0.7 | 5.0 |
| Lebih lambat | 1.0 | 8.0 |

Sebelum run, tulis prediksi. Setelah run, bandingkan dengan hasil.

## Percobaan 6 — Brainstorming PCB
Buat diagram blok:

```text
Temp input -> A0               D8 -> SSR logic interface
                   Mega 2560
Encoder -> D2/D3               D5/D6 -> L293D -> Motor
```

Buat tabel requirement:

| Fungsi | Pin | I/O | Connector | Test point | Catatan |
|---|---:|---|---|---|---|
| Temp input | A0 | input | | | |
| Aux ADC | A1 | input | | | |
| Encoder A | D2 | input | | | |
| Encoder B | D3 | input | | | |
| Motor A | D5 | output | | | |
| Motor B | D6 | output | | | |
| SSR logic | D8 | output | | | |

Tambahkan kebutuhan:
- 5 V dan GND;
- supply motor;
- label silkscreen;
- konektor;
- test point;
- indikator yang diperlukan;
- kondisi output saat startup.

## Challenge
Pilih satu:
1. tambah satu kasus gain sendiri pada `pid_parameter_sweep.py`;
2. ubah SP pada simulasi dan jelaskan hasil;
3. buat diagram blok kontrol suhu dan motor secara terpisah;
4. buat draft BOM awal PCB trainer.

## Hasil yang dikumpulkan
- grafik baseline;
- tabel P/PI/PID;
- hasil parameter sweep;
- hasil perubahan plant;
- diagram blok PCB;
- pin map;
- jawaban analisis.

## Pertanyaan analisis
1. Apa beda SP, PV, dan error?
2. Mengapa feedback membantu koreksi plant?
3. Apa risiko feedback dengan tanda yang salah?
4. Mengapa Ki dapat mengurangi error akhir?
5. Apa itu windup?
6. Mengapa Kd sensitif terhadap noise?
7. Mengapa sampling time penting pada kontrol digital?
8. Mengapa satu tuning tidak otomatis cocok ketika `PLANT_K` atau `TAU` berubah?
9. Mengapa project PCB harus dimulai dari requirement dan pin map?
10. Jelaskan hubungan P1 dengan P2–P4.

## Checklist
- [ ] `control_basics.py` berjalan;
- [ ] `pid_parameter_sweep.py` berjalan;
- [ ] P, PI, PID dibandingkan;
- [ ] perubahan plant diuji;
- [ ] semua perubahan gain dicatat;
- [ ] diagram blok PCB dibuat;
- [ ] pin map dibuat;
- [ ] kesimpulan berbasis hasil simulasi.

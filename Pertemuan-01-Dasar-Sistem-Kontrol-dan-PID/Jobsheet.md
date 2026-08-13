# Jobsheet Pertemuan 1

## Tujuan
1. Mengidentifikasi elemen closed-loop.
2. Mengamati pengaruh Kp/Ki/Kd melalui simulasi.
3. Membuat requirement awal PCB trainer.

## Alat
- Laptop.
- Python 3.10+.
- `numpy`, `matplotlib`.

## Percobaan A — Open-loop
```bash
python examples/control_basics.py
```

Amati grafik open-loop. Catat:
- nilai akhir;
- apakah output mencapai SP;
- efek perubahan gain plant.

## Percobaan B — Closed-loop PID
Ubah di file:
- `KP`;
- `KI`;
- `KD`.

Lakukan minimal:
1. P saja;
2. PI;
3. PID.

Catat rise time, overshoot, settling secara kualitatif.

## Percobaan C — Requirement PCB
Buat tabel net:
`D5, D6, D2, D3, D8, A0, A1, 5V, GND, motor supply`.

Gambar diagram blok PCB.

## Hasil yang dikumpulkan
- screenshot/PNG grafik;
- tabel variasi Kp/Ki/Kd;
- diagram blok PCB;
- daftar komponen awal;
- jawaban analisis.

## Pertanyaan
1. Mengapa closed-loop lebih tahan perubahan plant?
2. Mengapa Ki dapat menyebabkan windup?
3. Mengapa D sensitif noise?
4. Mengapa heater membutuhkan time-proportional, bukan PWM kHz pada relay mekanik?
5. Apa risiko jika D5 dan D6 aktif bersamaan pada driver arah motor?

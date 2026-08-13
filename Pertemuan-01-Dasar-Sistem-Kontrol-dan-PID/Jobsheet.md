# Pertemuan 01 — Jobsheet — Simulasi Dasar Open/Closed Loop dan PID


## Persiapan
- Python 3.10+.
- `pip install -r ../requirements.txt` atau minimal `numpy scipy matplotlib`.

## Percobaan A — open loop
1. Buka `examples/control_basics.py`.
2. Jalankan `python control_basics.py`.
3. Amati respon plant first-order tanpa feedback.
4. Ubah `tau` menjadi 1, 2, 5; catat perubahan kecepatan respon.

## Percobaan B — closed loop P
1. Ubah `kp` = 0.5, 1, 2, 4.
2. Catat rise time, overshoot, dan steady-state error.
3. Jelaskan mengapa P saja dapat menyisakan offset.

## Percobaan C — PI/PID
1. Aktifkan `ki` bertahap.
2. Tambahkan `kd` kecil.
3. Simpan grafik.
4. Bandingkan P, PI, PID dengan tabel.

## Percobaan D — briefing PCB
Buat block diagram project: Arduino Mega → SSR → heater → sensor → Arduino, serta Arduino Mega → L293D → motor → encoder → Arduino.

## Bukti wajib
- terminal saat program berjalan;
- grafik P/PI/PID;
- tabel parameter dan metrik;
- gambar block diagram project PCB;
- penjelasan fail-safe output OFF saat reset.

## Pertanyaan analisis
1. Apa beda command controller dan keluaran plant?
2. Mengapa closed loop membutuhkan tanda feedback benar?
3. Apa akibat sensor terbalik pada PID?
4. Mengapa integral membutuhkan anti-windup?
5. Mengapa derivative mudah terganggu noise?

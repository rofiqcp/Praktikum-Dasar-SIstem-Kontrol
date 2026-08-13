# Pertemuan 11 — MATLAB–Arduino Kontrol PID Kecepatan Motor DC


## Tujuan
Menutup loop speed: setpoint RPM → PID MATLAB → PWM bertanda → L293D → motor → encoder → RPM.

## Struktur
`e_rpm = SP_rpm - rpm`. PID menghasilkan `u` -255…255. Positif menyalakan D5, negatif D6. Integral anti-windup mencegah akumulasi saat command saturasi.

## Sampling
Firmware mengirim RPM setiap 50 ms. MATLAB controller mengikuti data baru; jangan menghitung derivative dengan `Ts` yang diasumsikan jika data timestamp tersedia. Script contoh menggunakan selisih timestamp telemetri.

## Filter
Untuk encoder resolusi rendah, RPM per-window dapat berisik. Moving average/LPF boleh dipakai, tetapi filter menambah delay. Catat apakah feedback menggunakan raw atau filtered.

## Tuning eksperimen
Mulai Kp kecil, Ki=Kd=0; naikkan Kp; tambah Ki untuk error akhir; tambah Kd kecil bila perlu. Selalu batasi command dan start dari setpoint rendah.

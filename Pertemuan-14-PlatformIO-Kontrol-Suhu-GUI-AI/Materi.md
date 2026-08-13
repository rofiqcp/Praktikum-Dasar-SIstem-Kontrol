# Pertemuan 14 — PlatformIO Arduino Mega Kontrol Suhu + GUI Lengkap + AI


## Tujuan
Menjalankan PID temperatur sepenuhnya di Arduino Mega, mengatur parameter melalui serial, memonitor GUI Python, menyimpan CSV dan JPG, serta menghitung karakteristik respon.

## Arsitektur
`A0 temperature -> PID 10 Hz -> time-proportional SSR D8 -> heater` di MCU. PC hanya GUI/config/logger, sehingga controller tetap berjalan bila plotting lambat. Fail-safe komunikasi dapat dikembangkan sesuai trainer.

## Telemetry
Firmware mengirim: time, temp, SP, error, P, I, D, PID%, SSR. GUI menampilkan live plot dan menyimpan data.

## Command serial
`RUN,1`, `RUN,0`, `SP,50`, `KP,6`, `KI,0.08`, `KD,8`, `ZEROI`.

## AI workflow
Gunakan AI untuk memperbaiki UX/fitur, bukan mengganti validasi hardware. Setiap prompt harus diikuti build/test. Simpan history perubahan penting pada laporan.

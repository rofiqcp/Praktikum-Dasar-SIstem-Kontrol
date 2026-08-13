# Safety / Keselamatan Praktikum

## Prinsip utama

Repository ini mengendalikan aktuator nyata. Program yang terlihat benar tetap dapat menghasilkan gerakan motor, panas, arus besar, dan kondisi tak terduga akibat sensor lepas atau wiring salah.

## Pemanas air

Untuk mahasiswa, gunakan heater DC low-voltage atau trainer terisolasi bila memungkinkan.

Jika sistem menggunakan mains:
- jangan sambungkan mains ke breadboard;
- enclosure harus tertutup;
- gunakan proteksi arus dan kebocoran yang sesuai instalasi;
- grounding protektif harus benar;
- sisi mains dan low-voltage harus memiliki creepage/clearance yang sesuai;
- konektor tidak boleh dapat tersentuh saat energized;
- commissioning dilakukan dosen/teknisi kompeten;
- sediakan pemutus daya fisik yang dapat dijangkau;
- jangan mengandalkan software sebagai satu-satunya proteksi over-temperature.

Tambahkan thermal fuse/thermostat independen untuk plant aktual.

## Motor DC

- Mulai dengan supply rendah dan batas PWM kecil.
- Pastikan mekanik tidak dapat mengenai tangan/kabel.
- Lepas beban saat commissioning awal.
- STOP software harus diuji sebelum tuning PID.
- Cabut supply motor sebelum mengubah wiring encoder/driver.
- L293D memiliki batas arus; jangan dipakai untuk motor yang melebihi rating perangkat.

## Failsafe software wajib

Firmware P14/P15 menerapkan:
- actuator OFF saat boot;
- RUN harus diberikan eksplisit;
- sensor invalid → fault;
- timeout command/host → STOP bila mode membutuhkan host;
- output PID disaturasi;
- integral anti-windup;
- arah motor tidak pernah aktif bersamaan.

Proteksi software ini hanya lapisan tambahan, bukan pengganti proteksi hardware.

## Prosedur fault test

Sebelum eksperimen PID:
1. Start pada output rendah.
2. Tekan STOP dari GUI → aktuator harus OFF.
3. Putus sensor → sistem harus fault/STOP.
4. Tutup GUI/putus serial → periksa perilaku aman.
5. Restart Arduino → output harus tetap OFF sampai RUN.

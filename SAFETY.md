# Safety — Praktikum Sistem Kontrol

## Prinsip utama
1. Praktikum mahasiswa berfokus pada **sisi kontrol low-voltage** Arduino, sensor, encoder, L293D, dan input SSR.
2. Pemanas yang disarankan adalah pemanas DC bertegangan rendah atau plant trainer yang sudah terisolasi.
3. Bila menggunakan beban AC/mains, bagian tersebut harus berupa modul terpisah tertutup dan tidak diakses saat bertegangan.
4. Tombol emergency stop / master enable harus memutus energi aktuator, bukan hanya menghentikan program.
5. Motor harus memiliki batas mekanik aman untuk praktikum posisi; jangan membiarkan PID mendorong mekanisme ke hard-stop tanpa pembatas arus/command.

## Checklist sebelum ON
- catu Arduino dan catu motor/heater sesuai rating;
- common ground hanya pada sisi low-voltage yang memang dirancang common;
- polaritas sensor benar;
- output SSR default OFF saat reset;
- PWM motor default 0;
- tidak ada kabel terbuka pada bagian berbahaya;
- setpoint dan gain dimulai kecil;
- logging berjalan sehingga perilaku abnormal dapat dianalisis.

## Stop condition
Hentikan percobaan bila sensor tidak valid, temperatur melewati limit lab, motor macet, driver terlalu panas, arus berlebih, encoder tidak berubah saat motor bergerak, atau arah feedback salah.

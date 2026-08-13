# Wiring Utama Trainer Arduino Mega 2560

## 1. Pin map default

| Fungsi | Arduino Mega |
|---|---|
| PWM motor CW | D5 |
| PWM motor CCW | D6 |
| Encoder A | D2 |
| Encoder B | D3 |
| SSR heater | D8 |
| LED test | D13 |
| Sensor temperatur analog | A0 |
| ADC test/potensiometer | A1 |

Semua contoh program menggunakan tabel di atas kecuali disebutkan lain.

## 2. L293D + motor DC

Contoh satu kanal motor:
- `EN1` L293D dapat diikat HIGH jika arah/PWM diberikan melalui input PWM terpisah sesuai trainer, atau mengikuti desain shield yang digunakan.
- Pada desain praktikum repository ini, antarmuka abstrak firmware adalah `PWM_CW=D5` dan `PWM_CCW=D6`.
- Jangan pernah memberi PWM non-zero ke CW dan CCW bersamaan.
- Motor supply dan logic supply harus mengikuti rating L293D.
- Satukan ground sisi low-voltage.
- Tambahkan decoupling dekat IC dan terminal motor.

## 3. Encoder quadrature

- Encoder A → D2.
- Encoder B → D3.
- VCC encoder → sesuai rating sensor.
- GND encoder → GND Arduino.
- Bila output open-collector, gunakan pull-up yang sesuai.
- Untuk encoder panjang/berisik, gunakan wiring twisted pair/shield dan conditioning.

Firmware P13–P15 membaca transisi quadrature dan menghasilkan signed count.

## 4. SSR heater

- D8 hanya sinyal kontrol low-voltage menuju input SSR/isolator.
- GND low-voltage mengikuti tipe input SSR.
- Beban pemanas harus dipisahkan dari bagian Arduino.
- Untuk praktikum mahasiswa, prioritaskan heater DC low-voltage.

Jika menggunakan mains, lihat `SAFETY.md`; jangan menempatkan jalur mains pada breadboard.

## 5. Sensor temperatur

Baseline kode menganggap `A0` menghasilkan tegangan yang dapat dipetakan menjadi derajat Celsius.

Contoh LM35:
- 10 mV/°C.
- `tempC = voltage * 100`.

Jika memakai sensor lain:
- ubah hanya fungsi `readTemperatureC()`;
- jangan ubah PID/GUI;
- lakukan kalibrasi minimal 2 titik.

## 6. Potensiometer ADC P7/P13

- ujung 1 → 5V;
- ujung 2 → GND;
- wiper → A1.

Jangan memberi tegangan >5V atau <0V ke ADC Arduino Mega.

## 7. Checklist sebelum power

- [ ] Tidak ada short VCC-GND.
- [ ] Polaritas supply benar.
- [ ] Ground low-voltage tersambung.
- [ ] Motor bebas berputar.
- [ ] Encoder dapat dibaca dengan motor diputar tangan.
- [ ] Heater/SSR masih OFF saat boot.
- [ ] E-stop / pemutus daya diketahui lokasinya.

# Hardware PCB Control Trainer — Arduino Mega 2560

## 1. Sasaran
PCB/shield digunakan dari Pertemuan 8 sampai 16 untuk dua plant: pemanas air dan motor DC encoder. PCB **tidak membawa jalur mains AC**; hanya sisi logika, sensor, driver motor low-voltage, dan konektor input SSR.

## 2. Blok Fungsional
```text
Thermocouple/Temp Sensor ──> Interface ──> Arduino Mega ──> SSR Logic ──> External Isolated Heater Power Stage
Encoder A/B ─────────────────────────────> Arduino Mega ──> L293D ─────> DC Motor
USB Serial <─────────────────────────────> Arduino Mega <──────────────> Python / Node.js / MATLAB
```

## 3. Minimum I/O
- D2 encoder A interrupt
- D3 encoder B interrupt
- D5 PWM motor CW
- D6 PWM motor CCW
- D8 SSR control
- SPI header untuk MAX6675/MAX31855: MISO/SO, SCK, CS
- 5V, 3.3V, GND test points
- header UART/USB serial via Mega
- terminal motor dan supply motor terpisah dari 5V logika

## 4. L293D
Gunakan suplai logika 5V dan suplai motor sesuai motor. Pasang kapasitor decoupling dekat IC. Pastikan semua GND low-voltage common. Motor yang arus stall-nya melampaui kemampuan L293D **tidak boleh** digunakan; pakai driver yang sesuai jika perlu.

## 5. SSR
Arduino hanya mengendalikan terminal input DC SSR melalui konektor low-voltage. Verifikasi kebutuhan arus input SSR. Tambahkan LED indikator dan resistor seri. Sisi beban AC/heater ditempatkan di modul terpisah ber-enclosure.

## 6. Checklist PCB
- [ ] ERC/DRC lulus
- [ ] footprint Arduino Mega header benar
- [ ] polarity connector jelas
- [ ] test point 5V/3V3/GND/PWM/SSR/encoder
- [ ] label pin di silkscreen
- [ ] fuse low-voltage motor bila diperlukan
- [ ] decoupling 100 nF tiap IC + bulk capacitor rail motor
- [ ] tidak ada trace mains pada shield praktikum
- [ ] terminal SSR diberi label `SSR+` dan `SSR-` hanya untuk sisi input

## 7. Bring-up
Urutan pengujian: power rail → serial → encoder → L293D tanpa beban → motor low duty → sensor temperatur → output SSR dengan LED dummy → baru integrasi plant.

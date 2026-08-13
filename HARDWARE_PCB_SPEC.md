# Spesifikasi Project PCB — Arduino Mega Control Trainer

## 1. Tujuan
Membuat shield/PCB trainer yang dapat dipakai untuk **kontrol temperatur pemanas air** dan **kontrol motor DC kecepatan/posisi** dari MATLAB maupun firmware PlatformIO.

## 2. Arsitektur
### Jalur temperatur
- Arduino Mega 2560.
- Input temperatur utama: `A0` untuk sensor/transmitter low-voltage terkondisi 0–5 V.
- Header opsional termokopel digital/MAX6675: CS D49, SO D50, SCK D52.
- Output SSR: D8 melalui rangkaian driver yang sesuai input SSR.
- LED indikator SSR dan hardware enable.
- Konektor plant heater low-voltage; bila SSR mengendalikan mains, terminal mains **tidak ditempatkan di PCB logika mahasiswa**.

### Jalur motor DC
- L293D atau footprint/socket kompatibel.
- D5 = PWM CW, D6 = PWM CCW.
- D2 = Encoder A, D3 = Encoder B.
- Enable driver dapat ditarik HIGH melalui jumper atau pin terpisah.
- Supply motor terpisah dari 5 V logic, tetapi ground low-voltage disatukan sesuai desain.
- Header encoder dengan VCC, GND, A, B.
- Dioda flyback bila driver/varian IC yang digunakan memerlukannya sesuai datasheet.

## 3. I/O tambahan yang direkomendasikan
- potensiometer A1 untuk manual setpoint;
- push button START/STOP;
- LED status RUN/FAULT;
- test point 5V, GND, A0, D5, D6, D8, encoder A/B;
- konektor UART0 USB/serial tetap bebas untuk komunikasi PC.

## 4. Deliverable project
1. block diagram;
2. schematic;
3. perhitungan resistor/driver dasar;
4. BOM;
5. PCB layout + DRC;
6. Gerber dan drill;
7. assembly;
8. continuity test tanpa power;
9. bring-up low-voltage;
10. demo LED/ADC, motor manual, encoder, SSR low-voltage;
11. demo PID suhu, speed, dan position;
12. laporan perubahan/revisi.

## 5. Milestone
- **P1:** briefing dan pembagian fungsi.
- **P7:** komunikasi MATLAB–Arduino dan I/O dasar.
- **P8:** review schematic/layout + bring-up.
- **P9–P12:** validasi kontrol menggunakan MATLAB.
- **P13–P15:** validasi firmware PlatformIO + GUI.
- **P16:** responsi dan demo end-to-end.

## 6. Kriteria lulus hardware
- tidak short;
- Arduino dapat diprogram;
- A0 terbaca stabil;
- D8 mengaktifkan indikator/SSR input dengan benar;
- D5/D6 mampu menggerakkan motor dua arah;
- encoder A/B menghasilkan count bertanda;
- emergency/enable bekerja;
- tidak ada bagian mains terbuka pada area praktikan.

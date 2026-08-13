# Spesifikasi Project PCB Trainer — Arduino Mega 2560

## 1. Tujuan

Satu shield/trainer dipakai sepanjang semester untuk dua plant:

1. **Temperature control**: sensor suhu → Arduino Mega → SSR → heater.
2. **DC motor control**: encoder → Arduino Mega → L293D → motor.

PCB berada pada sisi **low-voltage control**. Sisi mains, jika dipakai, diletakkan pada modul terpisah yang sudah terproteksi.

## 2. Minimum I/O

| Net | Pin |
|---|---|
| MOTOR_PWM_CW | D5 |
| MOTOR_PWM_CCW | D6 |
| ENC_A | D2 |
| ENC_B | D3 |
| SSR_OUT | D8 |
| TEMP_ADC | A0 |
| AUX_ADC | A1 |
| LED_STATUS | D13 |

## 3. Blok PCB

### 3.1 Power
- Input 5V logic sesuai kebutuhan shield.
- Terminal motor supply terpisah.
- Bulk capacitor dekat driver.
- 100 nF decoupling dekat setiap IC.
- LED power.

### 3.2 Motor
- L293D socket/DIP atau footprint sesuai komponen.
- Terminal motor.
- Header encoder A/B/VCC/GND.
- Test point PWM_CW, PWM_CCW, ENC_A, ENC_B.
- Jangan menghubungkan dua output PWM arah secara bersamaan dalam firmware.

### 3.3 Temperature
- Header sensor analog.
- Output logic SSR.
- LED indikator command heater.
- Test point TEMP_ADC dan SSR_OUT.
- Opsi input sensor digital dapat disediakan pada header tambahan.

### 3.4 Debug
- Header UART/USB tetap dapat diakses.
- Semua net penting diberi silkscreen.
- Ground test point.
- Nomor revisi PCB dan nama kelompok.

## 4. Dokumen desain wajib

- schematic PDF;
- source schematic;
- PCB layout;
- Gerber;
- BOM;
- pin map;
- foto PCB;
- hasil continuity test;
- hasil test power;
- hasil test ADC;
- hasil test encoder;
- hasil test motor output tanpa beban;
- hasil test SSR dengan dummy LED/load low-voltage.

## 5. Acceptance test P8

### Test A — visual
Tidak ada solder bridge, polaritas komponen benar, silkscreen jelas.

### Test B — continuity
Dengan power OFF:
- VCC ke GND tidak short;
- pin Arduino ke net target benar;
- terminal driver ke pin target benar.

### Test C — power
Power low-voltage:
- rail sesuai target;
- tidak ada komponen panas abnormal;
- Arduino terdeteksi USB.

### Test D — I/O
- D13 blink.
- A1 membaca potensiometer.
- D2/D3 berubah saat encoder diputar.
- D5/D6 dapat menghasilkan PWM ke dummy load.
- D8 dapat mengendalikan LED/dummy SSR input.

## 6. Acceptance test final P16

Trainer harus menyelesaikan:
- PID temperature;
- speed measurement;
- position measurement;
- PID speed;
- PID position;
- GUI P14;
- GUI P15;
- logging;
- fault/STOP test.

Gunakan `RUN_CHECKLIST.md` dan `TESTING.md`.

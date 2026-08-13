# Instalasi Environment Praktikum

## 1. Software minimum

| Software | Kebutuhan |
|---|---|
| MATLAB + Simulink | P2–P12 |
| Control System Toolbox | P3–P4, analisis |
| Simulink | builder `.slx` |
| MATLAB Support Package for Arduino Hardware | P7, P9–P12 (opsional sesuai metode) |
| Autonics DAQMaster | P6 |
| Python 3.10+ | P1, P5–P6, P14–P16 |
| VS Code | P13–P15 |
| PlatformIO extension / CLI | P13–P15 |
| Node.js 20+ | P16 |
| Excel / LibreOffice Calc | P5–P6 |

## 2. Python

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Tes:

```bash
python validate_repo.py
```

## 3. MATLAB

Di MATLAB:

```matlab
repo = 'D:\Praktikum-Dasar-SIstem-Kontrol'; % sesuaikan
cd(repo)
addpath(genpath(repo))
savepath
```

Tes dasar:

```matlab
ver
which tf
which pid
which new_system
```

Jika `tf` tidak ditemukan, install Control System Toolbox.

## 4. Arduino Mega + MATLAB

Install Add-On:
**MATLAB Support Package for Arduino Hardware**.

Tes:

```matlab
a = arduino();
writeDigitalPin(a,'D13',1);
pause(1);
writeDigitalPin(a,'D13',0);
```

Jika otomatis tidak menemukan board, tentukan COM dan board:

```matlab
a = arduino('COM5','Mega2560');
```

## 5. PlatformIO

VS Code → Extensions → PlatformIO IDE.

Tes CLI:

```bash
pio --version
```

Buka folder project yang memiliki `platformio.ini`, bukan root repository.

## 6. Serial port

Windows: Device Manager → Ports (COM & LPT).

Linux:

```bash
ls /dev/ttyACM*
ls /dev/ttyUSB*
```

Jika Linux tidak mendapat izin:

```bash
sudo usermod -a -G dialout $USER
```

Logout/login kembali setelah perubahan group.

## 7. Node.js

```bash
node --version
npm --version
```

P16:

```bash
cd Pertemuan-16-Responsi-P09-P15/examples/node_serial_logger
npm install
```

## 8. Urutan commissioning yang disarankan

1. Jalankan validator repository.
2. Jalankan P1 Python.
3. Jalankan script P2–P4 di MATLAB tanpa hardware.
4. Bangun `.slx` dengan `build_all_slx`.
5. Test Arduino Mega LED.
6. Test ADC.
7. Test encoder tanpa motor diberi daya.
8. Test driver motor dengan PWM kecil.
9. Test GUI P14/P15 menggunakan `--demo`.
10. Baru hubungkan plant aktual.

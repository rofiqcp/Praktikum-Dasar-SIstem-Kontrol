<div align="center">

# 🎛️ Praktikum Dasar Sistem Kontrol
### MATLAB/Simulink • Autonics TK4S • Arduino Mega 2560 • Python • Node.js

![Modules](https://img.shields.io/badge/Pertemuan-16-success?style=for-the-badge)
![MATLAB](https://img.shields.io/badge/MATLAB-Simulink-orange?style=for-the-badge)
![Arduino](https://img.shields.io/badge/Arduino-Mega%202560-00979D?style=for-the-badge&logo=arduino)
![PlatformIO](https://img.shields.io/badge/PlatformIO-Ready-F5822A?style=for-the-badge&logo=platformio)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Node](https://img.shields.io/badge/Node.js-20+-339933?style=for-the-badge&logo=nodedotjs)

**Alur belajar:** teori kontrol → MATLAB → model plant → PID → eksperimen pemanas air → motor DC → embedded PID → GUI/DAQ → proyek terpadu.

</div>

---

## Tujuan Repository
Repository ini adalah paket praktikum 16 pertemuan dengan format konsisten seperti repository **Praktikum-Sistem-Embedded**: setiap pertemuan mempunyai **Materi.md**, **Jobsheet.md**, dan **TugasVideo.md**. Untuk pertemuan **8, 12, dan 16**, `TugasVideo.md` diganti dengan `Project.md`.

Setiap pertemuan menyertakan program yang dapat dijalankan, bukan hanya teori. Program mencakup MATLAB/Simulink, Python/Colab, PlatformIO Arduino Mega 2560, serta Node.js.

## Arsitektur Hardware Trainer
Target hardware utama adalah **Arduino Mega 2560 control trainer/shield** yang menyediakan dua jalur plant:

1. **Kontrol suhu pemanas air**
   - sensor temperatur/termokopel melalui modul antarmuka terisolasi atau MAX6675/MAX31855 pada sisi low-voltage,
   - output logika ke **SSR** untuk pemanas,
   - kontrol ON-OFF, P, PI, PID dan time-proportional.
2. **Kontrol motor DC**
   - driver **L293D**,
   - encoder quadrature A/B,
   - kontrol PWM dua arah,
   - PID kecepatan dan PID posisi.

> **Keselamatan:** PCB praktikum dirancang sebagai **sisi kontrol tegangan rendah**. Jalur AC/mains untuk pemanas tidak ditempatkan pada breadboard atau area logika Arduino. Jika beban pemanas menggunakan tegangan berbahaya, koneksi mains, proteksi fuse/RCD, enclosure, grounding, creepage/clearance, dan commissioning harus dilakukan oleh teknisi/dosen yang kompeten. Untuk pembelajaran awal gunakan pemanas DC bertegangan rendah atau plant trainer terisolasi.

## Struktur 16 Pertemuan

| P | Topik | Program utama | Output tugas |
|---:|---|---|---|
| 01 | Dasar sistem kontrol & PID + briefing PCB | Python simulasi closed-loop | TugasVideo |
| 02 | Dasar MATLAB | `.m` dasar plotting, matriks, script/function | TugasVideo |
| 03 | Transfer function: pemanas air, motor speed, motor position | MATLAB + notebook Colab | TugasVideo |
| 04 | PID MATLAB + blok PID dibuat sendiri | MATLAB + pembangun model Simulink | TugasVideo |
| 05 | Autonics + pemanas air, pencatatan manual stopwatch | CSV/Excel + Python analyzer | TugasVideo |
| 06 | Autonics lanjutan dengan DAQMaster | Python analyzer ekspor DAQ | TugasVideo |
| 07 | Finite State Machine dengan Stateflow | MATLAB + Stateflow | TugasVideo |
| 08 | **Project UTS: PCB Control Trainer** | PlatformIO hardware bring-up | **Project** |
| 09 | PWM & encoder motor DC Simulink | MATLAB generator model | TugasVideo |
| 10 | PID discrete + blok manual motor DC | MATLAB/Simulink | TugasVideo |
| 11 | PID speed & position + anti-windup | MATLAB/Simulink | TugasVideo |
| 12 | **Project autotuning PID motor DC** | MATLAB autotuning workflow | **Project** |
| 13 | PlatformIO PID motor + Python Qt GUI | C++ + Python | TugasVideo |
| 14 | PlatformIO PID pemanas air + SSR | C++ Arduino Mega | TugasVideo |
| 15 | Node.js DAQ/dashboard serial | Node.js | TugasVideo |
| 16 | **Project final integrated trainer** | Python smoke test + C++ + Python/Node | **Project** |

## Quick Start

```bash
git clone -b v1 https://github.com/rofiqcp/Praktikum-Dasar-SIstem-Kontrol.git
cd Praktikum-Dasar-SIstem-Kontrol
```

### Python
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python Pertemuan-01-Dasar-Sistem-Kontrol-dan-PID/examples/control_basics.py
```

### MATLAB
Buka MATLAB lalu jalankan contoh dari folder pertemuan:
```matlab
cd Pertemuan-03-Transfer-Function-Plant/examples
plant_transfer_functions
```

### PlatformIO
```bash
cd Pertemuan-13-PlatformIO-PID-Motor-DC-Python-GUI/examples/mega_pid_motor
pio run
pio run -t upload
pio device monitor -b 115200
```

### Node.js
```bash
cd Pertemuan-15-NodeJS-DAQ-Dashboard-Kontrol/examples/node_serial_logger
npm install
node index.js COM5 115200
```

## Konvensi Pin Arduino Mega 2560

| Fungsi | Pin default |
|---|---:|
| Motor CW / L293D EN-A PWM | 5 |
| Motor CCW / L293D EN-B PWM | 6 |
| Encoder A | 2 |
| Encoder B | 3 |
| SSR control | 8 |
| MAX6675 SCK | 52 |
| MAX6675 SO | 50 |
| MAX6675 CS | 49 |

Pin dapat diubah melalui konstanta pada source code. Untuk motor, contoh mengikuti materi: **PWM CW pin 5, PWM CCW pin 6, encoder pin 2 dan 3**.

## Format Laporan / Video
Tugas video harus memperlihatkan: identitas, teori singkat, pembuatan dari awal, program/model dijalankan, grafik/data hasil, analisis karakteristik respon, dan kesimpulan. Jangan hanya menampilkan source code tanpa eksperimen.

## Parameter Respon Sistem yang Dipakai
- delay time,
- rise time,
- peak time,
- settling time,
- maximum overshoot,
- steady-state error.

## Catatan Sumber Materi
Konten disusun ulang dan diperluas dari materi kuliah/praktikum yang tersedia: dasar sistem kontrol/PID, MATLAB-Simulink, Autonics TK4S-T4RN, PWM/encoder motor DC, PID speed/position, autotuning Sinestream/Superposition/PRBS, PlatformIO Arduino Mega dan Python GUI. Bagian P14-P16 adalah kelanjutan praktikum yang dirancang agar hardware PCB dan software menjadi satu jalur pembelajaran utuh.

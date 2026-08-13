<div align="center">

# 🎛️ Praktikum Dasar Sistem Kontrol
### MATLAB/Simulink • Autonics TK4S/T4RN • Arduino Mega 2560 • PlatformIO • Python GUI • Node.js

**16 pertemuan — teori → simulasi → eksperimen pemanas air → motor DC → embedded PID → GUI/DAQ → responsi**

</div>

---

## Tentang repository
Repository ini adalah paket praktikum **Dasar Sistem Kontrol** lengkap 16 pertemuan. Struktur mengikuti pola repository `Praktikum-Sistem-Embedded`: setiap pertemuan memiliki `Materi.md`, `Jobsheet.md`, serta `TugasVideo.md`. Khusus **Pertemuan 08, 12, dan 16**, `TugasVideo.md` diganti menjadi `Project.md`.

Semua pertemuan mempunyai sesuatu yang benar-benar dijalankan: script MATLAB `.m`, pembangun model Simulink `.slx`, Python/Colab, program Arduino/PlatformIO, GUI Python, atau Node.js sesuai topik. Model `.slx` dibuat secara deterministik oleh file `build_*.m`; jalankan builder sekali di MATLAB agar file `.slx` tersimpan pada folder `models/`.

> **Catatan model Simulink:** environment otomatis yang membuat repository ini tidak mempunyai runtime MATLAB/Simulink, sehingga file biner `.slx` tidak dipalsukan. Sebagai gantinya tersedia builder MATLAB lengkap yang membuat dan menyimpan `.slx` menggunakan API resmi `new_system`, `add_block`, `add_line`, dan `save_system`. Dengan demikian model dapat dibuat ulang dan diedit dari source.

## Silabus 16 pertemuan

| P | Materi | Praktik utama | Penilaian |
|---:|---|---|---|
| 01 | Dasar sistem kontrol, PID, briefing project PCB | Python simulasi open/closed loop + PID | TugasVideo |
| 02 | Dasar-dasar MATLAB | command, script, function, plot, matriks | TugasVideo |
| 03 | Transfer function plant pemanas air, motor speed, motor position | MATLAB + Colab | TugasVideo |
| 04 | PID MATLAB dan PID block dibuat sendiri | MATLAB + generator Simulink | TugasVideo |
| 05 | Autonics + pemanas air, pengambilan manual stopwatch | tabel Excel/CSV + analisis respon | TugasVideo |
| 06 | Autonics lanjutan + DAQMaster + MATLAB | export CSV DAQMaster → MATLAB | TugasVideo |
| 07 | Pengenalan MATLAB–Arduino | LED, ADC, plotting real-time | TugasVideo |
| 08 | Responsi P1–P7 + checkpoint PCB | tanya jawab, demo, review hardware | **Project** |
| 09 | MATLAB–Arduino kontrol suhu PID | water heater + SSR time proportional | TugasVideo |
| 10 | MATLAB–Arduino baca RPM dan posisi motor | encoder A/B, RPM, posisi | TugasVideo |
| 11 | MATLAB–Arduino PID kecepatan | PID speed + anti-windup | TugasVideo |
| 12 | MATLAB–Arduino PID posisi | PID position + evaluasi project | **Project** |
| 13 | PlatformIO + AI: ADC, RPM, posisi | VS Code/PIO Arduino Mega + Python serial plotter | TugasVideo |
| 14 | PIO Arduino Mega kontrol suhu + GUI + AI | grafik live, CSV, JPG, metrik respon | TugasVideo |
| 15 | PIO Arduino Mega kontrol speed/position + GUI + AI | grafik live, CSV, JPG, metrik respon | TugasVideo |
| 16 | Responsi P9–P15 | tanya jawab, live coding, demo trainer | **Project** |

## Project hardware semester
Mahasiswa membuat **PCB/shield Arduino Mega 2560** yang dipakai berulang dari P7 sampai P16. Hardware mempunyai dua jalur plant:

1. **Pemanas air:** input temperatur low-voltage, output logika SSR, hardware enable/interlock.
2. **Motor DC:** L293D, PWM dua arah, encoder quadrature A/B.

Spesifikasi lengkap ada di [`HARDWARE_PCB_SPEC.md`](HARDWARE_PCB_SPEC.md). Daftar program yang wajib dijalankan tiap pertemuan ada di [`RUN_CHECKLIST.md`](RUN_CHECKLIST.md).

### Konvensi pin default
| Fungsi | Arduino Mega |
|---|---:|
| Motor CW / L293D input-A PWM | D5 |
| Motor CCW / L293D input-B PWM | D6 |
| Encoder A | D2 |
| Encoder B | D3 |
| SSR control | D8 |
| Temperature analog conditioned input | A0 |
| MAX6675 CS (opsional) | D49 |
| MAX6675 SO | D50 |
| MAX6675 SCK | D52 |

## Quick start
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
```matlab
cd Pertemuan-03-Transfer-Function-Plant/examples
plant_transfer_functions
```

### Membuat file `.slx`
Dari root repository:
```matlab
build_all_slx
```
Builder akan membuat model P3, P4, P9, P11, dan P12 ke folder `models/` masing-masing. Untuk satu model saja, jalankan `build_*.m` pada folder `examples/` pertemuan terkait.

### PlatformIO
```bash
cd Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_sensors
pio run
pio run -t upload
pio device monitor -b 115200
```

### GUI Python
```bash
cd Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui
pip install -r requirements.txt
python app.py
```

### Node.js logger tambahan
```bash
cd Pertemuan-16-Responsi-P09-P15/examples/node_serial_logger
npm install
node index.js COM5 115200
```

## Format tugas video
Video harus memperlihatkan **pembuatan dari awal dan program benar-benar dijalankan**, bukan hanya membaca source. Minimal: identitas, teori singkat, wiring/model, source, proses build/run, hasil grafik/data, analisis karakteristik respon, kesimpulan, dan bukti file hasil.

## Parameter karakteristik respon
Praktikum memakai parameter berikut bila relevan: delay time, rise time, peak time, settling time, maximum overshoot, steady-state error, serta untuk motor ditambah RMSE/tracking error bila dibutuhkan.

## Keselamatan
Gunakan pemanas DC low-voltage/plant trainer terisolasi untuk praktikum mahasiswa. Jika SSR mengendalikan tegangan PLN, sisi mains **tidak boleh berada pada PCB logika/breadboard mahasiswa** dan harus berada dalam enclosure terproteksi, dengan fuse/RCD, grounding, strain relief, jarak isolasi, dan commissioning oleh personel kompeten. Lihat [`SAFETY.md`](SAFETY.md).

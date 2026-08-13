<div align="center">

# 🎛️ Praktikum Dasar Sistem Kontrol — Branch `v1`

**MATLAB/Simulink • Autonics TK4S/T4RN • Arduino Mega 2560 • PlatformIO • Python GUI • Node.js**

Repository ini adalah paket praktikum **16 pertemuan** yang dirancang agar mahasiswa bergerak dari konsep sistem kontrol dan PID, pemodelan MATLAB/Simulink, eksperimen pemanas air dengan Autonics, integrasi MATLAB–Arduino, hingga implementasi embedded PID dan GUI pada Arduino Mega 2560.

</div>

---

## 1. Target pembelajaran

Setelah menyelesaikan seluruh pertemuan, mahasiswa diharapkan mampu:

1. Menjelaskan open-loop, closed-loop, feedback, setpoint, error, plant, controller, sensor, dan aktuator.
2. Menurunkan dan mensimulasikan transfer function plant pemanas air, motor DC kecepatan, dan motor DC posisi.
3. Memahami kontribusi P, I, D, saturasi, anti-windup, sampling time, serta karakteristik respon sistem.
4. Mengoperasikan Autonics TK4S/T4RN pada plant pemanas air untuk ON/OFF, hysteresis, dan PID/time-proportional.
5. Mengambil data manual dengan stopwatch dan otomatis melalui DAQMaster, kemudian menganalisisnya di Excel/MATLAB/Python.
6. Mengintegrasikan MATLAB dengan Arduino Mega 2560 untuk LED, ADC, temperatur, encoder, RPM, posisi, PID kecepatan, dan PID posisi.
7. Menggunakan VS Code/PlatformIO untuk membuat firmware Arduino Mega dari awal.
8. Membuat GUI Python untuk commissioning, tuning, plotting, logging CSV/XLSX, ekspor JPG, serta evaluasi respon.
9. Menggunakan AI coding assistant dengan proses engineering yang benar: prompt → review → compile → hardware test → analisis.
10. Menyelesaikan trainer PCB Arduino Mega untuk dua plant: pemanas air melalui SSR dan motor DC melalui L293D + encoder.

---

## 2. Silabus 16 pertemuan

| P | Topik | Program/alat utama | Tugas |
|---:|---|---|---|
| 01 | Dasar sistem kontrol & PID + briefing project PCB | Python/Colab | TugasVideo |
| 02 | Dasar MATLAB | MATLAB `.m` | TugasVideo |
| 03 | Transfer function pemanas air, motor speed, motor position | MATLAB + Simulink builder + Colab | TugasVideo |
| 04 | PID MATLAB & PID block dibuat sendiri | MATLAB + Simulink builder | TugasVideo |
| 05 | Autonics + pemanas air, data manual stopwatch | Excel/CSV + Python | TugasVideo |
| 06 | Autonics + DAQMaster + analisis MATLAB | DAQMaster + MATLAB/Python | TugasVideo |
| 07 | MATLAB–Arduino: LED & ADC | MATLAB Support Package | TugasVideo |
| 08 | Responsi P1–P7 + checkpoint PCB | Test PCB | **Project** |
| 09 | MATLAB–Arduino kontrol suhu PID | Arduino Mega + MATLAB | TugasVideo |
| 10 | MATLAB–Arduino baca RPM & posisi motor | Encoder + serial/MATLAB | TugasVideo |
| 11 | MATLAB–Arduino PID kecepatan | Arduino Mega + MATLAB | TugasVideo |
| 12 | MATLAB–Arduino PID posisi | Arduino Mega + MATLAB | **Project** |
| 13 | PlatformIO + ADC/RPM/posisi + AI | VS Code + PlatformIO | TugasVideo |
| 14 | PlatformIO PID suhu + GUI lengkap | C++ + PyQt5 | TugasVideo |
| 15 | PlatformIO PID speed/position + GUI lengkap | C++ + PyQt5 | TugasVideo |
| 16 | Responsi P9–P15 + validasi akhir | Python/Node + hardware | **Project** |

**Khusus P8, P12, dan P16:** `TugasVideo.md` diganti dengan `Project.md`.

---

## 3. Hardware trainer

### 3.1 Jalur pemanas air
- Arduino Mega 2560.
- Sensor suhu analog pada `A0` sebagai baseline praktikum. Untuk thermocouple dapat diganti MAX6675/MAX31855 dan menyesuaikan fungsi pembacaan.
- Output SSR pada `D8`.
- Algoritma ON/OFF, hysteresis, P/PI/PID, dan time-proportional window.
- Failsafe: output heater OFF saat sensor invalid, timeout, STOP, atau fault.

### 3.2 Jalur motor DC
- L293D.
- PWM arah CW `D5`.
- PWM arah CCW `D6`.
- Encoder quadrature A `D2`.
- Encoder quadrature B `D3`.
- Kontrol speed dan position.
- Moving average + LPF.
- Anti-windup.
- Hard stop software pada STOP/fault/disconnect.

Lihat [`HARDWARE_PCB_SPEC.md`](HARDWARE_PCB_SPEC.md), [`WIRING.md`](WIRING.md), dan [`SAFETY.md`](SAFETY.md).

---

## 4. Quick start

### Python

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python validate_repo.py
```

Contoh P1:

```bash
python Pertemuan-01-Dasar-Sistem-Kontrol-dan-PID/examples/control_basics.py
```

### MATLAB

Tambahkan root repo ke path:

```matlab
repo = pwd;
addpath(genpath(repo));
```

Bangun seluruh model Simulink yang disediakan oleh builder:

```matlab
build_all_slx
```

Builder akan membuat `.slx` lokal dari API Simulink (`new_system`, `add_block`, `add_line`, `save_system`). Ini sengaja dipakai agar model dapat direproduksi dan tidak bergantung pada file biner yang tidak dapat diaudit.

### PlatformIO

Contoh P14:

```bash
cd Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid
pio run
pio run -t upload
pio device monitor -b 115200
```

Contoh P15:

```bash
cd Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid
pio run
pio run -t upload
pio device monitor -b 115200
```

### GUI Python

```bash
cd Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui
pip install -r requirements.txt
python app.py --demo
```

Mode `--demo` memungkinkan GUI diuji tanpa Arduino. Setelah siap:

```bash
python app.py
```

### Node.js

P16 menyediakan logger serial sederhana:

```bash
cd Pertemuan-16-Responsi-P09-P15/examples/node_serial_logger
npm install
node index.js COM5 115200
```

---

## 5. Konvensi data serial

Firmware P13–P15 memakai protokol teks line-based 115200 baud. Detail lengkap: [`shared/protocol/SERIAL_PROTOCOL.md`](shared/protocol/SERIAL_PROTOCOL.md).

Prinsipnya:
- command: `KEY,VALUE`
- telemetry: satu baris CSV
- setiap firmware memiliki header/versi protokol
- STOP harus langsung mematikan aktuator
- GUI tidak boleh bergantung pada urutan port OS yang tetap

---

## 6. Struktur setiap pertemuan

Setiap pertemuan minimal mempunyai:

```text
Materi.md
Jobsheet.md
TugasVideo.md
```

atau untuk P8/P12/P16:

```text
Materi.md
Jobsheet.md
Project.md
```

Folder `examples/` berisi program yang harus benar-benar dijalankan mahasiswa. Jika ada Simulink, folder `models/` berisi README dan model `.slx` dihasilkan oleh script builder `.m`.

---

## 7. Definition of Done praktikum

Satu pertemuan dianggap selesai bila mahasiswa dapat menunjukkan:

- wiring yang benar;
- program dibuka dari awal;
- program compile/run;
- output atau telemetri tampil;
- data disimpan;
- grafik dibuat;
- parameter respon atau hasil pengukuran dianalisis;
- kesimpulan ditulis;
- fault/STOP diuji untuk praktikum hardware.

Gunakan [`RUN_CHECKLIST.md`](RUN_CHECKLIST.md).

---

## 8. Keselamatan

Untuk praktikum awal, gunakan **pemanas DC tegangan rendah atau trainer terisolasi**.

Jangan menghubungkan mains langsung ke breadboard, header Arduino, atau PCB logika. Jika pemanas menggunakan tegangan berbahaya, sisi mains harus dikerjakan dan diperiksa oleh dosen/teknisi kompeten dengan enclosure, fuse/MCB/RCD yang sesuai, grounding, strain relief, creepage/clearance, emergency disconnect, dan prosedur lock-out.

Firmware/GUI pada repository ini **bukan pengganti proteksi hardware**.

---

## 9. Validasi repository

Jalankan:

```bash
python validate_repo.py
```

Validator memeriksa:
- P1–P16 ada;
- aturan `TugasVideo.md` vs `Project.md`;
- file program utama ada;
- Python dapat dikompilasi;
- `platformio.ini` ada pada P13–P15;
- builder Simulink ada;
- tidak ada placeholder `TODO` pada file wajib.

Lihat [`TESTING.md`](TESTING.md) untuk pengujian software dan hardware.

---

## 10. Referensi

Materi repo disusun ulang dari bahan praktikum yang diberikan, dokumentasi MATLAB/Simulink, bahan Autonics TK4S/T4RN dan DAQMaster, serta konsep umum kontrol modern/PID. Lihat [`REFERENSI_MATERI.md`](REFERENSI_MATERI.md).

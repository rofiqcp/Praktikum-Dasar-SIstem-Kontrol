# Pertemuan 16 — Responsi P9–P15 dan Integrasi Final

## Tujuan
Pertemuan 16 adalah gerbang akhir untuk memastikan mahasiswa memahami hubungan antara model, sensor, PID, firmware, GUI, data, dan troubleshooting. Kelulusan tidak ditentukan hanya oleh apakah program dapat dijalankan, tetapi oleh kemampuan menjelaskan dan membuktikan sistem berdasarkan source serta data.

## Cakupan responsi

```text
P09 : PID suhu MATLAB–Arduino
P10 : encoder, CPR, RPM, posisi
P11 : PID kecepatan
P12 : PID posisi + project checkpoint
P13 : PlatformIO, ADC, encoder, workflow AI
P14 : PID suhu embedded + GUI
P15 : PID motor embedded + GUI
```

## 1. Kompetensi integrasi
Mahasiswa harus dapat menjelaskan alur umum:

```text
setpoint
   ↓
controller
   ↓
output terbatas
   ↓
plant
   ↓
sensor
   ↓
feedback
   └──────── kembali ke controller
```

Untuk setiap plant, mahasiswa harus mampu menunjukkan:

- setpoint;
- process variable/feedback;
- error;
- P/I/D;
- output;
- saturation;
- state RUN/STOP/FAULT;
- telemetry;
- data hasil pengujian.

## 2. P9 — PID suhu host-side
Poin wajib:

- sensor dan kalibrasi;
- `SP-PV`;
- P/I/D diskrit;
- derivative-on-measurement;
- anti-windup;
- output 0–100%;
- perbedaan sampling host dan timing embedded;
- perbandingan P/PI/PID;
- response metrics.

Mahasiswa harus dapat menjelaskan mengapa hasil P9 menjadi dasar P14 tetapi arsitekturnya tidak identik.

## 3. P10 — encoder sebagai fondasi
Poin wajib:

- A/B quadrature;
- state transition;
- PPR vs CPR;
- x4 decoding;
- signed count;
- atomic read;
- posisi unwrapped;
- RPM dari delta count;
- interval sampling;
- moving average;
- LPF;
- konvensi arah.

Jika CPR atau tanda feedback salah, PID motor tidak boleh dianggap valid.

## 4. P11 — PID kecepatan
Mahasiswa harus dapat menjelaskan:

```text
SP rpm -> error -> PID -> output bertanda -> motor -> encoder -> rpm_lpf
```

Poin analisis:

- P/PI/PID;
- output positif/negatif;
- saturation;
- anti-windup;
- filter delay;
- asimetri arah;
- heartbeat;
- raw CSV dan metrics per segmen.

## 5. P12 — PID posisi
Poin wajib:

- count-to-degree;
- zero/reference;
- wrapped vs unwrapped;
- P/PD/PID;
- derivative-on-measurement;
- residual error;
- saturation;
- repeatability;
- target positif dan negatif;
- project evidence.

ZERO harus dipahami sebagai perubahan reference coordinate, bukan homing mekanik otomatis.

## 6. P13 — PlatformIO dan AI
Mahasiswa harus dapat menjelaskan:

- `platformio.ini`;
- build vs upload;
- ISR;
- atomic access;
- protocol serial;
- command parser;
- ZERO estimator state;
- parameter CPR/TS/MA/ALPHA;
- bagaimana AI direview.

Workflow AI yang diterima:

```text
requirement -> prompt -> review -> build -> test -> keputusan
```

Bukan:

```text
prompt -> copy -> dianggap benar
```

## 7. P14 — PID suhu embedded + GUI
Poin wajib:

- perbedaan dengan P9;
- PID dihitung di MCU;
- GUI sebagai supervisor/logger;
- protocol `TEMP_PID`;
- sensor conversion;
- anti-windup;
- output window;
- STOP/RUN/FAULT;
- heartbeat;
- CSV/XLSX/JPG;
- metrics;
- demo mode.

## 8. P15 — PID motor embedded + GUI
Poin wajib:

- protocol `MOTOR_PID`;
- mode SPEED/POSITION;
- signed output;
- encoder dua arah;
- CPR;
- raw/MA/LPF;
- ZERO;
- reset estimator;
- anti-windup;
- saturation;
- heartbeat;
- stall fault;
- logging dan analisis.

## 9. Response metrics
Mahasiswa harus mampu membedakan:

- delay time;
- rise time;
- peak time;
- maximum overshoot;
- settling time;
- steady-state error.

Metrik tidak boleh dibaca tanpa memahami bentuk eksperimen. File dengan beberapa setpoint harus dianalisis per segmen step yang jelas.

## 10. Audit satuan
Kesalahan satuan sering terlihat seperti bug PID. Penguji dapat meminta mahasiswa menelusuri:

```text
ADC count -> volt
encoder count -> degree
count/dt -> RPM
PWM count -> normalized command/tegangan model
rad/s -> RPM
rad -> degree
```

Mahasiswa harus dapat menunjukkan satuan pada setiap tahap.

## 11. Audit tanda
Untuk motor, audit harus dilakukan dari ujung ke ujung:

```text
SP -> error -> PID output -> arah plant -> encoder count -> feedback
```

Jangan memperbaiki tanda hanya pada grafik jika firmware menggunakan konvensi berbeda.

## 12. State dan fault
Mahasiswa harus dapat menjelaskan perbedaan:

```text
STOP
RUN
FAULT
```

serta mengapa fault tidak sama dengan error kontrol biasa.

Konsep yang diuji:

- boot state;
- STOP;
- heartbeat timeout;
- sensor invalid;
- over-temperature;
- stall;
- clear fault;
- perubahan mode/reference.

## 13. Final smoke test
Gunakan:

```bash
python examples/final_smoke_test.py --port COM5 --seconds 8
```

atau port sesuai sistem operasi.

Script ini bersifat pasif terhadap aktuator: ia memastikan state tidak RUN, meminta status, membaca protocol/telemetry, lalu menyimpan JSON.

Hasil smoke test digunakan sebagai bukti komunikasi, bukan pengganti semua pengujian fungsi.

## 14. Lima station responsi
Responsi dapat dibagi menjadi:

### Station A — konsep kontrol
P/I/D, saturation, anti-windup, metrics.

### Station B — sensor dan satuan
ADC, kalibrasi, quadrature, CPR, RPM, posisi.

### Station C — source firmware
ISR, PIDCore, protocol, heartbeat, state/fault.

### Station D — data
CSV, grafik, metrik, diagnosis berdasarkan log.

### Station E — integrasi project
PCB/trainer, software, GUI, reproducibility, dan acceptance evidence.

## 15. Evidence minimum
Mahasiswa harus membawa:

- source final;
- screenshot build sukses;
- data mentah;
- grafik;
- parameter;
- response metrics;
- hasil P12 project;
- hasil P14;
- hasil P15;
- smoke test P16;
- catatan perubahan AI yang signifikan.

## 16. Diagnosis berbasis gejala
### Feedback tidak berubah
Audit sensor/pin/ISR sebelum PID.

### Feedback salah skala
Audit CPR, kalibrasi, satuan, dan conversion function.

### Satu arah motor gagal
Audit sign end-to-end.

### Output selalu saturasi
Audit setpoint feasibility, gain, plant, dan limit.

### Integral besar
Audit anti-windup dan durasi saturasi.

### GUI tersambung tetapi grafik kosong
Audit protocol, jumlah kolom, baud, parser, dan header.

### Sistem berhenti sendiri
Audit fault/heartbeat melalui telemetry sebelum menaikkan gain.

## 17. Kriteria siap digunakan
Paket praktikum dianggap siap bila:

- seluruh P1–P16 mempunyai dokumen wajib;
- P8/P12/P16 memakai `Project.md`;
- program yang dirujuk tersedia;
- Python lolos syntax validation;
- firmware PlatformIO P13–P15 build;
- sketch Arduino P10–P12 dapat dikompilasi;
- protocol konsisten;
- Simulink builder tersedia;
- data dapat disimpan dan dianalisis;
- fault/state dapat dijelaskan;
- responsi mempunyai acceptance checklist dan bank soal.

## 18. Penilaian
Komposisi yang direkomendasikan:

| Komponen | Bobot |
|---|---:|
| konsep/tanya jawab | 25% |
| source dan debugging | 20% |
| sensor/satuan/data | 15% |
| project/integrasi | 20% |
| analisis response | 15% |
| dokumentasi | 5% |

## 19. Dokumen pendamping
Gunakan:

```text
Project.md
RESPONSI_BANK_SOAL.md
FINAL_ACCEPTANCE_CHECKLIST.md
examples/final_smoke_test.py
```

## Hasil akhir
Mahasiswa dinyatakan menguasai rangkaian praktikum bila dapat menjelaskan sistem dari requirement sampai evidence, menunjukkan data yang konsisten dengan source, menemukan akar masalah dari gejala, dan membedakan antara “program berjalan” dengan “sistem kontrol tervalidasi”.
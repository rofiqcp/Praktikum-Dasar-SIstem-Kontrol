# Tugas Video Pertemuan 9 — PID Suhu MATLAB–Arduino

## Tujuan video
Membuktikan mahasiswa memahami implementasi PID suhu dari sensor sampai analisis data, bukan hanya memperlihatkan plant bekerja.

## Durasi yang disarankan
8–15 menit, dipadatkan melalui potongan proses dan grafik. Jangan mempercepat bagian penjelasan teknis sampai sulit dibaca.

## Struktur wajib

### 1. Pembukaan
Tampilkan:
- nama/NIM;
- judul P09;
- tujuan;
- diagram blok `SP -> PID -> output -> plant -> sensor -> PV`.

### 2. Sensor dan kalibrasi
Jelaskan:
- pin input;
- satuan tegangan;
- fungsi kalibrasi;
- minimal tiga titik referensi;
- slope dan offset hasil kalibrasi.

Tunjukkan `temperature_sensor_calibration.m` dijalankan.

### 3. PID diskrit
Jelaskan persamaan:

```text
P = Kp*e
I = I + Ki*e*Ts
D = -Kd*dPV/dt
u = sat(P+I+D,0,100)
```

Jelaskan mengapa terdapat saturasi dan anti-windup.

### 4. Simulasi sebelum hardware
Jalankan `temp_pid_offline_simulation.m` dan tunjukkan minimal P, PI, dan PID. Jelaskan perbedaan respon dengan istilah rise time, overshoot, settling time, dan SSE.

### 5. Source MATLAB host
Buka `matlab_temp_pid_host.m` dan tunjukkan bagian:
- konfigurasi SP/gain;
- pembacaan A0;
- error;
- P/I/D;
- anti-windup;
- output limit;
- time-proportional logic;
- cleanup/failsafe software.

### 6. Bukti eksperimen
Pada trainer laboratorium yang telah disiapkan, tampilkan data satu run representative. Video tidak perlu menunggu seluruh eksperimen real-time; boleh gunakan potongan awal, pertengahan, dan akhir asalkan data CSV asli ikut dikumpulkan.

### 7. P vs PI vs PID
Tampilkan grafik tiga run dan tabel parameter. Jelaskan tuning mana yang dipilih dan alasannya berdasarkan metrics.

### 8. Analisis CSV
Jalankan `analyze_temp_pid_log.m`. Tampilkan grafik:
- SP/PV;
- error;
- P/I/D;
- output %.

### 9. Perbandingan dengan Autonics
Bandingkan P9 terhadap P5/P6: algoritma, logging, sample timing, fleksibilitas, dan response metrics.

### 10. Penutup
Sampaikan:
- temuan utama;
- sumber error/ketidakpastian;
- parameter terbaik menurut data;
- satu perbaikan yang akan dilakukan bila eksperimen diulang.

## Bukti yang tidak boleh hilang
- source terlihat di layar;
- command/script benar-benar dijalankan;
- data kalibrasi;
- minimal tiga konfigurasi P/PI/PID;
- CSV/PNG/metrics;
- kondisi awal dan parameter dicantumkan;
- penjelasan anti-windup dan cleanup.

## File pendamping
```text
NIM_Nama_P09_source/
NIM_Nama_P09_raw/
NIM_Nama_P09_results/
NIM_Nama_P09_video_link.txt
```

## Rubrik
| Aspek | Bobot |
|---|---:|
| pemahaman sensor dan kalibrasi | 15% |
| pemahaman PID diskrit | 20% |
| bukti program dijalankan | 20% |
| kualitas eksperimen dan data | 15% |
| analisis response metrics | 20% |
| struktur video dan kesimpulan | 10% |

## Kesalahan yang mengurangi nilai
- hanya membaca slide;
- tidak menunjukkan source;
- tidak menyertakan raw data;
- menyebut PID terbaik tanpa metrics;
- kondisi awal setiap run tidak dicatat;
- konversi sensor tidak dijelaskan;
- tidak menjelaskan apa yang terjadi saat output saturasi.
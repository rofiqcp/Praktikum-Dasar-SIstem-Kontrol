# Tugas Video Pertemuan 4 — PID MATLAB dan PID Manual Simulink

## Durasi
Disarankan 7–12 menit.

## Isi wajib

### 1. Diagram closed-loop
Jelaskan hubungan setpoint, error, controller, plant, output, dan feedback negatif.

### 2. P, PI, PID
Tampilkan hasil eksperimen P, PI, dan PID. Untuk setiap controller sebutkan gain dan minimal dua parameter respon dari `stepinfo`.

### 3. Gain sweep
Tunjukkan minimal dua nilai Kp dan dua nilai Ki. Jelaskan perubahan respon berdasarkan hasil simulasi.

### 4. `pidtune`
Jalankan `pidtune` dan bandingkan gain/result dengan tuning manual kelompok. Jelaskan bahwa tuning otomatis tetap harus dievaluasi.

### 5. PID manual Simulink
Jalankan:

```matlab
run('examples/build_pid_manual_simulink.m')
```

Buka model hasil dan tunjukkan jalur:
- error;
- P;
- I + Integrator;
- derivative/filter;
- penjumlahan P+I+D;
- plant;
- feedback;
- Scope.

### 6. Verifikasi
Bandingkan hasil PID manual dengan PID built-in menggunakan gain yang sama. Jelaskan penyebab jika kurva berbeda.

### 7. Kesimpulan
Sampaikan pengaruh Kp, Ki, dan Kd serta hubungan P4 dengan implementasi digital berikutnya.

## Bukti yang wajib terlihat
- source MATLAB;
- Command Window saat run;
- `stepinfo`;
- grafik P/PI/PID;
- model Simulink manual;
- nilai gain yang digunakan.

## Rubrik

| Komponen | Bobot |
|---|---:|
| Pemahaman closed-loop | 15% |
| Analisis P/PI/PID | 25% |
| Penggunaan metrics | 20% |
| PID manual Simulink | 25% |
| Verifikasi dan kesimpulan | 15% |

## Format nama

```text
P04_NIM_Nama_PID_MATLAB
```

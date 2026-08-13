# Jobsheet P15 — PID Speed & Position + GUI

## A. Persiapan
- Arduino Mega 2560.
- Trainer/shield PCB.
- Motor DC berencoder.
- L293D dan catu motor sesuai rating.
- USB data cable.
- VS Code + PlatformIO.
- Python environment dari `INSTALLATION.md`.

Pastikan motor bebas berputar, tidak ada bagian mekanik yang dapat menjepit, dan catu motor masih OFF saat pertama upload.

## B. Build firmware
```bash
cd Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid
pio run
pio run -t upload
pio device monitor -b 115200
```
Output awal yang benar harus memiliki `#PROTO,MOTOR_PID,3` dan header telemetry.

## C. Bring-up tanpa catu motor
1. Pastikan D5/D6 LOW pada boot.
2. Putar poros dengan tangan.
3. Pastikan `position_deg` berubah dan tanda arah konsisten.
4. Putar satu putaran, verifikasi CPR. Ubah dengan `CPR,xxx` bila perlu.
5. Tes `ZERO,1` — posisi harus kembali dekat 0°.

## D. Uji driver open-loop terbatas
Sebelum closed-loop, gunakan firmware hanya setelah arah kabel diperiksa. Mulai `MAXPWM` <= 80. Jika arah mekanik dan tanda encoder berlawanan dengan konvensi, perbaiki kabel motor atau urutan encoder secara konsisten; jangan “menambal” hanya satu jalur kontrol.

## E. GUI demo
```bash
cd ../gui
python app.py --demo
```
Uji seluruh tombol, mode, checkbox, clear dan export. Demo harus bisa berjalan tanpa Arduino.

## F. GUI hardware
```bash
python app.py
```
1. Refresh port -> pilih Arduino -> Connect.
2. Verifikasi status `CONNECTED` dan fault 0.
3. Atur CPR dan MAXPWM rendah.
4. Mode SPEED, setpoint awal 50–100 rpm.
5. Start; amati SP, raw, MA, LPF, error dan PID.
6. Stop sebelum mengganti mode.
7. Pilih POSITION. GUI otomatis stop + zero encoder.
8. Target awal 30° atau 45°, kemudian Start.

## G. Percobaan wajib speed
Lakukan minimal 4 konfigurasi: P saja, PI, PID, dan PID dengan setpoint negatif. Untuk setiap run simpan CSV/XLSX/JPG dan catat Kp Ki Kd, alpha, MA, Ts, CPR, MAXPWM.

## H. Percobaan wajib position
Lakukan minimal target +90°, 0°, -90° dengan PWM limit aman. Uji pergantian target setelah posisi stabil. Jangan menguji target yang melewati batas mekanik trainer.

## I. Analisis
Untuk run terpilih jalankan:
```bash
python analyze_saved_run.py hasil.csv
```
Bahas rise time, peak time, settling time, overshoot, SSE, pengaruh filter, saturasi dan stall.

## J. Fault test
Dengan motor tidak RUN, pahami kode fault. Untuk menguji host timeout cukup Start dengan roda bebas lalu tutup GUI; firmware harus menghentikan PWM. Jangan sengaja menahan poros dengan tangan untuk membuat stall.

## K. Checklist kelulusan
- [ ] encoder signed benar dua arah
- [ ] CPR terkalibrasi
- [ ] PWM CW/CCW tidak aktif bersamaan
- [ ] RUN/STOP bekerja
- [ ] host timeout menghentikan motor
- [ ] speed positif dan negatif bekerja
- [ ] position positif dan negatif bekerja
- [ ] anti-windup terlihat saat saturasi
- [ ] CSV/XLSX/JPG tersimpan
- [ ] metrik respon dihitung
- [ ] video memperlihatkan hardware dan grafik nyata

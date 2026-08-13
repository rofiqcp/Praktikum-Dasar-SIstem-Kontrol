# Pertemuan 15 — PlatformIO Arduino Mega: PID Kecepatan & Posisi Motor DC + GUI + AI

## Capaian pembelajaran
Mahasiswa mampu membangun sistem kontrol motor DC lengkap dari sensor hingga antarmuka: membaca encoder quadrature, menghitung posisi dan kecepatan bertanda, memfilter kecepatan, menjalankan PID speed/position dengan anti-windup, menggerakkan L293D dua arah, melakukan tuning, merekam data dan menganalisis respons.

## Arsitektur sistem

```text
GUI Python / AI editor
      | serial 115200
      v
Arduino Mega 2560
  |-- Encoder A/B D2,D3 -> count -> posisi -> RPM raw -> MA -> LPF
  |-- PID speed / PID position
  |-- PWM signed -255..255
      v
L293D: D5=CW, D6=CCW -> Motor DC
```

Hardware pin default mengikuti trainer mata kuliah: PWM CW D5, PWM CCW D6, encoder A D2 dan encoder B D3. Semua ground sisi low-voltage harus common. Catu motor **tidak** diambil dari pin 5 V Arduino.

## 1. Encoder quadrature
Encoder A/B menghasilkan urutan Gray-code. Program menyimpan keadaan AB sebelumnya dan menggunakan tabel transisi 16 elemen. Hasil `encoderCount` bertanda sehingga arah CW dan CCW dapat dibedakan.

Jika `CPR` adalah jumlah count per putaran yang benar-benar dihasilkan oleh decoding yang dipakai:

- posisi: `theta_deg = count / CPR * 360`
- kecepatan: `rpm = delta_count / CPR * 60 / dt`

> CPR harus dikalibrasi. Putar poros tepat satu putaran, baca perubahan count, lalu masukkan angka itu melalui GUI/serial.

## 2. Mengapa ada RPM raw, moving average dan LPF?
RPM raw paling cepat merespons tetapi kasar pada sampling pendek. Moving average meredam spike, sedangkan LPF eksponensial memberi kompromi noise/lag:

`rpm_lpf[k] = alpha*rpm_ma[k] + (1-alpha)*rpm_lpf[k-1]`

Pada kontrol speed default feedback menggunakan RPM LPF. Mahasiswa dapat membandingkan raw, MA, dan LPF pada grafik.

## 3. Driver L293D dan PWM bertanda
Output PID dibatasi `-MAXPWM ... +MAXPWM`.

- `u > 0`: D5 menerima PWM, D6 = 0.
- `u < 0`: D5 = 0, D6 menerima `abs(u)`.
- stop/fault: D5 = D6 = 0.

Jangan pernah memberi PWM aktif ke dua arah secara bersamaan pada implementasi ini.

## 4. Mode SPEED
Feedback adalah RPM LPF. Setpoint dapat positif atau negatif. Urutan tuning praktikum yang disarankan:

1. Ki=Kd=0, naikkan Kp hingga respons cukup cepat namun stabil.
2. Tambahkan Ki kecil untuk menghilangkan steady-state error.
3. Tambahkan Kd bila perlu untuk meredam perubahan cepat/noise dengan hati-hati.
4. Bandingkan rise time, settling time, overshoot dan SSE.

## 5. Mode POSITION
Feedback adalah posisi derajat. Saat GUI berpindah ke mode Position, firmware dihentikan dahulu lalu GUI mengirim `ZERO,1`, sehingga posisi saat itu menjadi 0°. PID kemudian mengendalikan target sudut.

Mode position harus diuji pertama kali dengan `MAXPWM` kecil agar mekanisme tidak menabrak end-stop.

## 6. PID diskrit dan anti-windup
Implementasi menggunakan derivative-on-measurement agar setpoint step tidak menghasilkan derivative kick besar. Integrator menggunakan conditional integration: integral tidak dilanjutkan jika output jenuh dan penambahan integral mendorong saturasi makin jauh. Ketika gain/mode diganti, state PID di-reset untuk menghindari bump besar.

## 7. Keselamatan software
Firmware P15 menerapkan:

- output PWM OFF saat boot;
- heartbeat host; jika GUI hilang ketika RUN, output dihentikan;
- batas `MAXPWM`;
- deteksi stall sederhana saat command tinggi tetapi encoder tidak bergerak;
- fault latched hingga `CLEAR,1`;
- mode switch tidak langsung mengaktifkan motor;
- command `RUN,0` selalu menghentikan motor.

## 8. GUI Python
GUI mendukung:

- ukuran awal 1900x960;
- refresh/connect/disconnect;
- mode Speed/Position;
- Start/Stop;
- setpoint -600..600;
- Kp/Ki/Kd 0..3 step 0.01;
- alpha LPF 0..1;
- moving-average window 1..16;
- sampling 10..300 ms;
- CPR dan MAXPWM;
- check/uncheck setiap kurva;
- dua grafik: feedback dan komponen kontrol;
- clear data/fault;
- export CSV, XLSX dan JPG;
- hitung delay/rise/peak/settling time, overshoot dan steady-state error;
- `--demo` untuk latihan GUI tanpa hardware.

## 9. Serial protocol
Telemetry:

```text
ms,mode,sp,position_deg,rpm_raw,rpm_ma,rpm_lpf,error,P,I,D,pid_pwm,pwm_cw,pwm_ccw,fault
```

Command utama: `RUN`, `MODE`, `SP`, `KP`, `KI`, `KD`, `ALPHA`, `MA`, `TS`, `CPR`, `MAXPWM`, `ZERO`, `CLEAR`, `PING`, `STATUS`.

## 10. Alur AI yang benar
AI digunakan sebagai pair programmer, bukan pengganti pengujian. Selalu lakukan: prompt -> review pin/protokol/satuan -> build PlatformIO -> tes tanpa motor -> tes PWM rendah -> verifikasi arah encoder -> closed-loop -> simpan bukti. Jangan menerima perubahan AI yang menghapus interlock/fault hanya agar motor “langsung jalan”.

## Program yang wajib dijalankan

1. `examples/mega_motor_pid` — firmware PlatformIO.
2. `examples/gui/app.py --demo` — GUI tanpa hardware.
3. `examples/gui/app.py` — GUI dengan Arduino Mega.
4. `examples/analyze_saved_run.py <csv>` — analisis ulang data tersimpan.

Lihat `Jobsheet.md` untuk prosedur commissioning berurutan.

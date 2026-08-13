# Pertemuan 01 — Dasar Sistem Kontrol dan PID + Briefing Project PCB


## Capaian
Mahasiswa mampu menjelaskan plant, input, output, setpoint, error, sensor, controller, actuator, disturbance, open-loop, closed-loop, feedback, dan komponen P-I-D; membaca respon step; serta memahami project PCB Arduino Mega yang dipakai sepanjang semester.

## 1. Sistem kontrol
Sistem kontrol mengatur keluaran plant agar mengikuti tujuan. Pada **open loop**, aksi kontrol tidak dikoreksi oleh keluaran. Pada **closed loop**, sensor mengukur keluaran `y`, dibandingkan dengan setpoint `r`, menghasilkan error `e=r-y`, lalu controller menghasilkan command `u` ke actuator.

```text
r(setpoint) -> (+) -> e -> Controller -> u -> Actuator/Plant -> y
              ^ -                                  |
              |-------------- Sensor <-------------|
```

Contoh plant praktikum:
- pemanas air: `u` = duty SSR, `y` = temperatur;
- motor speed: `u` = PWM bertanda, `y` = RPM;
- motor position: `u` = PWM bertanda, `y` = count/sudut encoder.

## 2. Respon sistem
Istilah yang akan dipakai sepanjang semester: delay time, rise time, peak time, maximum overshoot, settling time, steady-state error. Jangan menyimpulkan controller "bagus" hanya dari satu parameter; respon cepat dapat menambah overshoot atau command aktuator.

## 3. PID
Bentuk kontinu ideal:

`u(t) = Kp e(t) + Ki ∫e(t)dt + Kd de(t)/dt`

- **P:** aksi sebanding error sekarang; terlalu kecil lambat, terlalu besar dapat berosilasi/saturasi.
- **I:** mengakumulasi error sehingga offset dapat hilang; harus dilindungi dari integral windup saat output saturasi.
- **D:** bereaksi terhadap laju perubahan error; membantu redaman tetapi sensitif noise, sehingga implementasi nyata biasanya difilter.

### PID diskrit sederhana
Pada sampling `Ts`:
- `P = Kp*e[k]`
- `I[k] = I[k-1] + Ki*e[k]*Ts`
- `D = Kd*(e[k]-e[k-1])/Ts`
- `u = sat(P+I+D, umin, umax)`

Anti-windup dasar: jangan menambah integral bila output sudah saturasi dan error mendorong lebih jauh ke arah saturasi.

## 4. Dua plant semester
### Water heater
Plant termal lambat. Model awal dapat dianggap first-order plus dead time: `G(s)=K*exp(-L*s)/(tau*s+1)`. Nilai K, tau, dan L harus diidentifikasi dari data plant nyata, bukan dianggap universal.

### Motor DC
Kecepatan merespons lebih cepat daripada temperatur. Posisi adalah integral dari kecepatan, sehingga kontrol posisi harus memperhatikan overshoot, hard-stop mekanik, dan batas command.

## 5. Briefing project PCB
Buat PCB/shield Arduino Mega 2560 dengan:
- jalur temperatur: A0/sensor interface, D8 SSR logic output, indikator/enable;
- jalur motor: L293D, D5 PWM CW, D6 PWM CCW, encoder A D2, B D3;
- test point, konektor, supply low-voltage, dan interlock;
- dokumentasi schematic, layout, BOM, Gerber, bring-up, dan pengujian.

Spesifikasi rinci: `../HARDWARE_PCB_SPEC.md`.

## 6. Keselamatan
Fokus PCB mahasiswa adalah low-voltage. Bila water heater menggunakan mains, sisi mains wajib terpisah/enclosed dan ditangani personel kompeten. Selama debugging awal gunakan lampu indikator atau heater DC low-voltage sebagai dummy load SSR.

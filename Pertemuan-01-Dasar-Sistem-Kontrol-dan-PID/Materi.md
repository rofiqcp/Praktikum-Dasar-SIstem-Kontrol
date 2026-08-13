# Pertemuan 1 — Dasar Sistem Kontrol, PID, dan Project PCB Trainer

## Capaian
Mahasiswa mampu menjelaskan struktur sistem kontrol, membedakan open-loop dan closed-loop, memahami error/feedback, menjelaskan fungsi P-I-D, membaca grafik respon, dan memahami project hardware semester.

## 1. Sistem kontrol
Sistem kontrol adalah susunan komponen yang membuat keluaran plant mengikuti tujuan tertentu. Istilah utama:

- **Plant**: objek yang dikendalikan, misalnya pemanas air atau motor DC.
- **Setpoint (SP)**: nilai yang diinginkan.
- **Process Variable (PV)**: nilai aktual yang diukur sensor.
- **Error**: `e(t)=SP(t)-PV(t)`.
- **Controller**: menghitung aksi kontrol.
- **Actuator**: mengubah energi/aksi fisik, misalnya SSR/heater atau driver motor.
- **Sensor**: memberi feedback.
- **Disturbance**: gangguan, misalnya air dingin ditambahkan atau beban motor berubah.

## 2. Open-loop vs closed-loop

### Open-loop
Controller tidak mengoreksi berdasarkan output aktual.

Contoh: heater diberi duty 50% selama 5 menit tanpa membaca suhu.

Kelebihan: sederhana. Kekurangan: mudah berubah bila plant/beban berubah.

### Closed-loop
PV dibaca dan dibandingkan dengan SP. Error dipakai untuk koreksi.

```text
SP ---> (+) ---> Controller ---> Actuator ---> Plant ---> PV
        ^  -                                      |
        |_________________________________________|
```

## 3. PID

Bentuk kontinu ideal:

`u(t) = Kp e(t) + Ki ∫e(t)dt + Kd de(t)/dt`

### P — Proportional
Bereaksi terhadap error sekarang.
- Kp kecil: respon lambat.
- Kp besar: respon agresif; dapat overshoot/osilasi.

### I — Integral
Menjumlahkan error terhadap waktu.
- membantu menghilangkan steady-state error;
- berisiko windup saat output saturasi.

### D — Derivative
Bereaksi terhadap laju perubahan.
- dapat menambah damping;
- sensitif noise;
- praktik embedded sering memakai derivative on measurement/filter.

## 4. Saturasi dan anti-windup
Aktuator selalu terbatas:
- heater: 0–100%;
- PWM Mega: 0–255.

Jika integral terus bertambah saat output sudah mentok, terjadi **integral windup**. Contoh program semester ini memakai conditional integration anti-windup.

## 5. Sampling time
PID digital dievaluasi berkala:

`I[k] = I[k-1] + Ki*e[k]*Ts`

`D[k] ≈ -Kd*(PV[k]-PV[k-1])/Ts`

Sampling terlalu lambat mengurangi kualitas kontrol; terlalu cepat meningkatkan noise/overhead. Ts harus dicatat di setiap eksperimen.

## 6. Karakteristik respon
Parameter yang dipakai sepanjang semester:
- delay time;
- rise time;
- peak time;
- settling time;
- maximum overshoot;
- steady-state error.

Definisi komputasional repo ada di `shared/python/response_metrics.py` dan `shared/matlab/response_metrics.m`.

## 7. Dua plant semester

### Pemanas air
Energi listrik → heater → temperatur air. Plant termal umumnya lambat dan dapat dimodelkan pendekatan orde satu:

`G(s)=K/(tau*s+1)`

### Motor DC
Input PWM → driver → motor. Feedback encoder dipakai untuk:
- speed (RPM);
- position (count/degree).

## 8. Project PCB semester
Buat shield/trainer Arduino Mega 2560 yang memiliki:
- L293D;
- motor CW D5;
- motor CCW D6;
- encoder A D2;
- encoder B D3;
- SSR output D8;
- temperature input A0;
- auxiliary ADC A1;
- test point dan terminal yang jelas.

Lihat `../HARDWARE_PCB_SPEC.md`.

## 9. Alur engineering
Project tidak dinilai dari “PCB jadi” saja. Tahapan:
1. requirement/pin map;
2. schematic;
3. ERC/manual review;
4. PCB layout;
5. Gerber/BOM;
6. assembly;
7. continuity test;
8. low-voltage bring-up;
9. I/O test;
10. plant test;
11. closed-loop PID;
12. dokumentasi.

## 10. Program wajib
Jalankan:

```bash
python examples/control_basics.py
```

Program membandingkan open-loop dan closed-loop PID pada plant orde satu sederhana dan menyimpan grafik.

# Pertemuan 1 — Dasar Sistem Kontrol, PID, dan Project PCB Trainer

## Capaian
Mahasiswa mampu menjelaskan open-loop, closed-loop, SP, PV, error, feedback, P-I-D, sampling time, saturasi, windup, karakteristik respon, serta requirement awal trainer semester.

## 1. Alur empat pertemuan awal

```text
P1 konsep kontrol -> P2 MATLAB -> P3 model plant -> P4 PID closed-loop
```

Dua studi kasus utama adalah pemanas air dan motor DC.

## 2. Elemen sistem kontrol

| Elemen | Arti |
|---|---|
| SP | nilai target |
| PV | nilai aktual yang diukur |
| Error | `SP-PV` |
| Controller | menghitung koreksi |
| Plant | objek dinamik |
| Sensor | mengukur output |
| Disturbance | gangguan pada plant |
| Noise | gangguan pengukuran |

## 3. Open-loop dan closed-loop
Open-loop tidak memakai hasil pengukuran untuk mengoreksi aksi. Closed-loop memakai feedback:

```text
SP -> (+) -> Controller -> Plant -> PV
      ^ -                    |
      |------ feedback ------|
```

Closed-loop dapat mengoreksi error, tetapi tanda feedback, gain, dan sensor harus benar.

## 4. PID

```text
u(t)=Kp e(t)+Ki integral(e(t))+Kd de(t)/dt
```

### P
Memberi koreksi berdasarkan error sekarang. Kp terlalu kecil dapat lambat; terlalu besar dapat membuat respon agresif.

### I
Mengakumulasi error dan membantu mengurangi steady-state error. Integral yang terus bertambah ketika output telah mencapai batas menyebabkan windup.

### D
Merespons laju perubahan. D dapat memberi damping, tetapi sensitif terhadap noise. Implementasi digital sering memakai derivative on measurement.

## 5. PID digital

```text
e[k]=SP[k]-PV[k]
P[k]=Kp*e[k]
I[k]=I[k-1]+Ki*e[k]*Ts
D[k]=-Kd*(PV[k]-PV[k-1])/Ts
```

`Ts` adalah sampling time dan harus dicatat pada eksperimen digital.

## 6. Karakteristik respon
Parameter yang dipakai sepanjang semester:
- rise time;
- peak time;
- overshoot;
- settling time;
- steady-state error.

Mahasiswa harus mampu menghubungkan perubahan gain dengan perubahan bentuk respon.

## 7. Plant semester
### Pemanas air
Pendekatan awal:

```text
G(s)=K/(tau*s+1)
```

`K` memengaruhi nilai steady-state dan `tau` memengaruhi kecepatan respon.

### Motor DC
Encoder digunakan untuk mendapatkan count, sudut, dan rpm. Model kecepatan dan posisi dibahas pada P3.

## 8. Kickoff PCB trainer
Pin awal yang dipakai sepanjang semester:

| Fungsi | Pin Mega |
|---|---:|
| Encoder A | D2 |
| Encoder B | D3 |
| Motor channel A | D5 |
| Motor channel B | D6 |
| SSR logic output | D8 |
| Temperature input | A0 |
| Auxiliary ADC | A1 |

Tahapan project:
1. requirement;
2. pin map;
3. diagram blok;
4. schematic;
5. review desain;
6. layout;
7. BOM/Gerber;
8. assembly;
9. continuity dan bring-up logic;
10. I/O test;
11. plant test;
12. closed-loop test;
13. dokumentasi.

Lihat juga `../HARDWARE_PCB_SPEC.md`, `../WIRING.md`, dan `../SAFETY.md`.

## 9. Program wajib

```bash
python examples/control_basics.py
python examples/pid_parameter_sweep.py
```

Grafik tersimpan di `examples/output/`.

Di `control_basics.py`, ubah konstanta `KP`, `KI`, `KD`, `PLANT_K`, dan `TAU` satu per satu. `pid_parameter_sweep.py` membandingkan P rendah, P tinggi, PI, dan PID pada satu grafik.

## 10. Eksperimen minimal
1. Jalankan baseline.
2. Uji P rendah dan P tinggi.
3. Uji PI.
4. Uji PID.
5. Ubah `PLANT_K`.
6. Ubah `TAU`.
7. Tulis prediksi sebelum setiap run.
8. Bandingkan prediksi dengan grafik.

## 11. Target akhir P1
Mahasiswa harus dapat menjelaskan tanpa membaca catatan:

```text
SP -> error -> controller -> plant -> PV -> feedback
```

serta menjelaskan mengapa satu kombinasi gain tidak otomatis cocok untuk semua plant.

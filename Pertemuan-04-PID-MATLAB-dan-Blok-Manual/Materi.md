# Pertemuan 4 — PID MATLAB dan PID Block Buat Sendiri

## Capaian
Mahasiswa mampu membentuk closed-loop, membandingkan P/PI/PID, membaca `stepinfo`, memakai object `pid`, membangun jalur P-I-D secara manual di Simulink, serta membandingkan hasil manual dengan blok PID bawaan.

## 1. Closed-loop
Dari plant P3, controller ditempatkan pada loop feedback negatif:

```text
R(s) -> (+) -> C(s) -> G(s) -> Y(s)
        ^ -                  |
        |____________________|
```

Transfer function closed-loop:

```text
T(s) = C(s)G(s)/(1+C(s)G(s))
```

MATLAB:

```matlab
T = feedback(C*G,1);
```

## 2. Bentuk controller

```text
P   : C(s)=Kp
PI  : C(s)=Kp+Ki/s
PD  : C(s)=Kp+Kd s
PID : C(s)=Kp+Ki/s+Kd s
```

MATLAB:

```matlab
C_P   = pid(Kp,0,0);
C_PI  = pid(Kp,Ki,0);
C_PID = pid(Kp,Ki,Kd);
```

## 3. Pengaruh gain
### Kp
Kp memperkuat error saat ini. Kenaikan Kp biasanya membuat koreksi lebih kuat, tetapi jika terlalu besar respon dapat menjadi agresif.

### Ki
Integral mengakumulasi error. Ia membantu mengurangi error akhir, namun nilai terlalu besar dapat memperbesar overshoot dan memperlama settling.

### Kd
Derivative merespons laju perubahan. Ia dapat menambah damping, tetapi bentuk ideal sensitif terhadap komponen frekuensi tinggi. Pada implementasi praktis derivative sering diberi filter.

## 4. Parameter respon
Gunakan:

```matlab
info = stepinfo(T);
ess = abs(1-dcgain(T));
```

Catat minimal:
- RiseTime;
- SettlingTime;
- Overshoot;
- Peak;
- PeakTime;
- steady-state error.

Jangan memilih gain hanya dari satu angka. Bandingkan keseluruhan respon.

## 5. Plant latihan
Gunakan plant pemanas air P3:

```text
G(s)=35/(120s+1)
```

Gain awal untuk eksplorasi:

```text
P   : Kp=0.20
PI  : Kp=0.20, Ki=0.005
PID : Kp=0.20, Ki=0.005, Kd=0.5
```

Nilai tersebut adalah titik awal simulasi, bukan tuning universal.

## 6. PID built-in
Contoh:

```matlab
s = tf('s');
G = 35/(120*s+1);
C = pid(0.20,0.005,0.5);
T = feedback(C*G,1);
step(T,600); grid on;
stepinfo(T)
```

## 7. PID manual di Simulink
Bentuk manual:

```text
                   -> [Kp] ------------------>
Error -> split ----> [Ki] -> [Integrator] ----> SUM -> output
                   -> [Kd] -> [Derivative] --->
```

Struktur lengkap:

```text
Step -> Sum(error) -> PID manual -> Plant -> Scope
          ^                         |
          |----------- (-) ---------|
```

Tujuan membangun manual block adalah melihat secara langsung asal kontribusi P, I, dan D.

## 8. Derivative dengan filter
Derivative ideal:

```text
Kd s
```

Pendekatan filtered derivative:

```text
Kd N s/(s+N)
```

Bandingkan respon ideal dan filtered pada simulasi bila waktu praktikum cukup.

## 9. PID diskrit sebagai jembatan
Untuk sampling `Ts`:

```text
e[k] = SP[k]-PV[k]
P[k] = Kp e[k]
I[k] = I[k-1] + Ki e[k] Ts
D[k] = -Kd (PV[k]-PV[k-1])/Ts
u[k] = P[k]+I[k]+D[k]
```

Persamaan ini akan muncul kembali pada implementasi digital di pertemuan berikutnya.

## 10. Tuning manual
Lakukan satu perubahan pada satu waktu:

1. mulai P saja;
2. ubah Kp dan catat respon;
3. tambahkan Ki dan catat perubahan error akhir;
4. tambahkan Kd dan amati damping;
5. simpan semua gain dan metrics.

Tabel wajib:

| Kasus | Kp | Ki | Kd | Rise | Settling | Overshoot | ess |
|---|---:|---:|---:|---:|---:|---:|---:|
| P | | 0 | 0 | | | | |
| PI | | | 0 | | | | |
| PID | | | | | | | |

## 11. `pidtune` sebagai pembanding

```matlab
[Cauto,infoTune] = pidtune(G,'PID');
Tauto = feedback(Cauto*G,1);
```

Bandingkan hasil otomatis dengan eksperimen manual. Tujuan penggunaan `pidtune` adalah pembanding, bukan menggantikan analisis.

## 12. Tiga plant
Setelah memahami pemanas air, ulangi konsep pada:
- `Gspeed` dari P3;
- `Gpos` dari P3.

Perhatikan bahwa gain yang cocok untuk satu plant tidak dapat langsung dipindahkan ke plant lain karena dinamika dan satuannya berbeda.

## 13. Program wajib

```matlab
run('examples/pid_comparison.m')
run('examples/pid_gain_sweep.m')
run('examples/build_pid_manual_simulink.m')
```

## 14. Kesalahan umum
- mengubah Kp, Ki, Kd sekaligus tanpa catatan;
- hanya melihat grafik tanpa `stepinfo`;
- salah tanda feedback;
- menganggap gain dari satu plant berlaku untuk semua plant;
- tidak membandingkan PID built-in dan manual;
- memakai hasil tuning otomatis tanpa memahami perubahan respon.

## 15. Hubungan P1–P4

```text
P1 konsep sistem kontrol
   -> P2 komputasi MATLAB
      -> P3 model transfer function
         -> P4 closed-loop PID dan Simulink manual
```

Setelah P4, mahasiswa harus dapat menjelaskan dari mana error berasal, bagaimana P/I/D dihitung, bagaimana plant merespons, dan bagaimana kualitas respon dinilai.

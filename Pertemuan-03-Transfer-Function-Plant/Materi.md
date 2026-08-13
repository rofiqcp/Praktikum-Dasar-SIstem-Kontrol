# Pertemuan 3 — Transfer Function Plant Pemanas Air dan Motor DC

## Capaian pembelajaran
Setelah pertemuan ini mahasiswa mampu:

1. menjelaskan hubungan persamaan diferensial, Laplace, dan transfer function;
2. membentuk transfer function plant pemanas air orde satu;
3. membentuk model motor DC untuk kecepatan dan posisi;
4. menggunakan `tf`, `step`, `impulse`, `pole`, `zero`, `dcgain`, dan `stepinfo`;
5. menjelaskan pengaruh pole, zero, gain, time constant, dan integrator;
6. membandingkan tiga plant secara kuantitatif;
7. melakukan estimasi sederhana `K` dan `tau` dari data step pemanas air;
8. membuat model Simulink secara manual dan melalui script builder.

---

## 1. Hubungan P1–P3
Pada P1 mahasiswa melihat plant sebagai kotak. Pada P2 mahasiswa mensimulasikan orde satu dengan persamaan diferensial diskrit. P3 menyatakan dinamika tersebut dalam domain Laplace.

```text
persamaan fisik -> differential equation -> Laplace -> G(s) -> analisis respon
```

Transfer function bukan pengganti pemahaman fisik. Ia adalah representasi input-output untuk sistem linear time invariant dengan initial condition nol.

---

## 2. Definisi transfer function
Untuk sistem LTI:

```text
G(s) = Y(s) / U(s)
```

`U(s)` adalah transformasi Laplace input dan `Y(s)` adalah transformasi Laplace output.

Contoh:

```text
tau dy/dt + y = K u
```

Laplace dengan initial condition nol:

```text
(tau s + 1)Y(s) = K U(s)
```

sehingga:

```text
G(s) = K/(tau s + 1)
```

---

## 3. Pole, zero, dan gain
Jika:

```text
G(s) = N(s)/D(s)
```

maka:
- **zero** adalah akar `N(s)`;
- **pole** adalah akar `D(s)`;
- lokasi pole sangat menentukan bentuk dan stabilitas respon.

Pada sistem kontinu sederhana, pole di left-half plane mempunyai komponen peluruhan. Pole di origin menunjukkan integrator. Pole right-half plane menunjukkan dinamika tidak stabil.

Perintah MATLAB:

```matlab
pole(G)
zero(G)
dcgain(G)
```

---

## 4. Plant 1 — Pemanas air
Untuk pembelajaran awal, temperatur dinyatakan sebagai kenaikan terhadap temperatur awal/ambient:

```text
DeltaT = T - Tambient
```

Model orde satu:

```text
G_T(s) = DeltaT(s)/U(s) = K_T/(tau_T s + 1)
```

Contoh parameter simulasi:

```text
K_T = 35 degC/p.u.
tau_T = 120 s
```

Jika input normalized `u=1`, kenaikan temperatur steady-state model adalah sekitar 35 °C di atas baseline.

### Makna parameter
- `K_T` menentukan perubahan steady-state akibat input;
- `tau_T` menentukan seberapa cepat plant mendekati steady state.

Untuk orde satu ideal, pada `t=tau` output telah mencapai sekitar 63.2% perubahan total.

### Catatan model nyata
Plant pemanas air nyata dapat mempunyai:
- dead time;
- kehilangan panas yang berubah;
- volume air berbeda;
- daya heater berbeda;
- mixing tidak sempurna;
- posisi sensor;
- noise pengukuran.

Karena itu model orde satu adalah model kerja awal, bukan klaim bahwa plant fisik selalu persis orde satu.

---

## 5. Identifikasi sederhana pemanas air dari step test
Misalkan input berubah dari `u0` ke `u1` dan output dari `y0` menuju `y_inf`.

Static gain:

```text
K = (y_inf - y0)/(u1-u0)
```

Untuk model orde satu tanpa dead time, cari titik:

```text
y_tau = y0 + 0.632 (y_inf-y0)
```

Waktu sejak step hingga output mencapai `y_tau` menjadi estimasi `tau`.

Metode ini sederhana dan berguna untuk memahami parameter, tetapi data eksperimen harus cukup lama hingga mendekati steady state.

---

## 6. Plant 2 — Motor DC: kecepatan
Model elektrik armature:

```text
V = L di/dt + R i + Ke omega
```

Model mekanik:

```text
J domega/dt + b omega = Kt i
```

Dengan menghilangkan `I(s)`, transfer function kecepatan terhadap tegangan adalah:

```text
Omega(s)/V(s) = Kt / ((L s + R)(J s + b) + Ke Kt)
```

Contoh parameter simulasi pembelajaran:

```text
J  = 0.01 kg.m^2
b  = 0.1 N.m.s
Kt = 0.01 N.m/A
Ke = 0.01 V.s/rad
R  = 1 ohm
L  = 0.5 H
```

Sehingga denominator diperoleh dari parameter listrik dan mekanik, bukan dipilih secara acak.

### Interpretasi
Motor mempunyai dinamika listrik dan mekanik. Karena itu model kecepatan dapat berorde dua. Pada beberapa motor, dinamika listrik jauh lebih cepat sehingga model dapat disederhanakan, tetapi P3 mempertahankan model lengkap agar asal persamaan terlihat.

---

## 7. Plant 3 — Motor DC: posisi
Hubungan posisi dan kecepatan:

```text
omega(t) = dtheta(t)/dt
```

Dalam Laplace:

```text
Omega(s) = s Theta(s)
```

maka:

```text
Theta(s)/V(s) = [Omega(s)/V(s)] / s
```

Artinya model posisi mempunyai satu integrator tambahan dibanding model kecepatan.

Konsekuensi penting:
- step tegangan pada model posisi dapat membuat sudut terus bertambah;
- posisi biasanya membutuhkan closed-loop agar berhenti pada target;
- konsep ini menjadi dasar P4 dan praktikum posisi selanjutnya.

---

## 8. MATLAB Control System Toolbox
Cara membuat transfer function:

```matlab
s = tf('s');
G = 35/(120*s + 1);
```

atau:

```matlab
num = 35;
den = [120 1];
G = tf(num,den);
```

Perintah analisis:

```matlab
step(G)
impulse(G)
pole(G)
zero(G)
dcgain(G)
stepinfo(G)
```

`stepinfo` membantu menghitung rise time, settling time, overshoot, dan parameter lain menurut definisi MATLAB.

---

## 9. Membaca step response
Sebelum melihat plot, biasakan memprediksi:

1. berapa nilai awal?
2. berapa nilai steady-state?
3. apakah output monoton atau berosilasi?
4. apakah terdapat integrator?
5. apakah respon akan settle?
6. parameter apa yang menentukan cepat/lambat?

Setelah itu baru gunakan `step` dan `stepinfo` untuk memverifikasi prediksi.

---

## 10. Perbandingan tiga plant

| Plant | Input | Output | Orde dasar | Karakter penting |
|---|---|---|---|---|
| Pemanas air | daya normalized | Delta temperatur | 1 | lambat, thermal |
| Motor speed | tegangan/perintah | rad/s | 2 | elektrik + mekanik |
| Motor position | tegangan/perintah | rad | 3 | speed model + integrator |

Jangan membandingkan amplitudo grafik tanpa memperhatikan satuan. Fokus pada struktur dinamika dan karakter respon.

---

## 11. Pengaruh parameter
### Pemanas
Ubah `K_T`: nilai akhir berubah.

Ubah `tau_T`: kecepatan respon berubah.

### Motor
- `J` lebih besar → akselerasi mekanik cenderung lebih lambat;
- `b` memengaruhi redaman mekanik;
- `R` dan `L` mengubah dinamika arus;
- `Kt` dan `Ke` menghubungkan domain elektrik dan mekanik.

P3 meminta mahasiswa mengubah parameter satu per satu agar hubungan fisik-model terlihat.

---

## 12. Simulink
Model dasar plant dapat dibuat dengan blok:

```text
Step -> Transfer Fcn -> Scope
```

Untuk membandingkan tiga plant:

```text
             -> G_heater  -> Scope
Step/inputs  -> G_speed   -> Scope
             -> G_pos     -> Scope
```

Repository menyediakan builder:

```matlab
run('examples/build_three_plants_simulink.m')
```

Builder menghasilkan file `.slx` di folder `models`. Mahasiswa tetap wajib memahami isi blok dan tidak hanya menjalankan builder.

---

## 13. Program wajib

```matlab
run('examples/plant_transfer_functions.m')
run('examples/compare_plants.m')
run('examples/parameter_sweep.m')
run('examples/identify_water_heater_from_step.m')
run('examples/build_three_plants_simulink.m')
```

Urutan belajar:
1. definisikan plant;
2. cek pole/zero/dcgain;
3. lihat step response;
4. bandingkan plant;
5. ubah parameter;
6. identifikasi pemanas dari data;
7. bangun Simulink.

---

## 14. Kesalahan umum
1. Menukar numerator dan denominator.
2. Menghilangkan satuan parameter.
3. Menganggap model posisi sama dengan speed.
4. Lupa integrator `1/s` pada posisi.
5. Menganggap `stepinfo` selalu bermakna untuk sinyal yang tidak settle.
6. Menganggap model simulasi identik dengan hardware.
7. Menyetel parameter agar grafik “bagus” tanpa dasar fisik.

---

## 15. Jembatan ke P4
Di P3 plant masih dianalisis terutama secara open-loop. Pada P4 plant ditempatkan dalam loop:

```text
SP -> PID -> G(s) -> PV
 ^                |
 |------ (-) -----|
```

Maka P4 akan menjawab pertanyaan: bagaimana `Kp`, `Ki`, dan `Kd` mengubah pole closed-loop dan karakter respon dari plant yang sudah dibuat di P3?

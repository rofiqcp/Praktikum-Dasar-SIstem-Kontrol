# Pertemuan 03 — MATLAB Transfer Function: Pemanas Air, Motor DC Kecepatan dan Posisi

## Capaian Pembelajaran
- membentuk transfer function
- menganalisis step response dan pole
- membedakan plant speed dan position
- membandingkan MATLAB dan Python/Colab

## Materi Inti

### Transfer function
Untuk sistem LTI, transfer function adalah `G(s)=Y(s)/U(s)` dengan kondisi awal nol.

### Plant pemanas air — model orde satu/FOPDT sederhana
\[
G_T(s)=\frac{K_T}{\tau_T s+1}
\]
Model awal praktikum menggunakan `K_T=0.8 °C/%heater` dan `tau=45 s`. Parameter dapat diganti dari hasil eksperimen P5–P6.

### Motor DC — kecepatan
Model elektromekanik standar:
\[
G_\omega(s)=\frac{K}{(Js+b)(Ls+R)+K^2}
\]

### Motor DC — posisi
Posisi adalah integral kecepatan:
\[
G_\theta(s)=\frac{G_\omega(s)}{s}
\]

Analisis awal menggunakan `step`, `impulse`, `pole`, `zero`, `dcgain` dan `stepinfo`.


## Program yang Wajib Dijalankan
- `examples/plant_transfer_functions.m`
- `examples/colab/plant_transfer_function.ipynb`

## Alur Praktikum
1. Jalankan `examples/plant_transfer_functions.m`.
2. Amati tiga plot: pemanas air, motor speed, motor position.
3. Ubah parameter termal K dan tau.
4. Ubah J, b, R, L, Kt motor dan amati pole/respon.
5. Jalankan notebook Colab `examples/colab/plant_transfer_function.ipynb` sebagai pembanding Python.
6. Jelaskan mengapa transfer posisi mempunyai integrator tambahan.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

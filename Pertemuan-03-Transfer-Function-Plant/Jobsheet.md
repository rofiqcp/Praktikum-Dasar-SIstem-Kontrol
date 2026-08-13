# Jobsheet Pertemuan 3 — Transfer Function Tiga Plant

## Tujuan
Mahasiswa mampu membuat, menganalisis, membandingkan, dan memodifikasi model transfer function pemanas air, motor DC kecepatan, dan motor DC posisi.

## Persiapan
1. Buka MATLAB dari root repository.
2. Masuk ke folder P3.
3. Pastikan Control System Toolbox tersedia.
4. Baca `Materi.md` dan tuliskan prediksi respon tiga plant sebelum menjalankan program.

## Percobaan 1 — Pemanas air orde satu
Gunakan model:

```text
G_T(s) = K_T/(tau_T s + 1)
```

Dengan baseline `K_T=35` dan `tau_T=120 s`.

Di MATLAB buat model menggunakan `tf`, lalu tampilkan:
- transfer function;
- pole;
- zero;
- DC gain;
- step response;
- `stepinfo`.

Isi tabel:

| K_T | tau_T | Pole | DC gain | Rise time | Settling time | Nilai akhir |
|---:|---:|---|---:|---:|---:|---:|
| 35 | 120 | | | | | |

Jelaskan mengapa temperatur pada model dinyatakan sebagai kenaikan terhadap baseline.

## Percobaan 2 — Pengaruh K dan tau pemanas
Uji minimal:

| Kasus | K_T | tau_T |
|---|---:|---:|
| A | 20 | 120 |
| B | 35 | 120 |
| C | 50 | 120 |
| D | 35 | 60 |
| E | 35 | 240 |

Gunakan satu figure untuk membandingkan hasil. Jelaskan parameter yang dominan terhadap nilai akhir dan parameter yang dominan terhadap kecepatan respon.

## Percobaan 3 — Motor DC speed
Gunakan parameter baseline pada `Materi.md`:

```text
J=0.01, b=0.1, Kt=0.01, Ke=0.01, R=1, L=0.5
```

Bentuk:

```text
Omega(s)/V(s) = Kt / ((Ls+R)(Js+b)+KeKt)
```

Jalankan `pole`, `zero`, `dcgain`, `step`, dan `stepinfo`.

Catat denominator hasil ekspansi dan cocokkan dengan hasil MATLAB.

## Percobaan 4 — Motor DC position
Buat:

```text
G_pos(s) = G_speed(s)/s
```

Bandingkan step response speed dan position.

Jawab:
1. Mengapa position mempunyai pole tambahan di origin?
2. Mengapa step position open-loop tidak harus settle?
3. Mengapa posisi memerlukan closed-loop pada praktikum berikutnya?

## Percobaan 5 — Program tiga plant
Jalankan:

```matlab
run('examples/plant_transfer_functions.m')
run('examples/compare_plants.m')
```

Simpan screenshot transfer function, pole/zero, dan grafik perbandingan.

## Percobaan 6 — Parameter sweep
Jalankan:

```matlab
run('examples/parameter_sweep.m')
```

Lakukan analisis minimal:
- tiga `tau` pemanas;
- tiga nilai inertia `J` motor.

Tulis kesimpulan berdasarkan bentuk grafik, bukan hanya nilai parameter.

## Percobaan 7 — Identifikasi pemanas dari step data
Jalankan:

```matlab
run('examples/identify_water_heater_from_step.m')
```

Script membaca data contoh dan mengestimasi:
- nilai awal;
- nilai steady-state;
- perubahan input;
- gain `K`;
- target 63.2%;
- time constant `tau`.

Bandingkan model estimasi dengan data pada satu plot.

Pertanyaan:
1. Apa syarat agar metode 63.2% masuk akal?
2. Apa akibat jika data berhenti sebelum steady-state?
3. Apa akibat noise pada estimasi `tau`?

## Percobaan 8 — Simulink
Jalankan:

```matlab
run('examples/build_three_plants_simulink.m')
```

Buka file hasil di `models`. Identifikasi:
- source/Step;
- tiga Transfer Fcn;
- Scope;
- parameter numerator/denominator.

Ubah satu parameter melalui Simulink GUI, run ulang, dan bandingkan dengan script MATLAB.

## Challenge
Pilih satu:
1. tambahkan dead time sederhana pada model pemanas;
2. bandingkan model motor lengkap dengan model pendekatan orde satu;
3. buat script yang mencetak tabel semua pole, DC gain, dan stepinfo;
4. buat data heater sintetis baru dengan `K` dan `tau` berbeda lalu identifikasi kembali.

## Hasil yang dikumpulkan
- laporan P3;
- grafik pemanas parameter sweep;
- grafik speed vs position;
- tabel pole/zero/dcgain;
- hasil identifikasi heater;
- screenshot Simulink;
- file challenge bila dikerjakan.

## Pertanyaan analisis akhir
1. Apa hubungan differential equation dan transfer function?
2. Apa makna pole pada sistem kontinu?
3. Apa makna DC gain?
4. Mengapa `tau` tidak sama dengan settling time?
5. Mengapa model speed motor dapat berorde dua?
6. Dari mana integrator model posisi berasal?
7. Mengapa unit input/output harus dicatat?
8. Mengapa model hasil identifikasi tidak pernah dianggap sempurna?
9. Apa beda mengubah `K_T` dengan `tau_T`?
10. Apa yang akan berubah ketika PID ditambahkan di P4?

## Checklist
- [ ] tiga plant berhasil dibuat;
- [ ] pole/zero/dcgain dicatat;
- [ ] stepinfo dianalisis;
- [ ] parameter sweep dilakukan;
- [ ] heater identification dijalankan;
- [ ] builder Simulink berhasil membuat `.slx`;
- [ ] hasil script dan Simulink konsisten;
- [ ] setiap grafik memiliki satuan dan legend.

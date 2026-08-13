# Pertemuan 02 — Jobsheet — MATLAB dari Nol


## Percobaan
1. Jalankan `examples/matlab_basics.m` per bagian.
2. Buat vector waktu 0–10 s dengan Ts 0.01 s.
3. Buat sinyal sinus 1 Hz dan noise kecil.
4. Plot raw dan moving-average sederhana.
5. Buat matriks 2×2, hitung determinant dan inverse.
6. Panggil function `saturate.m` untuk membatasi data ke -1…1.
7. Buat table `time,signal`, simpan ke CSV, lalu baca ulang dengan `readtable`.

## Latihan kontrol
Simulasikan respon diskrit first-order: `y(k)=y(k-1)+Ts/tau*(-y(k-1)+K*u(k))`. Gunakan input step dan plot hasil.

## Output
- file `.m`;
- satu CSV;
- minimal dua grafik;
- jawaban beda `*` dan `.*`, `^` dan `.^`.

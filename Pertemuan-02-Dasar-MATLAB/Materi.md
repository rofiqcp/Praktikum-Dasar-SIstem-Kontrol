# Pertemuan 2 — Dasar MATLAB

## Tujuan
Mahasiswa dapat memakai Command Window, Workspace, script, function, array/matrix, indexing, plotting, loop, conditional, dan file I/O sebagai fondasi seluruh praktikum kontrol.

## 1. Workspace dan script
MATLAB membedakan command interaktif dan script `.m`. Untuk praktikum, gunakan script agar eksperimen reproducible.

```matlab
clear; clc; close all;
x = 0:0.1:10;
y = sin(x);
plot(x,y); grid on;
```

## 2. Vectorization
MATLAB kuat pada operasi vektor.

```matlab
x = linspace(0,2*pi,1000);
y = sin(x).^2;
```

Operator `.*`, `./`, `.^` adalah operasi element-wise.

## 3. Matrix
```matlab
A = [1 2; 3 4];
b = [5; 6];
x = A\b;
```

Untuk persamaan linear, `A\b` lebih baik daripada `inv(A)*b`.

## 4. Indexing
MATLAB mulai dari indeks 1.

```matlab
v = 10:10:100;
v(1)
v(end)
v(3:6)
```

## 5. Plot
Gunakan label/unit.

```matlab
plot(t,y,'LineWidth',1.4);
xlabel('Time (s)');
ylabel('Temperature (degC)');
grid on;
```

## 6. Function
`examples/saturate.m` menunjukkan fungsi reusable.

## 7. Table/file
Data eksperimen P5/P6 nantinya memakai `readtable`, `writetable`.

## Program wajib
Jalankan `examples/matlab_basics.m` dari Editor dan pahami setiap section `%%`.

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **MATLAB dasar**. Program yang harus dibuka dan dipahami:
- `examples/matlab_basics.m`
- `examples/saturate.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Workspace berisi variabel latihan; figure muncul; CSV dapat ditulis/dibaca kembali.

## Validasi dan troubleshooting
Bedakan `*` dengan `.*`, `^` dengan `.^`, dan perhatikan indexing MATLAB dimulai dari 1.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

# Pertemuan 2 — Dasar MATLAB untuk Praktikum Sistem Kontrol

## Capaian pembelajaran
Setelah pertemuan ini mahasiswa mampu menggunakan MATLAB sebagai alat komputasi teknik: membuat variabel, vektor, matriks, script, function, grafik, tabel data, perulangan, percabangan, impor/ekspor data, serta menyiapkan dasar untuk Control System Toolbox dan Simulink pada P3–P4.

---

## 1. Mengapa MATLAB dipakai?
MATLAB sangat cocok untuk sistem kontrol karena operasi matriks, visualisasi, analisis data, model dinamik, Control System Toolbox, dan Simulink berada dalam satu ekosistem. Pada praktikum ini MATLAB bukan hanya kalkulator: hasil eksperimen hardware selanjutnya juga akan dibaca, diplot, dibandingkan, dan dianalisis di MATLAB.

Alur P2:

```text
scalar -> vector -> matrix -> indexing -> operator -> plot
       -> script -> function -> loop/if -> table/CSV
       -> dasar sinyal -> persiapan transfer function P3
```

---

## 2. Command Window, Workspace, Current Folder, Editor
Empat bagian yang harus dipahami:

- **Command Window**: menjalankan perintah langsung;
- **Workspace**: melihat variabel aktif;
- **Current Folder**: folder kerja MATLAB;
- **Editor**: membuat file `.m`.

Perintah dasar:

```matlab
clc          % membersihkan Command Window
clear        % menghapus variabel
close all    % menutup figure
pwd          % folder aktif
who          % nama variabel
whos         % detail variabel
```

Biasakan script praktikum dimulai dengan:

```matlab
clear; clc; close all;
```

---

## 3. Variabel dan tipe data

```matlab
Kp = 2.5;
setpoint = 60;
nama = "Plant Pemanas Air";
aktif = true;
```

MATLAB bersifat case-sensitive: `Kp` berbeda dengan `kp`.

Cek tipe:

```matlab
class(Kp)
class(nama)
```

Tipe yang sering ditemui:
- `double`;
- `logical`;
- `string`/`char`;
- `table`.

---

## 4. Vektor

```matlab
t = 0:0.1:10;
x = linspace(0, 1, 11);
sp = 60 * ones(size(t));
```

Operator colon sangat penting:

```matlab
awal:step:akhir
```

Contoh sampling 100 ms selama 20 detik:

```matlab
Ts = 0.1;
t = 0:Ts:20;
```

---

## 5. Matriks

```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];
```

Operasi matriks:

```matlab
A + B
A * B
A'
inv(A)
det(A)
eig(A)
```

Untuk komputasi numerik, menyelesaikan `Ax=b` lebih baik memakai:

```matlab
x = A\b;
```

daripada menghitung `inv(A)*b` secara eksplisit.

---

## 6. Operator matriks vs element-wise
Ini salah satu kesalahan paling sering pada mahasiswa.

```matlab
A * B     % perkalian matriks
A .* B    % perkalian elemen
A ^ 2     % pangkat matriks
A .^ 2    % setiap elemen dipangkatkan
A / B     % pembagian matriks
A ./ B    % pembagian elemen
```

Jika membuat fungsi terhadap vektor waktu, sering diperlukan operator titik:

```matlab
y = 2 .* exp(-t ./ 4);
```

---

## 7. Indexing
MATLAB mulai dari indeks 1.

```matlab
x = [10 20 30 40 50];
x(1)
x(end)
x(2:4)
```

Matriks:

```matlab
A(2,1)
A(:,1)      % seluruh baris, kolom 1
A(1,:)      % baris 1, seluruh kolom
```

Logical indexing:

```matlab
nilai = [20 55 70 45 90];
lebih60 = nilai(nilai > 60);
```

Konsep ini akan banyak dipakai saat memilih data eksperimen.

---

## 8. Fungsi matematika penting

```matlab
sin(x)
cos(x)
exp(x)
log(x)
sqrt(x)
abs(x)
min(x)
max(x)
mean(x)
std(x)
sum(x)
```

Konversi derajat-radian:

```matlab
rad2deg(pi)
deg2rad(180)
```

---

## 9. Plotting
Contoh dasar:

```matlab
t = 0:0.1:10;
y = 1 - exp(-t/2);
plot(t,y,'LineWidth',1.5);
grid on;
xlabel('Time (s)');
ylabel('Output');
title('First Order Response');
```

Dua kurva:

```matlab
hold on;
plot(t,ones(size(t)),'--');
legend('PV','SP','Location','best');
```

Dua panel:

```matlab
tiledlayout(2,1);
nexttile; plot(t,y); grid on;
nexttile; plot(t,ones(size(t))-y); grid on;
```

Simpan gambar:

```matlab
exportgraphics(gcf,'hasil_plot.png','Resolution',150);
```

---

## 10. Script dan function
### Script
Script menjalankan rangkaian perintah dalam workspace.

```matlab
% contoh_script.m
clear; clc;
K = 2;
x = 0:0.1:5;
y = K*x;
plot(x,y);
```

### Function
Function mempunyai input/output yang jelas.

```matlab
function y = saturate(x, low, high)
    y = min(max(x, low), high);
end
```

Contoh:

```matlab
u = saturate(310,0,255)
```

Function akan dipakai berulang pada kontrol digital.

---

## 11. Percabangan

```matlab
error = 8;
if abs(error) < 1
    status = "dekat setpoint";
elseif abs(error) < 5
    status = "transisi";
else
    status = "error besar";
end
```

---

## 12. Perulangan

```matlab
y = zeros(1,100);
for k = 2:length(y)
    y(k) = 0.95*y(k-1) + 0.05;
end
```

Preallocation dengan `zeros` penting agar program lebih efisien.

Loop ini adalah jembatan menuju simulasi persamaan diferensial diskrit dan PID from scratch.

---

## 13. Data table dan CSV
Membuat table:

```matlab
t = (0:1:5)';
pv = [25 28 32 37 42 47]';
T = table(t,pv,'VariableNames',{'time_s','temp_C'});
writetable(T,'hasil.csv');
```

Membaca kembali:

```matlab
D = readtable('hasil.csv');
plot(D.time_s,D.temp_C);
```

Ini akan dipakai pada praktikum Autonics/DAQMaster dan GUI.

---

## 14. NaN, Inf, dan validasi data
Data eksperimen tidak selalu ideal.

```matlab
x = [1 2 NaN 4];
isnan(x)
mean(x,'omitnan')
```

Cek nilai valid sebelum analisis. Jangan mengganti data rusak dengan angka sembarang tanpa catatan.

---

## 15. Dasar sinyal untuk sistem kontrol
Buat setpoint step manual:

```matlab
t = 0:0.1:20;
sp = zeros(size(t));
sp(t >= 5) = 60;
```

Sinyal ramp:

```matlab
ramp = 2*t;
```

Sinyal sinus:

```matlab
s = sin(2*pi*0.5*t);
```

Dengan ini mahasiswa belajar bahwa input sistem tidak selalu konstanta.

---

## 16. Model orde satu tanpa toolbox
Sebelum memakai `tf` di P3, respon orde satu dapat dihitung dengan loop Euler:

```matlab
Ts = 0.05;
t = 0:Ts:20;
K = 1.2;
tau = 3;
u = ones(size(t));
y = zeros(size(t));

for k = 2:length(t)
    dydt = (-y(k-1) + K*u(k-1))/tau;
    y(k) = y(k-1) + Ts*dydt;
end
```

Ini penting karena mahasiswa dapat melihat bahwa transfer function di P3 berasal dari dinamika sistem, bukan sekadar fungsi MATLAB.

---

## 17. Control System Toolbox preview
Jika toolbox tersedia:

```matlab
s = tf('s');
G = 1/(3*s + 1);
step(G);
grid on;
```

Pada P2 cukup mengenali syntax. Pembahasan pole, zero, transfer function, dan tiga plant dilakukan di P3.

---

## 18. Praktik penulisan program yang baik
- gunakan nama variabel bermakna;
- tulis satuan pada komentar atau nama kolom;
- hindari angka penting tersebar tanpa penjelasan;
- preallocate array pada loop;
- simpan output ke file;
- beri label dan unit pada plot;
- jangan menghapus data mentah ketika membuat data hasil olahan;
- pisahkan function yang dapat dipakai ulang.

---

## 19. Program wajib
Jalankan dari folder P2:

```matlab
run('examples/matlab_basics.m')
run('examples/vector_matrix_lab.m')
run('examples/plotting_and_data.m')
run('examples/first_order_euler.m')
```

Function:

```matlab
addpath('examples')
saturate(310,0,255)
```

Hasil dari P2 harus membuat mahasiswa siap membaca script P3 tanpa kebingungan mengenai vektor, indexing, function, plot, atau table.

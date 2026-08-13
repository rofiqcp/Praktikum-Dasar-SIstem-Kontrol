# Pertemuan 02 — Dasar-Dasar MATLAB


## Capaian
Mahasiswa dapat memakai Command Window, Workspace, Editor, script `.m`, function, vector/matrix, indexing, operator element-wise, plotting, loop, conditional, dan membaca/menyimpan data.

## Pokok materi
- variabel tanpa deklarasi tipe eksplisit: `a=10;`;
- vector: `t=0:0.01:5;`;
- matriks: `A=[1 2;3 4];`;
- matrix multiplication `A*B` vs element-wise `A.*B`;
- function: `function y=saturate(x,lo,hi)`;
- plot: `plot(t,y)`, `grid on`, `legend`;
- table/timetable untuk data eksperimen;
- `readtable`, `writetable`;
- script parameter plant/controller.

## Kebiasaan kerja yang benar
1. Gunakan nama variabel bermakna (`setpoint`, `temperature`, `rpm`).
2. Tulis satuan di komentar/label grafik.
3. Jangan menimpa fungsi MATLAB dengan nama file seperti `step.m`, `plot.m`, `filter.m`.
4. Gunakan `clear; clc; close all;` secukupnya saat praktikum.
5. Simpan data mentah sebelum memproses.

## Hubungan dengan kontrol
MATLAB dipakai untuk membuat model transfer function, mensimulasikan step response, menghitung PID, membaca data DAQMaster, dan berkomunikasi dengan Arduino pada pertemuan berikutnya.

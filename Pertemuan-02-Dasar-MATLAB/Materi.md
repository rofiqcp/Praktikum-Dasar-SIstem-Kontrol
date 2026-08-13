# Pertemuan 02 — Dasar-Dasar MATLAB dan Simulink

## Capaian Pembelajaran
- menggunakan script/function MATLAB
- melakukan operasi vector dan matrix
- membuat plot
- mengenal block dasar Simulink

## Materi Inti

Fokus pertemuan ini adalah dasar MATLAB sebelum masuk ke model plant. Topik: Command Window, Workspace, script `.m`, function, scalar/vector/matrix, indexing, operator elemen `.* ./ .^`, plotting, `linspace`, `zeros`, loop dan conditional, serta dasar penggunaan Control System Toolbox.

Mahasiswa juga mengenal Simulink sebagai lingkungan block diagram: Sources, Sinks, Math Operations, Mux/Demux/Bus, Switch, Logic, Subsystem, MATLAB Function dan penggunaan m-file untuk inisialisasi parameter.


## Program yang Wajib Dijalankan
- `examples/matlab_basics.m`
- `examples/saturate.m`

## Alur Praktikum
1. Buka MATLAB dan buat folder kerja.
2. Jalankan `examples/matlab_basics.m`.
3. Ubah frekuensi sinus dan matriks A/B.
4. Buat function sederhana `saturate.m`.
5. Buka Simulink dan susun Step → Gain → Scope.
6. Simpan screenshot plot dan model.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

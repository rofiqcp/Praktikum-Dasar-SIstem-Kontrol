# Jobsheet Pertemuan 2 — Dasar MATLAB

## Tujuan
Mahasiswa mampu menggunakan workspace MATLAB, scalar, vector, matrix, indexing, plotting, script, function, loop, percabangan, table, CSV, serta simulasi numerik sederhana.

## Persiapan
1. Buka MATLAB dan arahkan Current Folder ke `Pertemuan-02-Dasar-MATLAB`.
2. Jalankan `version` dan `ver`, lalu catat versi serta toolbox yang tersedia.
3. Baca `Materi.md` sebelum memulai.

## Percobaan 1 — Workspace dan variabel
Buat `Kp=2.5`, `Ki=0.4`, `Kd=0.1`, `SP=60`, dan `PV=52.5`. Hitung `error=SP-PV`, lalu gunakan `who` dan `whos`.

Catat nilai, class, dan ukuran variabel. Jelaskan perbedaan nilai dengan tipe data.

## Percobaan 2 — Vector dan indexing
Buat vektor waktu `0:0.1:10` dan respon `1-exp(-t/2)`. Tampilkan elemen pertama, terakhir, elemen 2–10, kemudian cari waktu pertama saat nilai mencapai 90% menggunakan logical indexing dan `find`.

## Percobaan 3 — Matrix
Gunakan:

```matlab
A=[1 2;3 4]; B=[5 6;7 8];
```

Bandingkan `A*B` dengan `A.*B`. Hitung transpose, determinant, eigenvalue, kemudian selesaikan sistem `A*x=b` menggunakan operator backslash. Verifikasi hasil dengan mengalikan kembali `A*x`.

## Percobaan 4 — Program dasar
Jalankan:

```matlab
run('examples/matlab_basics.m')
run('examples/vector_matrix_lab.m')
```

Identifikasi bagian scalar, vector, matrix, indexing, percabangan, loop, serta plotting. Ubah satu parameter dan jelaskan pengaruhnya.

## Percobaan 5 — Plot dan data
Jalankan:

```matlab
run('examples/plotting_and_data.m')
```

Pastikan script menghasilkan figure dan `output/p02_sample_data.csv`. Baca kembali CSV dengan `readtable`, kemudian plot salah satu kolom hasil.

## Percobaan 6 — Function
Tambahkan `examples` ke path, lalu uji function `saturate` untuk input di dalam batas, di atas batas, dan di bawah batas. Buat tabel input dan hasil.

## Percobaan 7 — Simulasi numerik orde satu
Jalankan:

```matlab
run('examples/first_order_euler.m')
```

Uji kombinasi berikut:

| Kasus | K | tau | Nilai akhir | Catatan kecepatan respon |
|---|---:|---:|---:|---|
| A | 1 | 2 | | |
| B | 1 | 5 | | |
| C | 2 | 5 | | |

Jelaskan pengaruh `K` terhadap nilai akhir dan `tau` terhadap kecepatan respon. Hubungkan hasil ini dengan materi transfer function pada P3.

## Percobaan 8 — Setpoint bertingkat
Buat vektor setpoint:
- 0–5 s = 25;
- 5–12 s = 50;
- setelah 12 s = 65.

Gunakan logical indexing, plot hasilnya, beri label sumbu dan grid, kemudian simpan gambar.

## Challenge
Pilih satu:
1. analisis 20 sampel temperatur: mean, minimum, maksimum, standard deviation, dan table;
2. bandingkan dua respon orde satu dengan `tau` berbeda pada satu figure;
3. buat function `control_error(sp,pv)` yang dapat menerima scalar maupun vector.

## Hasil yang dikumpulkan
- laporan singkat;
- screenshot workspace;
- hasil vector/matrix;
- minimal tiga figure;
- CSV hasil script;
- source challenge;
- tabel hasil Percobaan 7.

## Pertanyaan analisis
1. Apa beda `*` dan `.*`?
2. Mengapa preallocation array penting?
3. Apa beda script dan function?
4. Mengapa operator `A\b` umum dipakai untuk sistem linear?
5. Bagaimana logical indexing membantu analisis data?
6. Apa hubungan sampling time dengan jumlah sampel?
7. Mengapa CSV penting untuk praktikum berikutnya?
8. Apa makna `K` dan `tau` pada simulasi orde satu?

## Checklist
- [ ] seluruh script wajib berjalan;
- [ ] function `saturate` diuji;
- [ ] CSV berhasil dibaca kembali;
- [ ] semua grafik memiliki title, label, dan grid;
- [ ] challenge selesai;
- [ ] hasil tidak hanya berupa screenshot tetapi disertai interpretasi.

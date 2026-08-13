# Pertemuan 5 — Autonics Temperature Controller: Pengamatan Manual dan Analisis Respon

## Capaian pembelajaran
Mahasiswa mampu membaca PV dan SV, menjelaskan ON/OFF, hysteresis, dan PID secara konseptual, membuat eksperimen yang dapat direproduksi, merekam data dengan stopwatch, serta menganalisis respon temperatur menggunakan Excel, Python, dan MATLAB.

## Alur pembelajaran
P1–P4 menggunakan model dan simulasi. P5 mulai menggunakan data dari trainer temperatur laboratorium. Fokus utama P5 adalah kualitas eksperimen dan kualitas data.

## Istilah penting
- **PV**: nilai proses yang terukur.
- **SV**: nilai target.
- **Error**: selisih SV dan PV.
- **Hysteresis**: jarak ambang pada kontrol ON/OFF.
- **PID**: kombinasi aksi proportional, integral, dan derivative.

## ON/OFF dan hysteresis
Mode ON/OFF menghasilkan respon yang berosilasi di sekitar target. Hysteresis mencegah perubahan keadaan yang terlalu sering akibat variasi kecil pada PV. Mahasiswa membandingkan beberapa nilai hysteresis dan menjelaskan trade-off antara lebar ripple dan frekuensi perubahan output.

## PID
Secara konsep:

`u(t)=Kp e(t)+Ki integral(e)dt+Kd de(t)/dt`

P merespons error saat ini, I mengakumulasi error, dan D merespons laju perubahan. Analisis tidak hanya berdasarkan bentuk grafik, tetapi juga rise time, overshoot, settling time, dan steady-state error.

## Experimental fairness
Setiap run harus mencatat kondisi awal. Metadata minimum:

| Item | Dicatat |
|---|---|
| ID run | ya |
| mode | ya |
| SV | ya |
| PV awal | ya |
| volume/kondisi plant | ya |
| interval pencatatan | ya |
| parameter controller | ya |
| posisi sensor | ya |
| catatan gangguan | ya |

Jangan membandingkan dua run sebelum memeriksa bahwa kondisi awalnya cukup setara.

## Pengambilan data manual
Gunakan stopwatch dan template. Format minimum:

`time_s,setpoint_C,temperature_C,output_state,notes`

File yang tersedia:
- `templates/template_manual.csv`
- `templates/template_pengamatan.csv`
- `templates/template_pengamatan_pemanas_air.xlsx`

Raw data disimpan apa adanya. Jika dibutuhkan data bersih, buat salinan baru dan dokumentasikan perubahan.

## Eksperimen wajib
1. Ambil satu baseline.
2. Bandingkan minimal tiga variasi hysteresis.
3. Ambil data konfigurasi PID yang ditentukan pengajar.
4. Ulangi satu konfigurasi untuk melihat repeatability.
5. Bandingkan semua run menggunakan tabel parameter dan metrics.

## Metrics respon
Analisis minimal:
- rise time;
- peak value dan peak time;
- overshoot;
- settling time;
- steady-state error.

Sampling manual mempunyai resolusi terbatas. Peak yang terjadi di antara dua waktu pencatatan dapat tidak terukur. P6 akan membandingkannya dengan logging digital.

## Analisis Python

`python examples/analyze_manual_response.py data_run.csv`

Untuk beberapa run:

`python examples/compare_manual_runs.py run1.csv run2.csv run3.csv`

## Analisis MATLAB

`run('examples/analyze_manual_response.m')`

## Troubleshooting data
- Header CSV harus konsisten.
- Waktu harus naik secara monoton.
- PV dan SV harus numerik dan memiliki satuan yang jelas.
- Catat data kosong atau pencatatan terlambat, jangan menyembunyikannya.
- Jika data antar-run sangat berbeda, audit kembali kondisi awal dan metadata.

## Keselamatan
Gunakan hanya trainer laboratorium yang telah disiapkan dan diperiksa. Mahasiswa tidak melakukan perubahan pada instalasi daya. Jika pembacaan tidak wajar atau kondisi alat tidak sesuai SOP, pengambilan data dihentikan dan dilaporkan kepada pengajar/teknisi.

## File wajib P5
- `Materi.md`
- `Jobsheet.md`
- `TugasVideo.md`
- `templates/template_pengamatan_pemanas_air.xlsx`
- `examples/analyze_manual_response.py`
- `examples/analyze_manual_response.m`
- `examples/compare_manual_runs.py`

## Jembatan ke P6
Dataset P5 adalah baseline manual. Pada P6 data yang sama jenisnya dikumpulkan dengan DAQMaster sehingga mahasiswa dapat membandingkan resolusi waktu, jumlah sampel, peak, settling time, dan potensi kesalahan pencatatan manual.
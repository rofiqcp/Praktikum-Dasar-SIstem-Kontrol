# Pertemuan 3 — Transfer Function Plant

Fokus pada tiga plant yang dipakai sepanjang semester:
1. pemanas air;
2. motor DC speed;
3. motor DC position.

## 1. Transfer function
Untuk kondisi awal nol:

`G(s)=Y(s)/U(s)`

Transfer function memudahkan analisis pole, zero, gain, time constant, dan step response.

## 2. Pemanas air — model orde satu
Pendekatan:

`tau dT/dt + T = K u`

sehingga:

`G_T(s)=K/(tau s+1)`

Parameter `K` dan `tau` harus diidentifikasi dari data aktual P5/P6. Nilai script hanyalah contoh pendidikan.

## 3. Motor DC speed
Model elektro-mekanik:

`V = L di/dt + R i + K_e omega`

`J domega/dt + b omega = K_t i`

Transfer function speed:

`Omega(s)/V(s)=Kt / ((J s+b)(L s+R)+Kt Ke)`

## 4. Motor DC position
Karena `theta_dot=omega`:

`Theta(s)/V(s) = (Omega(s)/V(s))/s`

Plant posisi memiliki integrator tambahan.

## 5. Analisis
Gunakan:
- `tf`;
- `step`;
- `pole`;
- `zero`;
- `dcgain`;
- `stepinfo`.

## 6. Simulink
`build_three_plants_simulink.m` membuat `models/three_control_plants.slx`.

## 7. Identifikasi pemanas
Dari step open-loop:
- gain kira-kira `ΔT_ss/Δu`;
- `tau` kira-kira waktu mencapai 63.2% perubahan akhir.

## Program wajib
```matlab
plant_transfer_functions
build_three_plants_simulink
```

## Program referensi dan urutan belajar
Topik inti pertemuan ini adalah **transfer function tiga plant**. Program yang harus dibuka dan dipahami:
- `plant_transfer_functions.m`
- `compare_plants.m`
- `build_three_plants_simulink.m`

Urutan kerja yang direkomendasikan: pahami persamaan/diagram → jalankan contoh default → ubah satu parameter → catat output → jelaskan sebab perubahan → simpan bukti.

## Hasil yang diharapkan
Tiga model tampil dengan pole dan step response; builder menghasilkan model Simulink di folder models.

## Validasi dan troubleshooting
Jika `tf` atau `stepinfo` tidak dikenal, cek Control System Toolbox. Pastikan satuan parameter konsisten.

Setiap hasil eksperimen harus mencatat konfigurasi, satuan, sample time/interval akuisisi, dan kondisi awal. Hasil yang “terlihat bagus” tetapi tidak dapat direproduksi belum dianggap valid.

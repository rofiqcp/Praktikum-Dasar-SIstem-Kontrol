# Simulink Models — Generator `.slx`

File `.slx` adalah format biner/versioned milik Simulink. Repository menyediakan **source generator MATLAB** sehingga model dapat dibuat ulang secara deterministik pada MATLAB/Simulink yang terpasang, bukan menyimpan file biner palsu.

Dari root repository jalankan:

```matlab
build_all_slx
```

Output yang dibuat:

| Pertemuan | Builder | Output |
|---|---|---|
| P3 | `build_three_plants_simulink.m` | `three_control_plants.slx` |
| P4 | `build_pid_manual_simulink.m` | `pid_manual_water_heater.slx` |
| P9 | `build_temp_pid_simulink.m` | `temp_pid_water_heater.slx` |
| P11 | `build_motor_speed_pid_simulink.m` | `motor_speed_pid.slx` |
| P12 | `build_motor_position_pid_simulink.m` | `motor_position_pid.slx` |

Setelah generator berhasil, buka setiap `.slx`, jalankan simulation, dan simpan lagi dengan versi MATLAB lab bila diperlukan. Builder menggunakan blok Simulink standar dan Control System Toolbox untuk bagian transfer function/PID yang terkait.

## Validasi
- jangan hanya cek file `.slx` terbentuk;
- buka model dan `Ctrl+D`/Update Diagram;
- jalankan simulasi;
- pastikan tidak ada unresolved block;
- bandingkan scope dengan script `.m` referensi;
- untuk model hardware, verifikasi board dan pin sebelum deploy.

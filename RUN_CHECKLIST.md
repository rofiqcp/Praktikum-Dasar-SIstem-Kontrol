# Checklist Program yang Harus Dijalankan — P1 sampai P16

Dokumen ini adalah indeks praktik. Setiap pertemuan harus berakhir dengan **bukti program/model dijalankan**, data/grafik yang dihasilkan, dan analisis singkat.

| P | Program/model wajib | Cara menjalankan / bukti minimum |
|---:|---|---|
| 01 | `examples/control_basics.py` | Jalankan Python; tampilkan kurva P, PI, PID dan jelaskan perbedaannya. |
| 02 | `matlab_basics.m`, `saturate.m` | Jalankan dari MATLAB; tunjukkan workspace, plot, matriks, dan pemanggilan function. |
| 03 | `plant_transfer_functions.m`, `compare_plants.m`, notebook Colab, `build_three_plants_simulink.m` | Plot step response tiga plant; buat `models/three_control_plants.slx`. |
| 04 | `pid_comparison.m`, `build_pid_manual_simulink.m` | Bandingkan PID; buat dan jalankan `pid_manual_water_heater.slx`. |
| 05 | `analyze_manual_response.m/.py`, template CSV/XLSX | Stopwatch → isi temperatur manual → simpan → plot dan hitung metrik. |
| 06 | `analyze_daqmaster.m`, `compare_runs.m` | Export DAQMaster CSV → baca MATLAB → grafik/response metrics. |
| 07 | `led_adc.m`, `adc_to_temperature_example.m` | MATLAB konek Arduino Mega, blink LED, baca ADC A0 real-time. |
| 08 | Program P1–P7 yang dipilih penguji | Responsi + demo checkpoint PCB; tidak ada `TugasVideo.md`. |
| 09 | `matlab_temp_pid.m`, `build_temp_pid_simulink.m` | PID temperatur MATLAB→Arduino D8 SSR; juga buat model simulasi `.slx`. |
| 10 | `encoder_bridge.ino`, `read_encoder_matlab.m` | Upload bridge; putar motor dua arah; tampil RPM signed dan posisi. |
| 11 | `encoder_bridge.ino`, `pid_speed_matlab.m`, `build_motor_speed_pid_simulink.m` | Closed-loop RPM dua arah + model `.slx`. |
| 12 | `encoder_bridge.ino`, `pid_position_matlab.m`, `build_motor_position_pid_simulink.m` | Closed-loop posisi + project demo; tidak ada `TugasVideo.md`. |
| 13 | PlatformIO `mega_sensors`, `plot_serial.py` | `pio run`, upload, serial; ADC/RPM/posisi terbaca dan diplot. |
| 14 | PlatformIO `mega_temp_pid`, GUI `app.py` | Kontrol suhu, live graph, save CSV dan JPG, hitung metrik respon. |
| 15 | PlatformIO `mega_motor_pid`, GUI `app.py` | Mode speed & position, live graph, save CSV dan JPG. |
| 16 | `node_serial_logger` + program P9–P15 yang dipilih penguji | Responsi/live coding/demo integrated trainer; tidak ada `TugasVideo.md`. |

## Generator semua model Simulink
Dari root repository jalankan:

```matlab
build_all_slx
```

Script ini menjalankan builder P3, P4, P9, P11, dan P12. Model sengaja **dibangun dari source `.m`** agar versi Git mudah diaudit dan model dapat diregenerasi di versi MATLAB/Simulink mahasiswa.

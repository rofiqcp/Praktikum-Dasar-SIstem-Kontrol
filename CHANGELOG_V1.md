# Changelog branch v1

## Final readiness audit
- Melakukan audit ulang P1–P16 pada branch `v1`.
- Memperketat `validate_repo.py`: struktur modul, minimum kelengkapan dokumen, program wajib, referensi source pada Markdown, marker protocol, Python syntax, dan readiness marker firmware.
- GitHub Actions sekarang menjalankan quadrature test P10.
- GitHub Actions sekarang mengompilasi sketch Arduino Mega P10, P11, dan P12 dengan PlatformIO CI.
- Build PlatformIO P13, P14, dan P15 tetap menjadi regression gate.
- Memperbaiki P11 ZERO agar count, `lastCount`, buffer RPM, LPF, dan state PID di-reset bersama sehingga tidak muncul RPM palsu setelah perubahan reference.
- Memperbaiki P12 ZERO agar perubahan reference selalu dilakukan dalam state berhenti.
- Memperbaiki P13 ZERO agar estimator RPM ikut di-reset bersama encoder count.
- Memperbaiki P15 ZERO/mode transition agar histori estimator speed tidak terbawa ke reference baru.
- Memperluas P13 `Materi.md` dan `Jobsheet.md` menjadi modul PlatformIO/ADC/encoder/filter/AI yang lebih lengkap.
- Memperluas P16 `Materi.md` dan `Jobsheet.md` menjadi final responsi dan acceptance workflow P9–P15.
- Menambahkan `READINESS_V1.md` sebagai catatan status validasi repository, batas automated testing, dan kriteria branch siap digunakan.
- Audit sebelumnya juga telah menyelaraskan model Simulink P9/P11/P12 terhadap model P3, memperbaiki P12 offline simulation, memperkeras analyzer data, dan menutup legacy workflow P11.

## Complete lab-ready pass
- Memperluas seluruh P1–P16 menjadi jalur belajar yang konsisten dengan materi/jobsheet/tugas atau project.
- Mengganti plant temperatur menjadi **pemanas air**.
- Menetapkan trainer Arduino Mega: SSR heater + L293D motor + encoder A/B.
- Menambahkan source generator Simulink P3/P4/P9/P11/P12 dan `build_all_slx.m`.
- Menambahkan MATLAB, Python, Arduino sketch dan PlatformIO runnable examples.
- Menambahkan P5 template pengamatan stopwatch, analisis CSV dan workbook Excel.
- Menambahkan DAQMaster -> MATLAB/Python analysis pada P6.
- Menambahkan MATLAB-Arduino LED/ADC P7.
- Menambahkan responsi/checkpoint P8 tanpa TugasVideo.
- Menambahkan PID suhu P9, encoder P10, PID speed P11, project PID position P12.
- Menambahkan PlatformIO/AI P13.
- Menambahkan firmware + GUI P14 dengan demo mode, heartbeat, fault, over-temperature, CSV/XLSX/JPG dan response metrics.
- Menambahkan firmware + GUI P15 speed/position, raw/MA/LPF, zero encoder, stall/heartbeat fault, CSV/XLSX/JPG dan response metrics.
- Menambahkan P16 passive smoke test dan Node serial logger.
- Menambahkan dokumentasi installation, wiring, safety, testing, serial protocol, troubleshooting, Simulink generation dan repository validator/CI.

## Hardware safety
Sisi daya trainer mengikuti desain dan prosedur laboratorium. Dokumentasi repository berfokus pada kontrol, firmware, data, dan integrasi software; pemeriksaan kesiapan fisik tetap wajib dilakukan oleh instruktur/teknisi sebelum sesi mahasiswa.

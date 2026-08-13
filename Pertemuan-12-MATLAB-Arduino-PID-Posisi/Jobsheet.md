# Jobsheet Pertemuan 12 — PID Posisi dan Project

## Tujuan
Menganalisis reference posisi, response P/PD/PID, target bertanda, repeatability, saturation, dan response metrics sebagai checkpoint project.

## Urutan kerja
1. Baca `Materi.md`.
2. Selesaikan `WORKSHEET_ANALISIS.md`.
3. Jalankan contoh offline yang tercantum di worksheet.
4. Audit source firmware dan MATLAB logger.
5. Analisis CSV project menggunakan worksheet.
6. Lengkapi deliverable pada `Project.md`.

## File utama
```text
examples/arduino_position_pid/arduino_position_pid.ino
examples/matlab_position_pid_experiment.m
examples/position_pid_offline.m
examples/position_reference_profile.m
examples/analyze_position_pid_log.m
examples/build_motor_position_pid_simulink.m
WORKSHEET_ANALISIS.md
Project.md
```

## Gate kelulusan
- [ ] CPR dan sign dari P10 terdokumentasi;
- [ ] reference zero dijelaskan;
- [ ] P/PD/PID dibandingkan;
- [ ] target positif dan negatif dianalisis;
- [ ] repeatability dibahas;
- [ ] CSV/PNG/metrics tersedia;
- [ ] source PID dapat dijelaskan;
- [ ] deliverable `Project.md` lengkap.

P12 tidak menggunakan `TugasVideo.md`; tugas pengganti adalah `Project.md`.

## Expected result
Mahasiswa dapat mempertanggungjawabkan data position loop dari reference, feedback, PID terms, sampai response metrics dan repeatability.
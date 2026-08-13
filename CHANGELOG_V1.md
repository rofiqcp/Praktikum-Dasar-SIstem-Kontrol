# Changelog branch v1 — Silabus 16 Pertemuan

## Revisi utama
- Mengubah plant temperatur menjadi **pemanas air**.
- Menetapkan project hardware Arduino Mega 2560 dengan jalur **SSR pemanas air** dan **motor DC + encoder + L293D**.
- Menata ulang P7–P16 sesuai silabus terbaru: MATLAB–Arduino → responsi → PID suhu → RPM/posisi → PID speed/position → PlatformIO/AI → GUI → responsi final.
- Menetapkan `Project.md` khusus P8, P12, P16; pertemuan lain menggunakan `TugasVideo.md`.
- Menambahkan program runnable dan checklist eksekusi P1–P16.
- Menambahkan generator Simulink `build_*.m` serta `build_all_slx.m` untuk membuat model `.slx` di MATLAB/Simulink.
- Menambahkan template Excel pengamatan manual pemanas air untuk P5.
- Menambahkan analisis DAQMaster CSV dengan MATLAB pada P6.
- Menambahkan firmware serial encoder, PID MATLAB, proyek PlatformIO, GUI PyQt5, ekspor CSV/JPG, dan metrik respon.
- Memperkuat catatan keselamatan untuk SSR/mains dan penggunaan plant low-voltage/terisolasi.

## Validasi sebelum publish
- Struktur 16 pertemuan diverifikasi otomatis.
- Python source lolos `py_compile`.
- Notebook `.ipynb` dan JSON lolos parse.
- Node.js source lolos `node --check`.
- GUI P15 diperbaiki dari indeks telemetri P/I/D/PID yang salah.
- PlatformIO CLI dan MATLAB/Simulink runtime tidak tersedia pada environment validasi; firmware dan builder diaudit statis dan harus dibuild/run pada toolchain yang sesuai di laboratorium.

## Catatan `.slx`
File `.slx` adalah format model Simulink yang normalnya ditulis oleh MATLAB/Simulink. Repository menyimpan builder `.m` sebagai source-of-truth agar model dapat diregenerasi dan diaudit tanpa mengunggah model biner palsu. Jalankan `build_all_slx` dari root repository di MATLAB.

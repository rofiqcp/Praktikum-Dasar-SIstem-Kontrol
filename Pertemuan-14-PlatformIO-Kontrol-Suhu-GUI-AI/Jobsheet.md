# Jobsheet Pertemuan 14 — PID Suhu Embedded dan GUI

## Tujuan
Memvalidasi workflow P14 dari source firmware sampai GUI, logging, metrics, dan review AI.

Gunakan **`SOFTWARE_VALIDATION.md`** sebagai worksheet rinci. File tersebut memuat tabel protocol, build checklist, GUI demo, export, metrics, source audit, state/heartbeat, troubleshooting, dan AI review.

## Urutan kerja
1. Baca `Materi.md`.
2. Audit `examples/mega_temp_pid/platformio.ini` dan `src/main.cpp`.
3. Jalankan `pio run` dan simpan bukti build.
4. Cocokkan protocol `TEMP_PID,2` dengan `FIELDS` pada GUI.
5. Jalankan `examples/gui/app.py --demo`.
6. Uji Start/Stop, SP/gain, grafik, Clear Data, dan Save pada demo.
7. Buka CSV/XLSX/JPG yang dihasilkan.
8. Hitung dan interpretasikan response metrics pada satu segmen step.
9. Audit `PIDCore.h`, state STOP/RUN/FAULT, heartbeat, dan parser GUI.
10. Selesaikan satu review AI dengan bukti syntax/build/demo test.
11. Isi seluruh bagian `SOFTWARE_VALIDATION.md`.

## File utama

```text
examples/mega_temp_pid/platformio.ini
examples/mega_temp_pid/src/main.cpp
examples/mega_temp_pid/lib/PIDCore/PIDCore.h
examples/gui/app.py
examples/gui/response_metrics.py
examples/gui/requirements.txt
SOFTWARE_VALIDATION.md
PROMPT_AI_CONTOH.md
```

## Gate kelulusan
- [ ] firmware build sukses;
- [ ] protocol firmware dan GUI konsisten;
- [ ] GUI demo berjalan;
- [ ] CSV/XLSX/JPG dapat dibuat dan dibuka;
- [ ] metrics dapat dijelaskan;
- [ ] PIDCore dapat dijelaskan;
- [ ] state/heartbeat dapat dijelaskan;
- [ ] worksheet software selesai;
- [ ] AI review mempunyai bukti test.

## Expected result
Mahasiswa dapat menunjukkan hubungan source → protocol → GUI → data → metrics dan dapat melakukan diagnosis bila salah satu tahap gagal.
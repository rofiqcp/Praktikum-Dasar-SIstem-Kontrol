# Referensi Materi dan Jejak Sumber

Repository ini merupakan implementasi praktikum dari bahan kuliah/panduan yang diberikan untuk mata kuliah Dasar Sistem Kontrol, kemudian disusun ulang mengikuti format repository Praktikum Sistem Embedded.

Sumber internal yang menjadi dasar topik meliputi materi: dasar sistem kontrol/PID; dasar MATLAB/Simulink; pemodelan sistem dinamis; Autonics TK4S/T4RN; DAQMaster; PWM dan encoder motor DC; PID speed/position; serta PlatformIO + Python GUI. Manual Autonics digunakan untuk terminologi ON/OFF hysteresis, PID, komunikasi dan DAQ logging.

## Referensi teori umum yang direkomendasikan
1. K. Ogata, *Modern Control Engineering*.
2. R. C. Dorf & R. H. Bishop, *Modern Control Systems*.
3. Dokumentasi MATLAB/Simulink dan Control System Toolbox yang sesuai versi lab.
4. Dokumentasi Arduino Mega 2560 dan ATmega2560.
5. Datasheet L293/L293D dari pabrikan komponen yang digunakan.
6. Manual controller Autonics TK Series dan DAQMaster untuk model aktual di laboratorium.

## Catatan reproducibility
Nilai parameter plant pada contoh P3/P4 adalah model pedagogik. Untuk laporan eksperimen, mahasiswa harus mengganti/mengidentifikasi parameter berdasarkan plant aktual dan menyatakan satuan, metode identifikasi, sample time dan kondisi pengujian.

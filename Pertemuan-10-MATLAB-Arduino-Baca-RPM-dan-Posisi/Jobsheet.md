# Pertemuan 10 — Jobsheet — Encoder, RPM, Position


1. Upload `arduino_bridge/encoder_bridge.ino` via Arduino IDE atau PlatformIO sementara.
2. Set `PPR` sesuai encoder.
3. Jalankan `read_encoder_matlab.m`, pilih COM.
4. Putar motor manual; cek count +/−.
5. Kirim `M,80`, `M,-80`, `STOP` dari MATLAB/Serial Monitor.
6. Verifikasi RPM positif/negatif dan position.
7. Bandingkan RPM dengan tachometer bila tersedia.
8. Uji noise saat motor berhenti.

**Output:** CSV count, angle, rpm dan grafik.

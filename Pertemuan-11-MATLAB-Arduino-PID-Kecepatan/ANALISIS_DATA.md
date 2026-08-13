# Panduan Analisis Data P11

Gunakan file ini bersama `Jobsheet.md` untuk memperdalam analisis telemetry speed PID.

## Metadata wajib
Catat nama file, CPR, sample interval, Kp/Ki/Kd, setpoint, output limit, filter RPM, kondisi load, dan jumlah sampel.

## Grafik wajib
1. SP vs RPM;
2. error;
3. P/I/D;
4. output controller;
5. encoder count bila diperlukan untuk audit sign.

## P / PI / PID
| Mode | Kp | Ki | Kd | Rise | Overshoot | Settling | SSE | Max output |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P | | 0 | 0 | | | | | |
| PI | | | 0 | | | | | |
| PID | | | | | | | | |

Jelaskan perubahan berdasarkan data, bukan hanya bentuk grafik.

## Positive / negative comparison
Pisahkan segmen setpoint positif dan negatif. Bandingkan magnitude response metrics, final error, maximum output, dan waktu menuju kondisi tunak.

## Saturation audit
Hitung atau tandai bagian ketika absolute output mendekati limit. Jangan menilai gain tanpa menyebut apakah controller berada di saturation.

## Filter audit
Hubungkan hasil P11 dengan P10. Jelaskan tradeoff raw/MA/LPF antara noise dan delay.

## Source audit
Tunjukkan bagian source yang menangani:
- feedback RPM;
- error;
- P/I/D;
- anti-windup;
- saturation;
- telemetry;
- state stop dan host timeout.

## Pertanyaan akhir
1. Mengapa response dua arah dapat berbeda?
2. Mengapa Ki dapat mengurangi SSE namun menambah overshoot?
3. Bagaimana filter memengaruhi closed-loop response?
4. Apa arti output terus saturated?
5. Bagaimana membedakan masalah feedback dari masalah tuning?
6. Apa bukti bahwa data dapat direproduksi?

## Output laporan
Sertakan raw CSV, hasil plot, metrics per segmen, tabel gain, metadata, serta kesimpulan yang menyebut keterbatasan eksperimen.
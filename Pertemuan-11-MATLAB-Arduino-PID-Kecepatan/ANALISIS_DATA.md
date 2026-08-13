# Panduan Analisis Data P11 — PID Kecepatan

Gunakan file ini bersama `Jobsheet.md`. Fokus analisis adalah kualitas feedback, perilaku PID, pengaruh batas output, dan konsistensi respons pada arah positif maupun negatif.

## Metadata wajib
Catat untuk setiap dataset:
- nama file;
- CPR;
- interval sampling;
- Kp, Ki, Kd;
- setpoint;
- batas output;
- parameter filter RPM;
- kondisi beban;
- jumlah sampel;
- kondisi awal RPM.

Tanpa metadata tersebut, dua dataset tidak dapat dibandingkan secara adil.

## Grafik wajib
1. SP dan RPM;
2. error;
3. P, I, dan D;
4. output controller;
5. encoder count bila diperlukan untuk audit tanda;
6. interval sampling bila kualitas timing diragukan.

## Perbandingan P, PI, dan PID
| Mode | Kp | Ki | Kd | Rise time | Overshoot | Settling time | SSE | Output maksimum |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P | | 0 | 0 | | | | | |
| PI | | | 0 | | | | | |
| PID | | | | | | | | |

Jelaskan perubahan berdasarkan data, bukan hanya berdasarkan bentuk grafik.

## Perbandingan arah positif dan negatif
Pisahkan segmen setpoint positif dan negatif. Bandingkan:
- rise time;
- settling time;
- overshoot;
- steady-state error;
- output maksimum;
- lama kondisi saturasi.

Perbedaan dua arah dapat dipengaruhi friction, gearbox, driver, supply, beban, atau konvensi tanda. Karena itu penyebabnya tidak boleh langsung dianggap berasal dari tuning PID.

## Audit saturasi
Tandai bagian ketika nilai absolut output mendekati batas. Bila memungkinkan, hitung persentase sampel yang berada di sekitar batas tersebut.

Gain yang menghasilkan respons cepat tetapi membuat output hampir selalu saturasi harus dibedakan dari tuning yang bekerja lebih banyak pada daerah non-saturasi.

## Audit integral dan anti-windup
Periksa perilaku komponen I ketika output berada pada batas. Jawab:
1. kapan integral mulai dominan?
2. apakah integral membantu mengurangi SSE?
3. apakah integral memperbesar overshoot?
4. apakah perilaku integral sesuai dengan conditional anti-windup pada source?

## Audit filter
Hubungkan hasil P11 dengan P10. Jelaskan kompromi antara pengurangan noise dan tambahan delay pada moving average dan LPF.

Filter yang paling halus tidak selalu menjadi feedback terbaik bila keterlambatannya terlalu besar.

## Audit source
Tunjukkan bagian source yang menangani:
- feedback RPM;
- error;
- P, I, dan D;
- anti-windup;
- saturasi;
- telemetry;
- state berhenti dan host timeout.

## Analisis per segmen
Jika satu dataset mempunyai beberapa setpoint, pisahkan setiap segmen yang relevan sebelum menghitung response metrics. Jangan menghitung satu rise time atau settling time untuk seluruh profil multi-setpoint.

## Pertanyaan akhir
1. Mengapa respons dua arah dapat berbeda walaupun besar setpoint sama?
2. Mengapa Ki dapat mengurangi SSE tetapi menambah overshoot?
3. Bagaimana filter memengaruhi respons closed-loop?
4. Apa arti output yang terus berada pada kondisi saturasi?
5. Bagaimana membedakan masalah feedback dari masalah tuning?
6. Bagaimana mendeteksi kesalahan tanda dari telemetry?
7. Apa bukti bahwa hasil dapat direproduksi?
8. Parameter apa yang harus dibuat sama ketika dua tuning dibandingkan?

## Output laporan
Sertakan raw CSV, grafik hasil analisis, response metrics per segmen, tabel gain, metadata lengkap, perbandingan arah positif dan negatif, catatan saturasi, serta kesimpulan yang menyebut keterbatasan eksperimen.

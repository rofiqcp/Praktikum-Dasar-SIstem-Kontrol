# P14 Software Validation Worksheet

Gunakan worksheet ini bersama `Jobsheet.md` untuk memvalidasi firmware dan GUI P14 sebelum menilai data eksperimen.

## 1. Identitas source
Catat:

| Item | Nilai |
|---|---|
| branch | v1 |
| commit | |
| firmware path | `examples/mega_temp_pid` |
| GUI path | `examples/gui` |
| Python version | |
| PlatformIO version | |

## 2. Build firmware
Jalankan:

```bash
cd examples/mega_temp_pid
pio run
```

Catat:

| Pemeriksaan | Hasil |
|---|---|
| environment megaatmega2560 | |
| build success | |
| flash usage | |
| RAM usage | |
| warning penting | |

Jika gagal, tuliskan error pertama yang relevan dan koreksinya.

## 3. Protocol audit
Header firmware:

```text
#PROTO,TEMP_PID,2
#ms,temp_C,sp_C,error,P,I,D,pid_pct,ssr,fault
```

Isi tabel:

| Kolom | Arti | Satuan | Dipakai GUI? |
|---|---|---|---|
| ms | | | |
| temp_C | | | |
| sp_C | | | |
| error | | | |
| P | | | |
| I | | | |
| D | | | |
| pid_pct | | | |
| ssr | | | |
| fault | | | |

Pastikan `FIELDS` pada GUI mempunyai urutan yang sama.

## 4. GUI demo
Jalankan:

```bash
cd ../gui
pip install -r requirements.txt
python app.py --demo
```

Checklist:
- [ ] GUI terbuka;
- [ ] Demo Connect berhasil;
- [ ] Start/Stop berubah state;
- [ ] SP dapat diubah;
- [ ] Kp/Ki/Kd dapat diubah;
- [ ] PV/SP tampil;
- [ ] P/I/D/PID tampil;
- [ ] Clear Data bekerja;
- [ ] Save bekerja.

## 5. File hasil
Setelah Save, periksa:

- [ ] CSV tersedia;
- [ ] XLSX tersedia;
- [ ] JPG tersedia;
- [ ] metrics CSV tersedia;
- [ ] jumlah baris masuk akal;
- [ ] timestamp meningkat;
- [ ] kolom tidak berubah urutan;
- [ ] nilai numerik dapat dibaca ulang.

## 6. Gain comparison demo
Lakukan minimal tiga run demo:

| Run | Kp | Ki | Kd | Rise | Overshoot | Settling | SSE |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Jelaskan perubahan term P/I/D dan output, bukan hanya PV.

## 7. PIDCore audit
Temukan dan jelaskan:
- output limit;
- P term;
- candidate integral;
- conditional anti-windup;
- derivative-on-measurement;
- reset state.

Catatan source:

```text

```

## 8. State/heartbeat audit
Temukan:
- `running`;
- `fault`;
- `lastPing`;
- timeout;
- `stopControl()`;
- `setFault()`;
- command RUN/PING/CLEAR.

Gambarkan state:

```text
STOP -> RUN -> FAULT
 ^              |
 +--------------+
```

Sesuaikan panah dengan kondisi yang benar berdasarkan source.

## 9. Parser GUI audit
Identifikasi:
- `SerialDevice`;
- `DemoDevice`;
- parser baris `#`;
- parser 10 kolom;
- pengecekan finite values;
- heartbeat timer;
- DataFrame;
- export;
- `step_metrics`.

## 10. Metrics audit
Pilih satu segmen step yang jelas dan tulis:

| Metric | Nilai | Interpretasi |
|---|---:|---|
| delay | | |
| rise | | |
| peak | | |
| overshoot | | |
| settling | | |
| SSE | | |

Jelaskan mengapa metrics satu file multi-setpoint harus dipisahkan per segmen.

## 11. AI review
Catat:

```text
Requirement:
Prompt:
Output AI:
Risiko yang diperiksa:
Build/syntax/demo test:
Keputusan akhir:
```

## 12. Troubleshooting
Jawab berdasarkan source:

1. GUI tidak melihat port: apa yang diaudit?
2. Port terbuka tetapi tidak ada telemetry: apa yang diaudit?
3. Telemetry ada tetapi parser kosong: apa yang diaudit?
4. File XLSX gagal dibuat: dependency apa yang diperiksa?
5. Metrics tidak masuk akal: bagian data apa yang diperiksa?
6. Timeout muncul: state/heartbeat apa yang diperiksa?

## 13. Gate software
- [ ] build firmware PASS;
- [ ] protocol cocok;
- [ ] GUI demo PASS;
- [ ] Save CSV/XLSX/JPG PASS;
- [ ] metrics dapat dihitung;
- [ ] PIDCore dapat dijelaskan;
- [ ] state/heartbeat dapat dijelaskan;
- [ ] AI review mempunyai bukti test.

Kesimpulan:

```text
PASS / REVISI
Alasan:
```

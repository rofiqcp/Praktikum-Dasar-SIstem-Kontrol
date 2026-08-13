# Project Pertemuan 08 — UTS PCB Arduino Mega Control Trainer

## Tujuan
Merealisasikan checkpoint hardware semester: satu PCB/shield Arduino Mega 2560 untuk plant pemanas air dan motor DC encoder.

## Requirement Wajib
- Arduino Mega 2560 header compatible.
- L293D untuk motor DC kecil + terminal supply motor.
- Encoder A/B ke pin interrupt D2/D3.
- PWM motor default D5/D6.
- Output logika SSR D8 + LED indikator.
- Header sensor suhu (minimal SPI MAX6675/MAX31855 atau interface setara).
- Test point rail dan sinyal.
- Silkscreen pin/fungsi.
- Tidak membawa mains AC pada PCB mahasiswa.

## Deliverable
1. schematic PDF/PNG;
2. PCB layout top/bottom;
3. BOM;
4. hasil ERC/DRC;
5. foto PCB/assembly atau prototype bila fabrikasi belum selesai;
6. video bring-up;
7. source code `examples/mega_trainer_bringup` berhasil build/upload.

## Test Acceptance
- serial startup tampil;
- encoder count berubah sesuai arah;
- PWM CW/CCW dapat diuji dengan duty rendah;
- SSR output dapat menyalakan LED dummy;
- pembacaan sensor suhu tidak NaN/open circuit;
- tidak ada short rail.

## Penilaian
| Aspek | Bobot |
|---|---:|
| Schematic & DRC | 25% |
| Safety/segregasi power | 20% |
| PCB routing & labeling | 20% |
| Bring-up code | 20% |
| Dokumentasi/video | 15% |

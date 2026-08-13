# Project P8 — PCB Control Trainer Checkpoint

## Deliverable wajib
1. schematic;
2. PCB layout;
3. BOM;
4. Gerber;
5. foto top/bottom;
6. pin map;
7. continuity checklist;
8. low-voltage power test;
9. I/O bring-up log.

## Acceptance tests

### 1. Power OFF
- [ ] VCC-GND tidak short.
- [ ] D5→PWM_CW.
- [ ] D6→PWM_CCW.
- [ ] D2→ENC_A.
- [ ] D3→ENC_B.
- [ ] D8→SSR_OUT.
- [ ] A0→TEMP_ADC.
- [ ] A1→AUX_ADC.

### 2. Power ON low-voltage
- [ ] Arduino USB terdeteksi.
- [ ] tidak ada komponen panas abnormal.
- [ ] rail sesuai.

### 3. I/O
Gunakan program `examples/pcb_bringup/pcb_bringup.ino`.

Command serial:
- `LED`
- `ADC`
- `ENC`
- `CW,50`
- `CCW,50`
- `STOP`
- `SSR,1`
- `SSR,0`

Pada tahap ini motor/heater aktual boleh diganti dummy LED/load.

## Kriteria gagal langsung
- short power;
- polaritas salah;
- output aktif saat boot;
- D5 dan D6 aktif bersamaan;
- SSR aktif saat reset tanpa command.

## Bukti
Satu PDF laporan project + folder source desain + foto/video singkat pengujian.

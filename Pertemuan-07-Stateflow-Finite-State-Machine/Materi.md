# Pertemuan 07 — Finite State Machine dengan Stateflow MATLAB/Simulink

## Capaian Pembelajaran
- memahami state, event, transition, dan action
- mempraktikkan FSM MP3/traffic light/turning signal
- menggunakan entry/during/exit
- menghubungkan FSM dengan supervisory control

## Materi Inti

## Finite State Machine (FSM)
FSM adalah model perilaku diskrit yang memiliki sejumlah **state**, **event/input**, **transition**, dan **action**. Pada satu saat sistem berada pada satu state aktif dan berpindah state ketika kondisi transisi terpenuhi.

Komponen utama:
- **State**: kondisi operasi, misalnya `STOP`, `PLAY`, `PAUSE`.
- **Event/Input**: pemicu perpindahan.
- **Transition**: aturan perpindahan antarstate.
- **Action**: aksi `entry`, `during`, dan `exit`.

## Stateflow di MATLAB/Simulink
Stateflow dipakai untuk memodelkan logika sekuensial/discrete yang dipadukan dengan plant Simulink. Praktikum membahas tiga contoh dari materi sumber:
1. MP3 player: Play/Pause/Stop/Next/Prev.
2. Traffic light: Red/Green/Yellow berbasis timer.
3. Turning signal: Off/Left/Right berbasis input.

Stateflow cocok untuk supervisory control, mode switching, interlock, sequencing, serta state machine embedded. Pada control trainer, konsep ini akan dipakai untuk state `IDLE`, `MOTOR`, `HEATER`, `FAULT`, dan `E_STOP` pada project akhir.


## Program yang Wajib Dijalankan
- `examples/fsm_examples.m`
- `examples/build_traffic_light_stateflow.m`

## Alur Praktikum
1. Jalankan `examples/fsm_examples.m` dan amati trace state pada Command Window.
2. Ubah urutan event MP3 player dan cek state akhir.
3. Ubah durasi lampu traffic light dan plot hasilnya.
4. Uji input turning signal Left/Right/Off.
5. Jalankan `examples/build_traffic_light_stateflow.m` jika Stateflow tersedia.
6. Buka model `.slx` yang dibuat dan inspeksi state, transition, dan `after(...,sec)`.
7. Buat satu state FAULT tambahan dan jelaskan kondisi masuk/keluarnya.


## Output Minimal
- program/model dapat dijalankan;
- data/grafik disimpan;
- parameter penting dicatat;
- hasil dibandingkan dengan teori;
- kesimpulan menjawab pengaruh parameter kontrol terhadap respon plant.

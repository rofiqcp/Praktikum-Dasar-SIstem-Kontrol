# Pertemuan 12 — MATLAB–Arduino Kontrol PID Posisi Motor DC


## Tujuan
Mengendalikan posisi encoder ke setpoint count/degree dengan PID bertanda dan memahami perbedaan plant posisi vs speed.

## Zero/homing praktikum
Untuk trainer tanpa absolute encoder, `Z` menjadikan count saat ini sebagai nol. Ini bukan homing keselamatan otomatis. Bila mekanisme memiliki hard-stop, jangan membuat prosedur homing yang menabrak hard-stop tanpa current/limit switch protection.

## Error posisi
`e_pos = SP_count - count`. Command PID -255…255. Dekat target dapat diberi deadband kecil untuk mencegah dithering karena quantization/friction.

## Derivative
Derivative position error berkaitan dengan velocity. Filter derivative atau gunakan velocity terukur secara hati-hati bila noise besar.

## Kriteria
Accuracy, overshoot posisi, settling, repeatability dari beberapa initial position, dan kemampuan bergerak dua arah.

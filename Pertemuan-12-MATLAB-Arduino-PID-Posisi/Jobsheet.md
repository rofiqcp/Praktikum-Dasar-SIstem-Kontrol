# Jobsheet Pertemuan 12

## A. Safety
- lepaskan beban berbahaya;
- set MAXPWM rendah;
- pastikan ruang gerak mekanik cukup.

## B. Zero
Kirim `ZERO,1`.

## C. Target
Uji +90°, 0°, -90°.

## D. PID
Mulai PD/P: Ki=0, tune Kp, tambah Kd, tambah Ki bila perlu.

## E. MATLAB
`matlab_position_pid_experiment.m`.

## F. Project
Ikuti `Project.md`.

## Expected result
Target sudut positif/negatif tercapai tanpa hard-stop dan STOP mematikan kedua arah.

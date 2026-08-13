# Pertemuan 04 — MATLAB PID dan PID Block Dibuat Sendiri


## Tujuan
Membandingkan PID MATLAB dengan implementasi P+I+D yang dibangun sendiri dan memahami setiap sinyal internal.

## Struktur
`e = r-y`, `P=Kp*e`, `I=Ki*∫e dt`, `D=Kd*de/dt`, `u=P+I+D` lalu saturation.

Derivative nyata sebaiknya difilter: `D(s)=Kd*N*s/(s+N)` atau bentuk ekuivalen agar noise frekuensi tinggi tidak diperkuat tanpa batas.

## Anti-windup
Jika actuator hanya mampu 0–100% (heater) atau -255…255 (motor), integrator dapat terus membesar saat command saturasi. Solusi: conditional integration, clamping, atau back-calculation.

## Tuning
Gunakan `pid`, `pidtune`, `feedback`, dan `stepinfo` untuk eksperimen. Nilai tuning MATLAB adalah titik awal; verifikasi selalu pada plant dan batas aktuator nyata.

## Model Simulink
`build_pid_manual_simulink.m` membuat model lengkap: Step → Sum error → cabang P/I/D → Sum PID → Saturation → Plant → Scope + feedback. Builder menyimpan model sebagai `.slx` agar model dapat diregenerasi dari source.

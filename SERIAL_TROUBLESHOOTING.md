# Troubleshooting Serial

## Port tidak muncul
- cek kabel data USB;
- cek Device Manager / `/dev/ttyACM*`;
- tutup Serial Monitor lain;
- refresh GUI.

## `Permission denied` Linux
Tambahkan user ke `dialout`, logout/login.

## Data acak
- pastikan baud 115200;
- satu baris telemetry harus diakhiri `\n`;
- jangan mencetak debug bebas ke stream CSV; gunakan prefix `#`.

## GUI disconnect
Firmware harus tetap aman. Untuk motor/heater, tekan STOP sebelum disconnect.

## COM berubah
Jangan hard-code COM di firmware. Pilih dari GUI atau parameter MATLAB.

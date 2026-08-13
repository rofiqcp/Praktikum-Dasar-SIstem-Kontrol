# Pertemuan 10 — MATLAB–Arduino Baca RPM dan Posisi Motor DC


## Tujuan
Membaca encoder quadrature A/B secara andal di Arduino interrupt, mengirim count dan RPM ke MATLAB, mengubah count menjadi putaran/sudut, dan memeriksa tanda arah.

## Encoder
Untuk quadrature, arah ditentukan dari hubungan phase A/B. Contoh firmware menghitung pada CHANGE channel A. Nilai `PPR` harus disesuaikan dengan **counts per mechanical revolution** yang benar setelah mempertimbangkan metode decoding dan gearbox.

`rpm = DeltaCount / PPR / DeltaTime * 60`

`angle_deg = count/PPR*360`

## Mengapa ISR di Arduino?
Pulse encoder dapat datang lebih cepat daripada loop komunikasi PC. ISR mengamankan count di MCU; MATLAB menerima data yang sudah diringkas.

## Validasi arah
Command positif harus menghasilkan RPM/count bertanda positif menurut konvensi lab. Bila sensor negatif, jangan langsung `abs()`; perbaiki konvensi wiring/arah atau sign di satu tempat yang terdokumentasi.

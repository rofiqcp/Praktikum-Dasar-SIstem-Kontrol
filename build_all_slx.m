function build_all_slx
% BUILD_ALL_SLX Membuat semua model Simulink yang disediakan repository.
repo = fileparts(mfilename('fullpath'));
builders = {
    fullfile(repo,'Pertemuan-03-Transfer-Function-Plant','examples','build_three_plants_simulink.m')
    fullfile(repo,'Pertemuan-04-PID-MATLAB-dan-Blok-Manual','examples','build_pid_manual_simulink.m')
    fullfile(repo,'Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID','examples','build_temp_pid_simulink.m')
    fullfile(repo,'Pertemuan-11-MATLAB-Arduino-PID-Kecepatan','examples','build_motor_speed_pid_simulink.m')
    fullfile(repo,'Pertemuan-12-MATLAB-Arduino-PID-Posisi','examples','build_motor_position_pid_simulink.m')
};
for k = 1:numel(builders)
    fprintf('\n=== Running %s ===\n', builders{k});
    old = pwd;
    cleaner = onCleanup(@() cd(old)); %#ok<NASGU>
    cd(fileparts(builders{k}));
    run(builders{k});
    clear cleaner
end
fprintf('\nSemua builder selesai. Cek folder models/ pada pertemuan terkait.\n');
end

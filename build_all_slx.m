function build_all_slx()
%BUILD_ALL_SLX Build all Simulink .slx artifacts from auditable MATLAB sources.
root=fileparts(mfilename('fullpath'));
items={...
 {'Pertemuan-03-Transfer-Function-Plant','build_three_plants_simulink'},...
 {'Pertemuan-04-PID-MATLAB-dan-Blok-Manual','build_pid_manual_simulink'},...
 {'Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID','build_temp_pid_simulink'},...
 {'Pertemuan-11-MATLAB-Arduino-PID-Kecepatan','build_motor_speed_pid_simulink'},...
 {'Pertemuan-12-MATLAB-Arduino-PID-Posisi','build_motor_position_pid_simulink'}};
old=pwd;cleanup=onCleanup(@()cd(old));
for i=1:numel(items)
    module=items{i}{1};fn=items{i}{2};ex=fullfile(root,module,'examples');
    fprintf('\n=== %s : %s ===\n',module,fn);addpath(ex);cd(ex);
    feval(fn);rmpath(ex);cd(root);
end
fprintf('\nAll builders completed. Inspect each module/models directory.\n');
end

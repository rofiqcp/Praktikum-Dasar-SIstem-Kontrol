clear; clc;

model='motor_speed_pid';
baseDir=fileparts(mfilename('fullpath'));
outdir=fullfile(baseDir,'..','models');
if ~exist(outdir,'dir'),mkdir(outdir);end

if bdIsLoaded(model),close_system(model,0);end
new_system(model);
open_system(model);

add_block('simulink/Sources/Step',[model '/RPM Setpoint'], ...
    'Time','0.5','Before','0','After','100','Position',[30 55 65 85]);
add_block('simulink/Math Operations/Sum',[model '/Error'], ...
    'Inputs','+-','Position',[110 52 135 88]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID Speed'], ...
    'P','0.5','I','0.2','D','0','SampleTime','0.05','Position',[180 45 275 95]);
add_block('simulink/Discontinuities/Saturation',[model '/PWM Limit'], ...
    'UpperLimit','180','LowerLimit','-180','Position',[320 52 390 88]);

% Convert signed PWM count to an equivalent armature voltage for the
% conceptual 12 V motor model.
add_block('simulink/Math Operations/Gain',[model '/PWM to Voltage'], ...
    'Gain','12/255','Position',[430 52 505 88]);

% Same physical baseline as P3:
% J=0.01, b=0.1, Kt=Ke=0.01, R=1, L=0.5
% Omega(s)/V(s) = 0.01 / (0.005 s^2 + 0.06 s + 0.1001)
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Speed rad_s'], ...
    'Numerator','0.01','Denominator','[0.005 0.06 0.1001]', ...
    'Position',[545 48 680 92]);
add_block('simulink/Math Operations/Gain',[model '/rad_s to RPM'], ...
    'Gain','60/(2*pi)','Position',[720 52 795 88]);

add_block('simulink/Signal Routing/Mux',[model '/Mux'], ...
    'Inputs','2','Position',[845 45 850 105]);
add_block('simulink/Sinks/Scope',[model '/Scope'], ...
    'Position',[900 55 935 90]);

add_line(model,'RPM Setpoint/1','Error/1');
add_line(model,'Error/1','PID Speed/1');
add_line(model,'PID Speed/1','PWM Limit/1');
add_line(model,'PWM Limit/1','PWM to Voltage/1');
add_line(model,'PWM to Voltage/1','DC Motor Speed rad_s/1');
add_line(model,'DC Motor Speed rad_s/1','rad_s to RPM/1');
add_line(model,'rad_s to RPM/1','Error/2','autorouting','on');
add_line(model,'RPM Setpoint/1','Mux/1','autorouting','on');
add_line(model,'rad_s to RPM/1','Mux/2');
add_line(model,'Mux/1','Scope/1');

set_param(model,'StopTime','10');
save_system(model,fullfile(outdir,[model '.slx']));
open_system(model);
fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

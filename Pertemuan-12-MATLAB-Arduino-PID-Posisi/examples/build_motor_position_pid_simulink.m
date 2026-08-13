clear; clc;

model='motor_position_pid';
baseDir=fileparts(mfilename('fullpath'));
outdir=fullfile(baseDir,'..','models');
if ~exist(outdir,'dir'),mkdir(outdir);end

if bdIsLoaded(model),close_system(model,0);end
new_system(model);
open_system(model);

add_block('simulink/Sources/Step',[model '/Position Setpoint deg'], ...
    'Time','0.5','Before','0','After','90','Position',[30 55 65 85]);
add_block('simulink/Math Operations/Sum',[model '/Error'], ...
    'Inputs','+-','Position',[110 52 135 88]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID Position'], ...
    'P','2','I','0','D','0.05','SampleTime','0.02','Position',[180 45 280 95]);
add_block('simulink/Discontinuities/Saturation',[model '/PWM Limit'], ...
    'UpperLimit','150','LowerLimit','-150','Position',[325 52 395 88]);

% Convert signed PWM count to an equivalent armature voltage for the
% conceptual 12 V motor model.
add_block('simulink/Math Operations/Gain',[model '/PWM to Voltage'], ...
    'Gain','12/255','Position',[435 52 510 88]);

% Same physical baseline as P3. Position is the integral of motor speed:
% Theta(s)/V(s) = 0.01 / (0.005 s^3 + 0.06 s^2 + 0.1001 s)
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Position rad'], ...
    'Numerator','0.01','Denominator','[0.005 0.06 0.1001 0]', ...
    'Position',[550 48 690 92]);
add_block('simulink/Math Operations/Gain',[model '/rad to deg'], ...
    'Gain','180/pi','Position',[730 52 800 88]);

add_block('simulink/Signal Routing/Mux',[model '/Mux'], ...
    'Inputs','2','Position',[850 45 855 105]);
add_block('simulink/Sinks/Scope',[model '/Scope'], ...
    'Position',[905 55 940 90]);

add_line(model,'Position Setpoint deg/1','Error/1');
add_line(model,'Error/1','PID Position/1');
add_line(model,'PID Position/1','PWM Limit/1');
add_line(model,'PWM Limit/1','PWM to Voltage/1');
add_line(model,'PWM to Voltage/1','DC Motor Position rad/1');
add_line(model,'DC Motor Position rad/1','rad to deg/1');
add_line(model,'rad to deg/1','Error/2','autorouting','on');
add_line(model,'Position Setpoint deg/1','Mux/1','autorouting','on');
add_line(model,'rad to deg/1','Mux/2');
add_line(model,'Mux/1','Scope/1');

set_param(model,'StopTime','10');
save_system(model,fullfile(outdir,[model '.slx']));
open_system(model);
fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

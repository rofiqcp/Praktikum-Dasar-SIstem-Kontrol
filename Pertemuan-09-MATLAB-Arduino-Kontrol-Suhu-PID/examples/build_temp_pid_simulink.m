clear; clc;

model='temp_pid_water_heater';
baseDir=fileparts(mfilename('fullpath'));
outdir=fullfile(baseDir,'..','models');
if ~exist(outdir,'dir'),mkdir(outdir);end

if bdIsLoaded(model),close_system(model,0);end
new_system(model);
open_system(model);

% Absolute temperature setpoint: ambient 25 degC -> target 45 degC.
add_block('simulink/Sources/Step',[model '/Setpoint'], ...
    'Time','10','Before','25','After','45','Position',[30 60 60 90]);
add_block('simulink/Math Operations/Sum',[model '/Error'], ...
    'Inputs','+-','Position',[105 58 130 92]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID'], ...
    'P','5','I','0.08','D','2','SampleTime','0.2','Position',[170 50 260 100]);
add_block('simulink/Discontinuities/Saturation',[model '/Output 0-100 pct'], ...
    'UpperLimit','100','LowerLimit','0','Position',[300 55 395 95]);

% P3 thermal plant uses G(s)=35/(120s+1) with normalized input 0..1.
% Convert controller percentage to per-unit before the plant.
add_block('simulink/Math Operations/Gain',[model '/Percent to pu'], ...
    'Gain','0.01','Position',[425 55 485 95]);
add_block('simulink/Continuous/Transfer Fcn',[model '/Temperature Rise Plant'], ...
    'Numerator','35','Denominator','[120 1]','Position',[525 55 655 95]);

% Plant output is temperature rise above ambient. Add 25 degC so the
% feedback variable has the same absolute-temperature meaning as SP/PV P9.
add_block('simulink/Sources/Constant',[model '/Ambient 25C'], ...
    'Value','25','Position',[525 135 575 165]);
add_block('simulink/Math Operations/Sum',[model '/Absolute Temperature'], ...
    'Inputs','++','Position',[700 58 730 112]);

add_block('simulink/Signal Routing/Mux',[model '/Mux'], ...
    'Inputs','2','Position',[780 48 785 112]);
add_block('simulink/Sinks/Scope',[model '/Scope'], ...
    'Position',[835 55 870 90]);

add_line(model,'Setpoint/1','Error/1');
add_line(model,'Error/1','PID/1');
add_line(model,'PID/1','Output 0-100 pct/1');
add_line(model,'Output 0-100 pct/1','Percent to pu/1');
add_line(model,'Percent to pu/1','Temperature Rise Plant/1');
add_line(model,'Temperature Rise Plant/1','Absolute Temperature/1');
add_line(model,'Ambient 25C/1','Absolute Temperature/2');
add_line(model,'Absolute Temperature/1','Error/2','autorouting','on');
add_line(model,'Setpoint/1','Mux/1','autorouting','on');
add_line(model,'Absolute Temperature/1','Mux/2');
add_line(model,'Mux/1','Scope/1');

set_param(model,'StopTime','700');
save_system(model,fullfile(outdir,[model '.slx']));
open_system(model);
fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

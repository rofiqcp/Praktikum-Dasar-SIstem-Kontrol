clear; clc;
model='temp_pid_water_heater'; outdir=fullfile('..','models'); if ~exist(outdir,'dir'),mkdir(outdir);end
if bdIsLoaded(model),close_system(model,0);end
new_system(model); open_system(model);
add_block('simulink/Sources/Step',[model '/Setpoint'],'Time','10','Before','25','After','50','Position',[30 60 60 90]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[105 58 130 92]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID'], ...
    'P','8','I','0.2','D','0','SampleTime','1','Position',[170 50 260 100]);
add_block('simulink/Discontinuities/Saturation',[model '/Duty 0-100'],'UpperLimit','100','LowerLimit','0','Position',[300 55 370 95]);
add_block('simulink/Continuous/Transfer Fcn',[model '/Water Heater'], ...
    'Numerator','0.8','Denominator','[120 1]','Position',[420 55 540 95]);
add_block('simulink/Signal Routing/Mux',[model '/Mux'],'Inputs','2','Position',[585 48 590 112]);
add_block('simulink/Sinks/Scope',[model '/Scope'],'Position',[640 55 675 90]);
add_line(model,'Setpoint/1','Error/1'); add_line(model,'Error/1','PID/1'); add_line(model,'PID/1','Duty 0-100/1'); add_line(model,'Duty 0-100/1','Water Heater/1'); add_line(model,'Water Heater/1','Error/2','autorouting','on');
add_line(model,'Setpoint/1','Mux/1','autorouting','on'); add_line(model,'Water Heater/1','Mux/2'); add_line(model,'Mux/1','Scope/1');
set_param(model,'StopTime','700'); save_system(model,fullfile(outdir,[model '.slx'])); open_system(model); fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

clear; clc;
model='motor_position_pid'; outdir=fullfile('..','models'); if ~exist(outdir,'dir'),mkdir(outdir);end
if bdIsLoaded(model),close_system(model,0);end
new_system(model); open_system(model);
add_block('simulink/Sources/Step',[model '/Position Setpoint'],'Time','0.5','Before','0','After','90','Position',[30 55 65 85]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[110 52 135 88]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID Position'],'P','2','I','0.1','D','0.05','SampleTime','0.05','Position',[180 45 280 95]);
add_block('simulink/Discontinuities/Saturation',[model '/PWM'],'UpperLimit','255','LowerLimit','-255','Position',[325 52 390 88]);
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Position'],'Numerator','0.1','Denominator','[0.01 0.14 0.41 0]','Position',[435 48 560 92]);
add_block('simulink/Signal Routing/Mux',[model '/Mux'],'Inputs','2','Position',[610 45 615 105]); add_block('simulink/Sinks/Scope',[model '/Scope'],'Position',[665 55 700 90]);
add_line(model,'Position Setpoint/1','Error/1'); add_line(model,'Error/1','PID Position/1'); add_line(model,'PID Position/1','PWM/1'); add_line(model,'PWM/1','DC Motor Position/1'); add_line(model,'DC Motor Position/1','Error/2','autorouting','on'); add_line(model,'Position Setpoint/1','Mux/1','autorouting','on'); add_line(model,'DC Motor Position/1','Mux/2'); add_line(model,'Mux/1','Scope/1');
set_param(model,'StopTime','10'); save_system(model,fullfile(outdir,[model '.slx'])); open_system(model); fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

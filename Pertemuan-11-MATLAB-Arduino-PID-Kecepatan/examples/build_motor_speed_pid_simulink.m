clear; clc;
model='motor_speed_pid'; outdir=fullfile('..','models'); if ~exist(outdir,'dir'),mkdir(outdir);end
if bdIsLoaded(model),close_system(model,0);end
new_system(model); open_system(model);
add_block('simulink/Sources/Step',[model '/RPM Setpoint'],'Time','0.5','Before','0','After','100','Position',[30 55 65 85]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[110 52 135 88]);
add_block('simulink/Discrete/Discrete PID Controller',[model '/PID Speed'],'P','1','I','0.5','D','0.01','SampleTime','0.05','Position',[180 45 275 95]);
add_block('simulink/Discontinuities/Saturation',[model '/PWM'],'UpperLimit','255','LowerLimit','-255','Position',[320 52 385 88]);
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Speed'],'Numerator','0.1','Denominator','[0.01 0.14 0.41]','Position',[430 48 550 92]);
add_block('simulink/Signal Routing/Mux',[model '/Mux'],'Inputs','2','Position',[600 45 605 105]); add_block('simulink/Sinks/Scope',[model '/Scope'],'Position',[655 55 690 90]);
add_line(model,'RPM Setpoint/1','Error/1'); add_line(model,'Error/1','PID Speed/1'); add_line(model,'PID Speed/1','PWM/1'); add_line(model,'PWM/1','DC Motor Speed/1'); add_line(model,'DC Motor Speed/1','Error/2','autorouting','on'); add_line(model,'RPM Setpoint/1','Mux/1','autorouting','on'); add_line(model,'DC Motor Speed/1','Mux/2'); add_line(model,'Mux/1','Scope/1');
set_param(model,'StopTime','10'); save_system(model,fullfile(outdir,[model '.slx'])); open_system(model); fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

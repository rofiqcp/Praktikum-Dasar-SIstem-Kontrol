clear; clc;
model='pid_manual_water_heater';
outdir=fullfile('..','models'); if ~exist(outdir,'dir'), mkdir(outdir); end
outfile=fullfile(outdir,[model '.slx']);
if bdIsLoaded(model), close_system(model,0); end
new_system(model); open_system(model);
% Parameters live in base workspace
assignin('base','Kp',2); assignin('base','Ki',0.03); assignin('base','Kd',8); assignin('base','Tf',2);
assignin('base','Kplant',0.8); assignin('base','tau',120);
add_block('simulink/Sources/Step',[model '/Setpoint'],'Time','0','Before','0','After','1','Position',[30 90 60 120]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[100 85 125 125]);
add_block('simulink/Signal Routing/Goto',[model '/ErrorGoto'],'GotoTag','e','Position',[155 105 205 125]);
add_block('simulink/Signal Routing/From',[model '/eP'],'GotoTag','e','Position',[240 35 280 55]);
add_block('simulink/Signal Routing/From',[model '/eI'],'GotoTag','e','Position',[240 90 280 110]);
add_block('simulink/Signal Routing/From',[model '/eD'],'GotoTag','e','Position',[240 145 280 165]);
add_block('simulink/Math Operations/Gain',[model '/P'],'Gain','Kp','Position',[315 25 370 65]);
add_block('simulink/Continuous/Integrator',[model '/Integrator'],'Position',[315 80 345 120]);
add_block('simulink/Math Operations/Gain',[model '/Ki'],'Gain','Ki','Position',[375 80 430 120]);
add_block('simulink/Continuous/Transfer Fcn',[model '/D_filter'],'Numerator','[Kd 0]','Denominator','[Tf 1]','Position',[315 140 410 175]);
add_block('simulink/Math Operations/Sum',[model '/PID_Sum'],'Inputs','+++','Position',[470 75 500 135]);
add_block('simulink/Discontinuities/Saturation',[model '/Saturation'],'UpperLimit','1','LowerLimit','0','Position',[540 85 590 125]);
add_block('simulink/Continuous/Transfer Fcn',[model '/WaterHeater'],'Numerator','Kplant','Denominator','[tau 1]','Position',[640 80 750 130]);
add_block('simulink/Sinks/Scope',[model '/Scope'],'NumInputPorts','2','Position',[820 60 850 130]);
add_line(model,'Setpoint/1','Error/1'); add_line(model,'Error/1','ErrorGoto/1');
add_line(model,'eP/1','P/1'); add_line(model,'eI/1','Integrator/1'); add_line(model,'Integrator/1','Ki/1'); add_line(model,'eD/1','D_filter/1');
add_line(model,'P/1','PID_Sum/1'); add_line(model,'Ki/1','PID_Sum/2'); add_line(model,'D_filter/1','PID_Sum/3');
add_line(model,'PID_Sum/1','Saturation/1'); add_line(model,'Saturation/1','WaterHeater/1'); add_line(model,'WaterHeater/1','Scope/1'); add_line(model,'Setpoint/1','Scope/2');
add_line(model,'WaterHeater/1','Error/2','autorouting','on');
set_param(model,'StopTime','600','Solver','ode45');
save_system(model,outfile); fprintf('Created %s\n',outfile);

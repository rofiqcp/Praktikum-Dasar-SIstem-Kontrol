clear; clc;
model='pid_manual_water_heater';
outdir=fullfile('..','models'); if ~exist(outdir,'dir'), mkdir(outdir); end
if bdIsLoaded(model), close_system(model,0); end
new_system(model);

Kp=0.20; Ki=0.005; Kd=0.50; Tf=1.0; Kplant=35; tau=120;
assignin('base','Kp',Kp); assignin('base','Ki',Ki); assignin('base','Kd',Kd);
assignin('base','Tf',Tf); assignin('base','Kplant',Kplant); assignin('base','tau',tau);

add_block('simulink/Sources/Step',[model '/SP'],'Time','0','After','1','Position',[25 95 55 125]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[90 90 120 130]);
add_block('simulink/Math Operations/Gain',[model '/P'],'Gain','Kp','Position',[180 25 230 55]);
add_block('simulink/Math Operations/Gain',[model '/Ki'],'Gain','Ki','Position',[180 85 230 115]);
add_block('simulink/Continuous/Integrator',[model '/I'],'Position',[270 85 300 115]);
add_block('simulink/Continuous/Transfer Fcn',[model '/D'],'Numerator','[Kd 0]','Denominator','[Tf 1]','Position',[180 145 270 180]);
add_block('simulink/Math Operations/Sum',[model '/PID'],'Inputs','+++','Position',[350 80 380 140]);
add_block('simulink/Continuous/Transfer Fcn',[model '/Plant'],'Numerator','Kplant','Denominator','[tau 1]','Position',[440 90 540 130]);
add_block('simulink/Sinks/Scope',[model '/Scope'],'NumInputPorts','2','Position',[610 75 640 135]);

add_line(model,'SP/1','Error/1');
add_line(model,'Error/1','P/1','autorouting','on');
add_line(model,'Error/1','Ki/1','autorouting','on');
add_line(model,'Ki/1','I/1');
add_line(model,'Error/1','D/1','autorouting','on');
add_line(model,'P/1','PID/1'); add_line(model,'I/1','PID/2'); add_line(model,'D/1','PID/3');
add_line(model,'PID/1','Plant/1'); add_line(model,'Plant/1','Scope/1'); add_line(model,'SP/1','Scope/2','autorouting','on');
add_line(model,'Plant/1','Error/2','autorouting','on');

set_param(model,'StopTime','600','Solver','ode45');
save_system(model,fullfile(outdir,[model '.slx']));
open_system(model);
fprintf('Created %s with Kp=%g Ki=%g Kd=%g\n',model,Kp,Ki,Kd);

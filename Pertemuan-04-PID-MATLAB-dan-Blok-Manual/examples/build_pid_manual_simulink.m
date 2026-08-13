model='pid_manual_water_heater';
if bdIsLoaded(model), close_system(model,0); end
new_system(model); open_system(model);
add_block('simulink/Sources/Step',[model '/SP'],'Position',[30 80 60 110]);
add_block('simulink/Math Operations/Sum',[model '/Error'],'Inputs','+-','Position',[100 80 125 115]);
add_block('simulink/Math Operations/Gain',[model '/Kp'],'Gain','2','Position',[170 30 230 60]);
add_block('simulink/Continuous/Integrator',[model '/Integral'],'Position',[165 90 195 120]);
add_block('simulink/Math Operations/Gain',[model '/Ki'],'Gain','0.05','Position',[220 90 280 120]);
add_block('simulink/Continuous/Transfer Fcn',[model '/D_Filter'],'Numerator','[5 0]','Denominator','[0.5 1]','Position',[170 145 280 180]);
add_block('simulink/Math Operations/Sum',[model '/PID_Sum'],'Inputs','+++','Position',[330 75 355 125]);
add_block('simulink/Discontinuities/Saturation',[model '/Actuator'],'UpperLimit','100','LowerLimit','0','Position',[400 80 455 120]);
add_block('simulink/Continuous/Transfer Fcn',[model '/WaterHeater'],'Numerator','0.8','Denominator','[45 1]','Position',[510 80 615 120]);
add_block('simulink/Sinks/Scope',[model '/Scope'],'Position',[680 75 710 105]);
add_line(model,'SP/1','Error/1'); add_line(model,'Error/1','Kp/1'); add_line(model,'Error/1','Integral/1'); add_line(model,'Integral/1','Ki/1'); add_line(model,'Error/1','D_Filter/1');
add_line(model,'Kp/1','PID_Sum/1'); add_line(model,'Ki/1','PID_Sum/2'); add_line(model,'D_Filter/1','PID_Sum/3'); add_line(model,'PID_Sum/1','Actuator/1'); add_line(model,'Actuator/1','WaterHeater/1'); add_line(model,'WaterHeater/1','Scope/1'); add_line(model,'WaterHeater/1','Error/2','autorouting','on');
set_param([model '/SP'],'Time','0','Before','0','After','60'); set_param(model,'StopTime','200'); save_system(model); open_system(model);

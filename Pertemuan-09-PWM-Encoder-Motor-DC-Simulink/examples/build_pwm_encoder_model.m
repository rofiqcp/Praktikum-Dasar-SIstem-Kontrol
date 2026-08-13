model='p09_pwm_encoder_skeleton'; if bdIsLoaded(model),close_system(model,0);end; new_system(model);open_system(model);
add_block('simulink/Sources/Slider Gain',[model '/PWM_Command'],'Gain','1','Position',[40 50 110 90]);
add_block('simulink/Discontinuities/Saturation',[model '/Limit'],'UpperLimit','255','LowerLimit','-255','Position',[160 50 215 90]);
add_block('simulink/Sinks/Display',[model '/Command_Display'],'Position',[280 50 340 85]);
add_line(model,'PWM_Command/1','Limit/1');add_line(model,'Limit/1','Command_Display/1');
add_block('simulink/Ports & Subsystems/Subsystem',[model '/Arduino_PWM_CW_CCW'],'Position',[400 35 540 105]);
add_block('simulink/Ports & Subsystems/Subsystem',[model '/Encoder_AB_Read'],'Position',[400 150 540 220]);
set_param(model,'StopTime','inf');save_system(model); open_system(model);
disp('Tambahkan block Arduino PWM pin 5/6 dan encoder sesuai support package versi MATLAB Anda.');

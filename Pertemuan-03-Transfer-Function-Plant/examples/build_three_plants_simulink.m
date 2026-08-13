clear; clc;
model='three_control_plants';
outdir=fullfile('..','models'); if ~exist(outdir,'dir'), mkdir(outdir); end
if bdIsLoaded(model), close_system(model,0); end
new_system(model);

add_block('simulink/Sources/Step',[model '/Step'],'Position',[25 145 55 175]);
add_block('simulink/Continuous/Transfer Fcn',[model '/Water Heater'], ...
    'Numerator','35','Denominator','[120 1]','Position',[130 35 250 75]);
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Speed'], ...
    'Numerator','0.01','Denominator','[0.005 0.06 0.1001]','Position',[130 130 250 170]);
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Position'], ...
    'Numerator','0.01','Denominator','[0.005 0.06 0.1001 0]','Position',[130 225 250 265]);

for k=1:3
    add_block('simulink/Sinks/Scope',[model sprintf('/Scope%d',k)], ...
        'Position',[335 35+95*(k-1) 365 65+95*(k-1)]);
end
add_line(model,'Step/1','Water Heater/1','autorouting','on');
add_line(model,'Step/1','DC Motor Speed/1','autorouting','on');
add_line(model,'Step/1','DC Motor Position/1','autorouting','on');
add_line(model,'Water Heater/1','Scope1/1');
add_line(model,'DC Motor Speed/1','Scope2/1');
add_line(model,'DC Motor Position/1','Scope3/1');
set_param(model,'StopTime','600');
save_system(model,fullfile(outdir,[model '.slx']));
open_system(model);
fprintf('Created %s\n',fullfile(outdir,[model '.slx']));

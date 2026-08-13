clear; clc;
model = 'three_control_plants';
outdir = fullfile('..','models'); if ~exist(outdir,'dir'), mkdir(outdir); end
if bdIsLoaded(model), close_system(model,0); end
new_system(model); open_system(model);

% Input step shared by three example plants.
add_block('simulink/Sources/Step',[model '/Step'],'Position',[30 155 60 185]);

% Water heater: K/(tau*s+1), delay discussed separately in Materi.md.
add_block('simulink/Continuous/Transfer Fcn',[model '/Water Heater'], ...
    'Numerator','0.8','Denominator','[120 1]','Position',[130 40 260 80]);
% DC motor speed example.
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Speed'], ...
    'Numerator','0.1','Denominator','[0.01 0.14 0.41]','Position',[130 135 260 175]);
% DC motor position = speed plant * 1/s.
add_block('simulink/Continuous/Transfer Fcn',[model '/DC Motor Position'], ...
    'Numerator','0.1','Denominator','[0.01 0.14 0.41 0]','Position',[130 230 260 270]);

for k=1:3
    add_block('simulink/Sinks/Scope',[model sprintf('/Scope%d',k)], ...
        'Position',[350 35+95*(k-1) 380 65+95*(k-1)]);
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

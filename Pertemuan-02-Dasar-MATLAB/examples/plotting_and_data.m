clear; clc; close all;

outdir = 'output';
if ~exist(outdir,'dir'); mkdir(outdir); end

time_s = (0:1:20)';
setpoint = 50*ones(size(time_s));
pv = 25 + 27*(1-exp(-time_s/6));
error_value = setpoint - pv;

T = table(time_s,setpoint,pv,error_value, ...
    'VariableNames',{'time_s','setpoint','pv','error'});
writetable(T,fullfile(outdir,'p02_sample_data.csv'));

figure('Name','P02 Plotting and Data');
tiledlayout(2,1);
nexttile;
plot(time_s,setpoint,'--','LineWidth',1.2); hold on;
plot(time_s,pv,'LineWidth',1.5); grid on;
xlabel('Time (s)'); ylabel('Value');
legend('Setpoint','PV','Location','best');
title('Setpoint dan process variable');
nexttile;
plot(time_s,error_value,'LineWidth',1.5); grid on;
xlabel('Time (s)'); ylabel('Error'); title('Error terhadap waktu');

exportgraphics(gcf,fullfile(outdir,'p02_plotting_result.png'),'Resolution',150);
fprintf('CSV dan PNG tersimpan di folder %s\n',outdir);

%% P10 - Offline encoder math demonstration
clear; clc; close all;

CPR=600;
dt=0.05;
count=[0 5 15 30 45 50 45 35 20 5 0]';
time_s=(0:numel(count)-1)'*dt;
position_deg=count/CPR*360;
delta_count=[0;diff(count)];
rpm=delta_count/CPR*60/dt;

T=table(time_s,count,position_deg,delta_count,rpm);
disp(T);
fprintf('RPM resolution per count at dt=%.3f s and CPR=%.1f: %.4f RPM/count\n',dt,CPR,60/(CPR*dt));

figure('Color','w');
tiledlayout(2,1);
nexttile; plot(time_s,position_deg,'o-');grid on;ylabel('Position (deg)');
nexttile; stairs(time_s,rpm,'LineWidth',1.1);grid on;ylabel('RPM');xlabel('Time (s)');

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(T,fullfile(outDir,'encoder_math_offline.csv'));
exportgraphics(gcf,fullfile(outDir,'encoder_math_offline.png'),'Resolution',180);

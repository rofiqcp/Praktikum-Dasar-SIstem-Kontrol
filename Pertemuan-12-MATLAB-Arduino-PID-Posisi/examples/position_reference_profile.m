%% P12 offline reference profile for analysis and plotting
clear; clc; close all;
t=[0 2 6 10 14 18]';
position_reference_deg=[0 90 -90 45 0 0]';
T=table(t,position_reference_deg,'VariableNames',{'time_s','reference_deg'});
disp(T);
figure('Color','w');stairs(t,position_reference_deg,'LineWidth',1.2);grid on;xlabel('Time (s)');ylabel('Reference (deg)');title('P12 Position Reference Profile');
outDir=fullfile(fileparts(mfilename('fullpath')),'output');if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(T,fullfile(outDir,'position_reference_profile.csv'));exportgraphics(gcf,fullfile(outDir,'position_reference_profile.png'),'Resolution',180);

%% P11 - Offline signed speed setpoint profile generator
clear; clc; close all;

t=(0:0.05:20)';
sp=zeros(size(t));
sp(t>=2 & t<7)=120;
sp(t>=9 & t<14)=-120;
sp(t>=16 & t<19)=60;

T=table(t,sp,'VariableNames',{'time_s','sp_rpm'});
outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(T,fullfile(outDir,'speed_profile.csv'));

figure('Color','w');
stairs(t,sp,'LineWidth',1.3);grid on;
xlabel('Time (s)');ylabel('SP (RPM)');title('P11 signed speed reference profile');
exportgraphics(gcf,fullfile(outDir,'speed_profile.png'),'Resolution',180);

fprintf('Profile segments: 0 -> +120 -> 0 -> -120 -> 0 -> +60 -> 0 RPM\n');
fprintf('Analyze each step segment separately when computing response metrics.\n');

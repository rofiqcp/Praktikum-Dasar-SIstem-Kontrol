%% P11 - Offline analysis of speed PID telemetry CSV
clear; clc; close all;
baseDir=fileparts(mfilename('fullpath')); file=fullfile(baseDir,'output','speed_pid.csv');
if ~isfile(file),error('Missing %s. Copy a compatible telemetry CSV into examples/output.',file);end
T=readtable(file);
req={'time_s','sp_rpm','rpm','error','P','I','D','pid_pwm','count'};
assert(all(ismember(req,T.Properties.VariableNames)),'Unexpected CSV columns.');
dt=diff(T.time_s); maxU=max(abs(T.pid_pwm));
fprintf('Samples: %d\n',height(T));
if ~isempty(dt),fprintf('dt min/median/max: %.6f / %.6f / %.6f s\n',min(dt),median(dt),max(dt));end
fprintf('RPM range: %.3f .. %.3f\n',min(T.rpm),max(T.rpm));
fprintf('Max |control|: %.3f\n',maxU);
fprintf('Positive RPM samples: %d\n',nnz(T.rpm>0));
fprintf('Negative RPM samples: %d\n',nnz(T.rpm<0));
figure('Color','w');tiledlayout(3,1);
nexttile;plot(T.time_s,T.sp_rpm,'--',T.time_s,T.rpm,'LineWidth',1.0);grid on;ylabel('RPM');legend('SP','RPM');
nexttile;plot(T.time_s,T.error);grid on;ylabel('Error');
nexttile;plot(T.time_s,T.P,T.time_s,T.I,T.time_s,T.D,T.time_s,T.pid_pwm);grid on;xlabel('Time (s)');ylabel('Terms');legend('P','I','D','control');
outDir=fullfile(baseDir,'output');exportgraphics(gcf,fullfile(outDir,'speed_pid_analysis.png'),'Resolution',180);
summary=table(height(T),min(T.rpm),max(T.rpm),maxU,'VariableNames',{'samples','rpm_min','rpm_max','max_abs_control'});writetable(summary,fullfile(outDir,'speed_pid_analysis_summary.csv'));

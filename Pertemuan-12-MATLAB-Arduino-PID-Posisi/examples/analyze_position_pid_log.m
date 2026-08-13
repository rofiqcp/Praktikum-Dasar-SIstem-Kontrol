%% P12 - Offline analysis of position PID telemetry CSV
clear; clc; close all;
baseDir=fileparts(mfilename('fullpath')); file=fullfile(baseDir,'output','position_pid.csv');
if ~isfile(file),error('Missing %s. Copy a compatible telemetry CSV into examples/output.',file);end
T=readtable(file);
req={'time_s','sp_deg','position_deg','error','P','I','D','pid_pwm','count'};
assert(all(ismember(req,T.Properties.VariableNames)),'Unexpected CSV columns.');
dt=diff(T.time_s); finalError=T.error(end); maxU=max(abs(T.pid_pwm));
fprintf('Samples: %d\n',height(T));
if ~isempty(dt),fprintf('dt min/median/max: %.6f / %.6f / %.6f s\n',min(dt),median(dt),max(dt));end
fprintf('Position range: %.3f .. %.3f deg\n',min(T.position_deg),max(T.position_deg));
fprintf('Final error: %.3f deg\n',finalError);
fprintf('Max |control|: %.3f\n',maxU);
figure('Color','w');tiledlayout(3,1);
nexttile;plot(T.time_s,T.sp_deg,'--',T.time_s,T.position_deg,'LineWidth',1.0);grid on;ylabel('deg');legend('SP','Position');
nexttile;plot(T.time_s,T.error);grid on;ylabel('Error (deg)');
nexttile;plot(T.time_s,T.P,T.time_s,T.I,T.time_s,T.D,T.time_s,T.pid_pwm);grid on;xlabel('Time (s)');ylabel('Terms');legend('P','I','D','control');
outDir=fullfile(baseDir,'output');exportgraphics(gcf,fullfile(outDir,'position_pid_analysis.png'),'Resolution',180);
summary=table(height(T),min(T.position_deg),max(T.position_deg),finalError,maxU,'VariableNames',{'samples','position_min','position_max','final_error','max_abs_control'});writetable(summary,fullfile(outDir,'position_pid_analysis_summary.csv'));

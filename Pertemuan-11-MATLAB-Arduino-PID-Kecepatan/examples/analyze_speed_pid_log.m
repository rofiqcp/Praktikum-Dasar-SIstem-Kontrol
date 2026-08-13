%% P11 - Offline analysis of speed PID telemetry CSV
clear; clc; close all;

baseDir=fileparts(mfilename('fullpath'));
file=fullfile(baseDir,'output','speed_pid.csv');
if ~isfile(file)
    error('Missing %s. Run the P11 logger first or copy a compatible CSV into examples/output.',file);
end

T=readtable(file);
req={'time_s','sp_rpm','rpm','error','P','I','D','pid_pwm','count'};
assert(all(ismember(req,T.Properties.VariableNames)),'Unexpected CSV columns.');
assert(height(T)>=3,'Speed PID log must contain at least three samples.');

numericNames=req;
for k=1:numel(numericNames)
    values=T.(numericNames{k});
    assert(all(isfinite(values)),'%s contains NaN or Inf.',numericNames{k});
end

dt=diff(T.time_s);
assert(all(dt>0),'time_s must be strictly increasing.');

maxU=max(abs(T.pid_pwm));
if maxU>0
    saturationThreshold=0.98*maxU;
    saturationPct=100*nnz(abs(T.pid_pwm)>=saturationThreshold)/height(T);
else
    saturationThreshold=0;
    saturationPct=0;
end

fprintf('Samples: %d\n',height(T));
fprintf('dt min/median/max: %.6f / %.6f / %.6f s\n',min(dt),median(dt),max(dt));
fprintf('RPM range: %.3f .. %.3f\n',min(T.rpm),max(T.rpm));
fprintf('Max |control|: %.3f\n',maxU);
fprintf('Samples near observed output limit: %.2f %%\n',saturationPct);
fprintf('Positive RPM samples: %d\n',nnz(T.rpm>0));
fprintf('Negative RPM samples: %d\n',nnz(T.rpm<0));

figure('Color','w');
tiledlayout(4,1);
nexttile;
plot(T.time_s,T.sp_rpm,'--',T.time_s,T.rpm,'LineWidth',1.0);
grid on;ylabel('RPM');legend('SP','RPM');
nexttile;
plot(T.time_s,T.error);grid on;ylabel('Error');
nexttile;
plot(T.time_s,T.P,T.time_s,T.I,T.time_s,T.D);
grid on;ylabel('PID terms');legend('P','I','D');
nexttile;
plot(T.time_s,T.pid_pwm);grid on;xlabel('Time (s)');ylabel('Control');

outDir=fullfile(baseDir,'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
exportgraphics(gcf,fullfile(outDir,'speed_pid_analysis.png'),'Resolution',180);
summary=table(height(T),min(dt),median(dt),max(dt),min(T.rpm),max(T.rpm),maxU,saturationPct, ...
    'VariableNames',{'samples','dt_min','dt_median','dt_max','rpm_min','rpm_max','max_abs_control','near_limit_pct'});
writetable(summary,fullfile(outDir,'speed_pid_analysis_summary.csv'));

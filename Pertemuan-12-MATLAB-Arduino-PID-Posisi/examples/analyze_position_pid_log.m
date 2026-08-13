%% P12 - Offline analysis of position PID telemetry CSV
clear; clc; close all;

baseDir=fileparts(mfilename('fullpath'));
file=fullfile(baseDir,'output','position_pid.csv');
if ~isfile(file)
    error('Missing %s. Run the P12 logger first or copy a compatible CSV into examples/output.',file);
end

T=readtable(file);
req={'time_s','sp_deg','position_deg','error','P','I','D','pid_pwm','count'};
assert(all(ismember(req,T.Properties.VariableNames)),'Unexpected CSV columns.');
assert(height(T)>=3,'Position PID log must contain at least three samples.');

for k=1:numel(req)
    values=T.(req{k});
    assert(all(isfinite(values)),'%s contains NaN or Inf.',req{k});
end

dt=diff(T.time_s);
assert(all(dt>0),'time_s must be strictly increasing.');

finalError=T.error(end);
maxU=max(abs(T.pid_pwm));
countRange=max(T.count)-min(T.count);

fprintf('Samples: %d\n',height(T));
fprintf('dt min/median/max: %.6f / %.6f / %.6f s\n',min(dt),median(dt),max(dt));
fprintf('Position range: %.3f .. %.3f deg\n',min(T.position_deg),max(T.position_deg));
fprintf('Count range: %g counts\n',countRange);
fprintf('Final error: %.3f deg\n',finalError);
fprintf('Max |control|: %.3f\n',maxU);
fprintf('Positive target samples: %d\n',nnz(T.sp_deg>0));
fprintf('Negative target samples: %d\n',nnz(T.sp_deg<0));

figure('Color','w');
tiledlayout(4,1);
nexttile;
plot(T.time_s,T.sp_deg,'--',T.time_s,T.position_deg,'LineWidth',1.0);
grid on;ylabel('deg');legend('SP','Position');
nexttile;
plot(T.time_s,T.error);grid on;ylabel('Error (deg)');
nexttile;
plot(T.time_s,T.P,T.time_s,T.I,T.time_s,T.D);
grid on;ylabel('PID terms');legend('P','I','D');
nexttile;
plot(T.time_s,T.pid_pwm);grid on;xlabel('Time (s)');ylabel('Control');

outDir=fullfile(baseDir,'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
exportgraphics(gcf,fullfile(outDir,'position_pid_analysis.png'),'Resolution',180);
summary=table(height(T),min(dt),median(dt),max(dt),min(T.position_deg),max(T.position_deg), ...
    finalError,maxU,countRange,nnz(T.sp_deg>0),nnz(T.sp_deg<0), ...
    'VariableNames',{'samples','dt_min','dt_median','dt_max','position_min','position_max', ...
    'final_error','max_abs_control','count_range','positive_sp_samples','negative_sp_samples'});
writetable(summary,fullfile(outDir,'position_pid_analysis_summary.csv'));

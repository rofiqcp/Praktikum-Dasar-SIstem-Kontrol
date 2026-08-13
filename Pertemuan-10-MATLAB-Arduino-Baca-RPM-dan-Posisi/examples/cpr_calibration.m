%% P10 - Estimate counts per revolution from repeated measurements
clear; clc;

% Replace these example values with measured data.
revolutions = [5 5 5 5 5]';
start_count = [0 0 0 0 0]';
end_count   = [3002 2998 3001 3000 2999]';

assert(numel(revolutions)==numel(start_count) && numel(start_count)==numel(end_count), ...
    'revolutions, start_count, and end_count must have the same length.');
assert(~isempty(revolutions),'Calibration data must not be empty.');
assert(all(isfinite(revolutions)) && all(isfinite(start_count)) && all(isfinite(end_count)), ...
    'Calibration data contains NaN or Inf.');
assert(all(revolutions>0),'Revolutions must be positive.');

delta_count=end_count-start_count;
assert(all(delta_count~=0),'Every calibration trial must contain a non-zero count change.');
cpr_est=abs(delta_count)./revolutions;

T=table(revolutions,start_count,end_count,delta_count,cpr_est);
disp(T);
fprintf('Mean CPR   = %.4f\n',mean(cpr_est));
fprintf('Median CPR = %.4f\n',median(cpr_est));
fprintf('Std CPR    = %.4f\n',std(cpr_est));
fprintf('Range CPR  = %.4f\n',range(cpr_est));
if mean(cpr_est)>0
    fprintf('CV CPR     = %.4f %%\n',100*std(cpr_est)/mean(cpr_est));
end

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(T,fullfile(outDir,'cpr_calibration.csv'));

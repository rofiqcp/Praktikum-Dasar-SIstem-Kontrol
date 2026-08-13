%% P10 - Estimate counts per revolution from repeated measurements
clear; clc;

% Replace with your measured values.
revolutions = [5 5 5 5 5]';
start_count = [0 0 0 0 0]';
end_count   = [3002 2998 3001 3000 2999]';

assert(all(revolutions>0),'Revolutions must be positive.');
delta_count=end_count-start_count;
cpr_est=abs(delta_count)./revolutions;

T=table(revolutions,start_count,end_count,delta_count,cpr_est);
disp(T);
fprintf('Mean CPR   = %.4f\n',mean(cpr_est));
fprintf('Median CPR = %.4f\n',median(cpr_est));
fprintf('Std CPR    = %.4f\n',std(cpr_est));
fprintf('Range CPR  = %.4f\n',range(cpr_est));

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(T,fullfile(outDir,'cpr_calibration.csv'));

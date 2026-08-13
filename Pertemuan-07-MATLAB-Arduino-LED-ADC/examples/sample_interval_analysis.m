clear; clc;
T = readtable('adc_log.csv');
if ~ismember('time_s', T.Properties.VariableNames)
    error('adc_log.csv must contain time_s');
end
dt = diff(T.time_s);
fprintf('samples = %d\n', height(T));
fprintf('duration = %.3f s\n', T.time_s(end)-T.time_s(1));
fprintf('dt min = %.6f s\n', min(dt));
fprintf('dt median = %.6f s\n', median(dt));
fprintf('dt max = %.6f s\n', max(dt));
figure; histogram(dt); grid on;
xlabel('Sample interval (s)'); ylabel('Count');
title('P7 Sample Interval Distribution');

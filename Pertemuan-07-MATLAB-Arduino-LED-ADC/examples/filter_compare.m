clear; clc; close all;
T=readtable('adc_log.csv');
if ~ismember('A0_V',T.Properties.VariableNames), error('adc_log.csv must contain A0_V'); end
T.A0_MA5=movmean(T.A0_V,5);
figure; plot(T.time_s,T.A0_V,label='Raw'); hold on; plot(T.time_s,T.A0_MA5,label='MA5'); grid on; legend;
xlabel('Time (s)'); ylabel('A0 (V)'); title('Raw vs Moving Average');
writetable(T,'adc_log_filtered.csv');

clear; clc; close all;
file=fullfile('..','templates','template_pengamatan.csv');
T=readtable(file);
valid=~isnan(T.temperature_C); T=T(valid,:);
if height(T)<3, error('Isi template dengan minimal 3 data temperatur.'); end
figure; plot(T.time_s,T.temperature_C,'o-'); hold on; plot(T.time_s,T.setpoint_C,'--'); grid on;
xlabel('Time (s)'); ylabel('Temperature (C)'); legend('PV','SV');
target=median(T.setpoint_C(end-max(1,round(height(T)*0.1)):end));
y0=T.temperature_C(1); A=target-y0;
peak=max(T.temperature_C); overshoot=max(0,(peak-target)/max(abs(A),eps)*100);
ess=target-mean(T.temperature_C(max(1,end-2):end));
fprintf('Overshoot = %.2f %%\nSteady-state error = %.3f C\n',overshoot,ess);

clear; clc; close all;
file=fullfile('..','sample_data','daq_export.csv'); T=readtable(file);
% Map these names if your DAQMaster export uses different headers.
t=T.time_s; pv=T.PV_C; sv=T.SV_C;
figure; plot(t,pv,'LineWidth',1.4); hold on; plot(t,sv,'--'); grid on;
xlabel('Time (s)'); ylabel('Temperature (C)'); legend('PV','SV');
if ismember('MV_pct',T.Properties.VariableNames)
    yyaxis right; plot(t,T.MV_pct,':'); ylabel('MV (%)');
end
% basic metrics
sp=median(sv(end-max(1,round(numel(sv)*.1)):end)); y0=pv(1); A=sp-y0;
[peak,ip]=max(pv); os=max(0,(peak-sp)/max(abs(A),eps)*100);
ess=sp-mean(pv(end-max(2,round(numel(pv)*.1)):end));
fprintf('Peak time %.1f s, Overshoot %.2f%%, Ess %.3f C\n',t(ip)-t(1),os,ess);

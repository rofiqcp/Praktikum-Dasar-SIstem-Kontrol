clear; clc;
a=arduino();
writeDigitalPin(a,'D13',1); pause(0.5); writeDigitalPin(a,'D13',0);
T=20; t0=tic; t=[]; v=[];
figure;
while toc(t0)<T
    tk=toc(t0); vk=readVoltage(a,'A0');
    t(end+1,1)=tk; v(end+1,1)=vk; %#ok<SAGROW>
    plot(t,v); grid on; xlabel('Time (s)'); ylabel('A0 (V)'); drawnow limitrate;
    pause(0.05);
end
writetable(table(t,v,'VariableNames',{'time_s','A0_V'}),'adc_log.csv');

clear; clc; close all;
a=arduino();
SSR='D8'; SP=50; Kp=6; Ki=0.08; Kd=8; Ts=0.2; window=2.0;
TEMP_OFFSET=0; TEMP_SCALE_PER_V=20; TEMP_MAX=70; % replace from calibration
I=0; eprev=0; t0=tic; windowStart=0; log=[];
writeDigitalPin(a,SSR,0); cleanup=onCleanup(@()writeDigitalPin(a,SSR,0));
while toc(t0)<600
    loopStart=tic; t=toc(t0); V=readVoltage(a,'A0'); T=TEMP_OFFSET+TEMP_SCALE_PER_V*V;
    if ~isfinite(T) || T<0 || T>TEMP_MAX, error('Temperature invalid/over limit'); end
    e=SP-T; P=Kp*e; D=Kd*(e-eprev)/Ts; trial=P+I+D; u=min(max(trial,0),100);
    if ~((u>=100 && e>0)||(u<=0 && e<0)), I=I+Ki*e*Ts; end
    I=min(max(I,0),100); u=min(max(P+I+D,0),100); eprev=e;
    if t-windowStart>=window, windowStart=t; end
    ssrOn=(t-windowStart) < window*(u/100); writeDigitalPin(a,SSR,ssrOn);
    log(end+1,:)=[t,T,SP,e,P,I,D,u,ssrOn]; %#ok<SAGROW>
    fprintf('t=%6.1f T=%5.2f u=%5.1f%%\n',t,T,u);
    pause(max(0,Ts-toc(loopStart)));
end
writeDigitalPin(a,SSR,0);
Tlog=array2table(log,'VariableNames',{'time_s','temp_C','sp_C','error','P','I','D','PID_pct','SSR'});
writetable(Tlog,'temperature_pid_log.csv');
figure; plot(Tlog.time_s,Tlog.temp_C); hold on; plot(Tlog.time_s,Tlog.sp_C,'--'); grid on;

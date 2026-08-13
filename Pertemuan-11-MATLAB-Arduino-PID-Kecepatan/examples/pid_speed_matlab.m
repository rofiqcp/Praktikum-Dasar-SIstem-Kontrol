clear; clc; close all;
port="COM5"; s=serialport(port,115200); configureTerminator(s,"LF"); flush(s);
SP=120; Kp=0.8; Ki=0.5; Kd=0.01; I=0; eprev=0; lastT=[]; log=[];
writeline(s,"Z"); cleanup=onCleanup(@()writeline(s,"STOP")); t0=tic;
while toc(t0)<20
 line=strtrim(readline(s)); q=split(line,',');
 if numel(q)~=4 || q(1)~="T", continue; end
 t=str2double(q(2))/1000; rpm=str2double(q(4));
 if isempty(lastT), lastT=t; eprev=SP-rpm; continue; end
 dt=max(t-lastT,1e-3); lastT=t; e=SP-rpm; P=Kp*e; D=Kd*(e-eprev)/dt;
 trial=P+I+D; u=max(min(trial,255),-255);
 if ~((u>=255&&e>0)||(u<=-255&&e<0)), I=I+Ki*e*dt; end
 I=max(min(I,255),-255); u=round(max(min(P+I+D,255),-255)); eprev=e;
 writeline(s,"M,"+string(u)); log(end+1,:)=[t,SP,rpm,e,P,I,D,u]; %#ok<SAGROW>
end
writeline(s,"STOP"); T=array2table(log,'VariableNames',{'time_s','sp_rpm','rpm','error','P','I','D','PID'}); writetable(T,'pid_speed.csv');
figure; tiledlayout(2,1); nexttile; plot(T.time_s,T.sp_rpm,'--',T.time_s,T.rpm); grid on; legend('SP','RPM'); nexttile; plot(T.time_s,T.P,T.time_s,T.I,T.time_s,T.D,T.time_s,T.PID); grid on; legend('P','I','D','PID');

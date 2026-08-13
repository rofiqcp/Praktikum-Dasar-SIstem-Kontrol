clear; clc; close all;
port="COM5"; s=serialport(port,115200); configureTerminator(s,"LF"); flush(s);
PPR=600; SPdeg=90; SP=SPdeg/360*PPR; Kp=1.2; Ki=0.02; Kd=0.08; I=0; eprev=0; lastT=[]; log=[];
writeline(s,"Z"); cleanup=onCleanup(@()writeline(s,"STOP")); t0=tic;
while toc(t0)<15
 line=strtrim(readline(s)); q=split(line,','); if numel(q)~=4||q(1)~="T",continue;end
 t=str2double(q(2))/1000; c=str2double(q(3)); rpm=str2double(q(4));
 if isempty(lastT),lastT=t;eprev=SP-c;continue;end
 dt=max(t-lastT,1e-3);lastT=t;e=SP-c;P=Kp*e;D=Kd*(e-eprev)/dt;trial=P+I+D;u=max(min(trial,255),-255);
 if ~((u>=255&&e>0)||(u<=-255&&e<0)),I=I+Ki*e*dt;end;I=max(min(I,255),-255);u=round(max(min(P+I+D,255),-255));
 if abs(e)<1.0,u=0;end; eprev=e; writeline(s,"M,"+string(u)); posdeg=c/PPR*360; log(end+1,:)=[t,SPdeg,posdeg,rpm,e,P,I,D,u]; %#ok<SAGROW>
end
writeline(s,"STOP"); T=array2table(log,'VariableNames',{'time_s','sp_deg','pos_deg','rpm','error_count','P','I','D','PID'});writetable(T,'pid_position.csv');
figure;plot(T.time_s,T.sp_deg,'--',T.time_s,T.pos_deg);grid on;legend('SP','Position');

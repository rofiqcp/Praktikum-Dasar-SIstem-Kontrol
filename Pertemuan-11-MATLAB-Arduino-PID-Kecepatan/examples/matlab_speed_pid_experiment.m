%% P11 - MATLAB supervisor/logger for Arduino speed PID
clear;clc;close all;PORT="COM5";BAUD=115200;DURATION=45;SP=120;KP=.5;KI=.20;KD=0;MAXPWM=180;
s=serialport(PORT,BAUD,'Timeout',1);configureTerminator(s,"LF");flush(s);cleanup=onCleanup(@() safeStop(s)); %#ok<NASGU>
send(s,"KP",KP);send(s,"KI",KI);send(s,"KD",KD);send(s,"MAXPWM",MAXPWM);send(s,"SP",SP);send(s,"RUN",1);
rows=[];experiment=tic;lastPing=0;while toc(experiment)<DURATION,elapsed=toc(experiment);if elapsed-lastPing>.5,send(s,"PING",1);lastPing=elapsed;end;if s.NumBytesAvailable>0,line=strtrim(readline(s));if startsWith(line,"#"),fprintf('%s\n',line);continue;end;v=str2double(split(line,","));if numel(v)==9&&all(isfinite(v)),rows(end+1,:)=v.';end,end;pause(.005);end
send(s,"RUN",0);if isempty(rows),error('No telemetry');end;t=(rows(:,1)-rows(1,1))/1000;T=array2table([t rows(:,2:end)],'VariableNames',{'time_s','sp_rpm','rpm','error','P','I','D','pid_pwm','count'});
figure('Color','w');subplot(2,1,1);plot(t,T.sp_rpm,'--',t,T.rpm,'LineWidth',1.2);grid on;ylabel('RPM');legend('SP','RPM');subplot(2,1,2);plot(t,T.P,t,T.I,t,T.D,t,T.pid_pwm);grid on;xlabel('Time (s)');legend('P','I','D','PID');
outDir=fullfile(fileparts(mfilename('fullpath')),'output');if ~exist(outDir,'dir'),mkdir(outDir);end;writetable(T,fullfile(outDir,'speed_pid.csv'));exportgraphics(gcf,fullfile(outDir,'speed_pid.png'),'Resolution',180);repo=fileparts(fileparts(fileparts(mfilename('fullpath'))));addpath(fullfile(repo,'shared','matlab'));M=response_metrics(T.time_s,T.rpm,T.sp_rpm);disp(M);writetable(struct2table(M),fullfile(outDir,'metrics.csv'));
function send(s,k,v),writeline(s,k+","+string(v));end
function safeStop(s),try,writeline(s,"RUN,0");catch,end,end

%% P9 - MATLAB host PID controlling Arduino Mega heater/SSR
clear; clc; close all;

PORT = ""; SP = 45.0; KP = 5.0; KI = 0.08; KD = 2.0;
TS = 0.20; WINDOW_S = 2.0; MAX_TEMP_C = 60.0; RUN_TIME_S = 300;

if strlength(PORT)==0, a=arduino(); else, a=arduino(PORT,'Mega2560'); end
SSR='D8'; TEMP='A0'; writeDigitalPin(a,SSR,0);
cleanup=onCleanup(@() writeDigitalPin(a,SSR,0)); %#ok<NASGU>

n=ceil(RUN_TIME_S/TS);data=nan(n,9);integral=0;prevPV=nan;windowStart=tic;experiment=tic;
for k=1:n
 loopStart=tic;now=toc(experiment);voltage=readVoltage(a,TEMP);pv=voltage*100.0;
 if ~isfinite(pv) || pv < -5 || pv > MAX_TEMP_C,writeDigitalPin(a,SSR,0);error('Temperature fault: %.3f C',pv);end
 e=SP-pv;P=KP*e;if isnan(prevPV),D=0;else,D=-KD*(pv-prevPV)/TS;end
 candidateI=integral+KI*e*TS;rawCandidate=P+candidateI+D;high=rawCandidate>100;low=rawCandidate<0;
 if (~high && ~low) || (high && e<0) || (low && e>0),integral=candidateI;end
 I=integral;u=min(max(P+I+D,0),100);elapsedWindow=toc(windowStart);
 if elapsedWindow>=WINDOW_S,windowStart=tic;elapsedWindow=0;end
 ssr=elapsedWindow<(u/100)*WINDOW_S;writeDigitalPin(a,SSR,ssr);
 data(k,:)=[now,pv,SP,e,P,I,D,u,double(ssr)];prevPV=pv;pause(max(0,TS-toc(loopStart)));
end
writeDigitalPin(a,SSR,0);data=data(all(isfinite(data(:,1:2)),2),:);
T=array2table(data,'VariableNames',{'time_s','temp_C','sp_C','error','P','I','D','pid_pct','ssr'});
outDir=fullfile(fileparts(mfilename('fullpath')),'output');if ~exist(outDir,'dir'),mkdir(outDir);end
stamp=char(datetime('now','Format','yyyyMMdd_HHmmss'));writetable(T,fullfile(outDir,['temp_' stamp '.csv']));
repo=fileparts(fileparts(fileparts(mfilename('fullpath'))));addpath(fullfile(repo,'shared','matlab'));
M=response_metrics(T.time_s,T.temp_C,T.sp_C);disp(M);writetable(struct2table(M),fullfile(outDir,['metrics_' stamp '.csv']));
save_response_plot(T.time_s,T.sp_C,T.temp_C,fullfile(outDir,['temp_' stamp '.png']),'P9 MATLAB-Arduino Temperature PID');

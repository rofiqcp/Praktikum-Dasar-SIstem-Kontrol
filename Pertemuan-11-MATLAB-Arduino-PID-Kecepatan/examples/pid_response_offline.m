%% P11 - Offline PID response exercise
clear; clc; close all;
Ts=0.05; t=(0:Ts:12)'; ref=zeros(size(t)); ref(t>=1 & t<5)=1; ref(t>=7 & t<11)=-1;
Kp=1.2; Ki=0.8; Kd=0.02; limit=1.0; tau=0.4;
y=zeros(size(t)); u=zeros(size(t)); integ=0; prevY=0;
for k=2:numel(t)
 e=ref(k-1)-y(k-1); P=Kp*e; D=-Kd*(y(k-1)-prevY)/Ts;
 candI=integ+Ki*e*Ts; cand=P+candI+D; hi=cand>limit; lo=cand<-limit;
 if (~hi&&~lo)||(hi&&e<0)||(lo&&e>0), integ=candI; end
 u(k)=min(max(P+integ+D,-limit),limit); prevY=y(k-1);
 y(k)=y(k-1)+Ts*(u(k)-y(k-1))/tau;
end
figure('Color','w');tiledlayout(2,1);nexttile;plot(t,ref,'--',t,y,'LineWidth',1.1);grid on;legend('reference','response');nexttile;plot(t,u);grid on;xlabel('Time (s)');ylabel('control');
outDir=fullfile(fileparts(mfilename('fullpath')),'output');if ~exist(outDir,'dir'),mkdir(outDir);end
T=table(t,ref,y,u,'VariableNames',{'time_s','reference','response','control'});writetable(T,fullfile(outDir,'pid_response_offline.csv'));exportgraphics(gcf,fullfile(outDir,'pid_response_offline.png'),'Resolution',180);

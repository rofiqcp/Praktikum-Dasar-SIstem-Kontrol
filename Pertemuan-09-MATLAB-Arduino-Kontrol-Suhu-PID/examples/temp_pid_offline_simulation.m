%% P09 - Offline discrete PID simulation for a first-order thermal plant
clear; clc; close all;

Ts=0.2; T_end=500; t=(0:Ts:T_end)';
SP=45; Tamb=25; Kplant=35; tau=120;
configs=[5 0 0; 5 0.08 0; 5 0.08 2; 12 0.10 1];
names={'P','PI','PID','Aggressive'};

figure('Color','w'); hold on;
summary=table('Size',[0 7], ...
    'VariableTypes',{'string','double','double','double','double','double','double'}, ...
    'VariableNames',{'Mode','Kp','Ki','Kd','FinalPV','FinalError','MaxOutput'});

for r=1:size(configs,1)
    Kp=configs(r,1); Ki=configs(r,2); Kd=configs(r,3);
    pv=zeros(size(t)); pv(1)=Tamb; u=zeros(size(t));
    integral=0; prevPV=pv(1);
    for k=2:numel(t)
        e=SP-pv(k-1);
        P=Kp*e;
        D=-Kd*(pv(k-1)-prevPV)/Ts;
        candidateI=integral+Ki*e*Ts;
        candidate=P+candidateI+D;
        high=candidate>100; low=candidate<0;
        if (~high && ~low) || (high && e<0) || (low && e>0)
            integral=candidateI;
        end
        u(k)=min(max(P+integral+D,0),100);
        prevPV=pv(k-1);
        target=Tamb+Kplant*(u(k)/100);
        pv(k)=pv(k-1)+Ts*(target-pv(k-1))/tau;
    end
    plot(t,pv,'DisplayName',names{r},'LineWidth',1.1);
    summary(end+1,:)={string(names{r}),Kp,Ki,Kd,pv(end),SP-pv(end),max(u)}; %#ok<SAGROW>
end

yline(SP,'--','DisplayName','SP'); grid on;
xlabel('Time (s)'); ylabel('Temperature (degC)');
title('P09 Offline Temperature PID Comparison'); legend('Location','best');
disp(summary);

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
writetable(summary,fullfile(outDir,'temp_pid_offline_summary.csv'));
exportgraphics(gcf,fullfile(outDir,'temp_pid_offline.png'),'Resolution',180);

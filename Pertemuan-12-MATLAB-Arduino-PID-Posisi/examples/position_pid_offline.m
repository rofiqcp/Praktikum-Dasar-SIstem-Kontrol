%% P12 - Offline position PID simulation using the P3 DC-motor equations
clear; clc; close all;

Ts=0.02;
t=(0:Ts:10)';
sp_deg=zeros(size(t));
sp_deg(t>=0.5)=90;

% Same physical baseline used in P3.
J=0.01;
b=0.1;
Kt=0.01;
Ke=0.01;
R=1.0;
L=0.5;
Vbus=12.0;

% P12 baseline controller values.
Kp=2.0;
Ki=0.0;
Kd=0.05;
MAXPWM=150.0;

current_A=zeros(size(t));
omega_rad_s=zeros(size(t));
theta_rad=zeros(size(t));
position_deg=zeros(size(t));
error_deg=zeros(size(t));
Pterm=zeros(size(t));
Iterm=zeros(size(t));
Dterm=zeros(size(t));
pwm=zeros(size(t));
voltage_V=zeros(size(t));

integral=0;
prev_position_deg=0;

for k=2:numel(t)
    pv=position_deg(k-1);
    e=sp_deg(k-1)-pv;
    P=Kp*e;
    D=-Kd*(pv-prev_position_deg)/Ts;

    candidateI=integral+Ki*e*Ts;
    candidate=P+candidateI+D;
    high=candidate>MAXPWM;
    low=candidate<-MAXPWM;
    if (~high && ~low) || (high && e<0) || (low && e>0)
        integral=candidateI;
    end

    u=min(max(P+integral+D,-MAXPWM),MAXPWM);
    v=(u/255.0)*Vbus;

    di=(v-R*current_A(k-1)-Ke*omega_rad_s(k-1))/L;
    domega=(Kt*current_A(k-1)-b*omega_rad_s(k-1))/J;

    current_A(k)=current_A(k-1)+Ts*di;
    omega_rad_s(k)=omega_rad_s(k-1)+Ts*domega;
    theta_rad(k)=theta_rad(k-1)+Ts*omega_rad_s(k);
    position_deg(k)=theta_rad(k)*180/pi;

    error_deg(k)=e;
    Pterm(k)=P;
    Iterm(k)=integral;
    Dterm(k)=D;
    pwm(k)=u;
    voltage_V(k)=v;
    prev_position_deg=pv;
end

error_deg(1)=sp_deg(1)-position_deg(1);

figure('Color','w');
tiledlayout(3,1);
nexttile;
plot(t,sp_deg,'--',t,position_deg,'LineWidth',1.1);
grid on;ylabel('Position (deg)');legend('SP','Position');
nexttile;
plot(t,error_deg);grid on;ylabel('Error (deg)');
nexttile;
plot(t,Pterm,t,Iterm,t,Dterm,t,pwm,'LineWidth',1.0);
grid on;xlabel('Time (s)');ylabel('Controller');legend('P','I','D','PWM');

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
T=table(t,sp_deg,position_deg,error_deg,Pterm,Iterm,Dterm,pwm,voltage_V,current_A,omega_rad_s, ...
    'VariableNames',{'time_s','sp_deg','position_deg','error_deg','P','I','D','pwm','voltage_V','current_A','omega_rad_s'});
writetable(T,fullfile(outDir,'position_pid_offline.csv'));
exportgraphics(gcf,fullfile(outDir,'position_pid_offline.png'),'Resolution',180);

repo=fileparts(fileparts(fileparts(mfilename('fullpath'))));
addpath(fullfile(repo,'shared','matlab'));
M=response_metrics(t,position_deg,sp_deg);
disp(M);
writetable(struct2table(M),fullfile(outDir,'position_pid_offline_metrics.csv'));

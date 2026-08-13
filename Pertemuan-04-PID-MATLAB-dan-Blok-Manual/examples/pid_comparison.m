clear; clc; close all; s=tf('s');
G=35/(120*s+1);
controllers={pid(0.20,0,0),pid(0.20,0.005,0),pid(0.20,0.005,0.5)};
names={'P','PI','PID'};
figure; hold on;
for i=1:numel(controllers)
    C=controllers{i};
    T=feedback(C*G,1);
    [y,t]=step(T,600);
    plot(t,y,'LineWidth',1.5,'DisplayName',names{i});
    info=stepinfo(y,t,1);
    ess=abs(1-dcgain(T));
    fprintf('%s: Kp=%.4f Ki=%.4f Kd=%.4f | rise=%.3f settle=%.3f OS=%.2f%% ess=%.5f\n', ...
        names{i},C.Kp,C.Ki,C.Kd,info.RiseTime,info.SettlingTime,info.Overshoot,ess);
end
yline(1,'--','SP'); grid on; legend('Location','best');
xlabel('Time (s)'); ylabel('Output'); title('P, PI, PID comparison');

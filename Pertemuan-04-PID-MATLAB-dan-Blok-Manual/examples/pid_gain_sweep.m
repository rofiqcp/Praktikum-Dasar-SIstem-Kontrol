clear; clc; close all; s=tf('s');
G=35/(120*s+1);
KpList=[0.05 0.10 0.20 0.40];
figure('Name','P04 Gain Sweep'); hold on;
for i=1:length(KpList)
    Kp=KpList(i);
    T=feedback(pid(Kp,0,0)*G,1);
    [y,t]=step(T,600);
    plot(t,y,'LineWidth',1.3,'DisplayName',sprintf('Kp=%.2f',Kp));
    info=stepinfo(y,t,1);
    fprintf('Kp=%.2f | rise=%.2f settle=%.2f overshoot=%.2f%% ess=%.4f\n', ...
        Kp,info.RiseTime,info.SettlingTime,info.Overshoot,abs(1-dcgain(T)));
end
yline(1,'--','SP'); grid on; legend('Location','best');
xlabel('Time (s)'); ylabel('Output'); title('Kp sweep');

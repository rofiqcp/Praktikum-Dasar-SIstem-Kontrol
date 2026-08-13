clear; clc; close all;
s = tf('s');

Kth = 35;
tauList = [60 120 240];
figure('Name','P03 Thermal Parameter Sweep'); hold on;
for i = 1:length(tauList)
    G = Kth/(tauList(i)*s+1);
    step(G,600);
end
grid on; title('Pengaruh time constant');
legend('tau=60 s','tau=120 s','tau=240 s','Location','best');

R=1; L=0.5; b=0.1; Kt=0.01; Ke=0.01;
JList=[0.005 0.01 0.02];
figure('Name','P03 Mechanical Parameter Sweep'); hold on;
for i=1:length(JList)
    J=JList(i);
    G=Kt/((L*s+R)*(J*s+b)+Ke*Kt);
    step(G,5);
end
grid on; title('Pengaruh inertia J pada plant kecepatan');
legend('J=0.005','J=0.01','J=0.02','Location','best');

fprintf('Parameter sweep selesai.\n');

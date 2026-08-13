clear; clc; close all;

Ts = 0.05;
t = 0:Ts:20;
u = ones(size(t));

cases = [1 2; 1 5; 2 5]; % [K tau]
labels = {'K=1 tau=2','K=1 tau=5','K=2 tau=5'};

figure('Name','P02 First Order Euler'); hold on;
for c = 1:size(cases,1)
    K = cases(c,1);
    tau = cases(c,2);
    y = zeros(size(t));
    for k = 2:length(t)
        dydt = (-y(k-1) + K*u(k-1))/tau;
        y(k) = y(k-1) + Ts*dydt;
    end
    plot(t,y,'LineWidth',1.5,'DisplayName',labels{c});
    fprintf('%s -> y akhir = %.4f\n',labels{c},y(end));
end

grid on; xlabel('Time (s)'); ylabel('Output');
title('Simulasi orde satu dengan integrasi Euler');
legend('Location','best');

outdir = 'output';
if ~exist(outdir,'dir'); mkdir(outdir); end
exportgraphics(gcf,fullfile(outdir,'first_order_euler.png'),'Resolution',150);

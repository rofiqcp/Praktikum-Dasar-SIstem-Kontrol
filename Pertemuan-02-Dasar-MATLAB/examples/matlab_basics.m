clear; clc; close all;
Ts=0.01; t=(0:Ts:10)';
x=sin(2*pi*1*t)+0.15*randn(size(t));
window=20; xma=movmean(x,window);
figure; plot(t,x); hold on; plot(t,xma,'LineWidth',1.2); grid on;
xlabel('Time (s)'); ylabel('Amplitude'); legend('raw','moving average');
A=[1 2;3 5]; disp(det(A)); disp(inv(A));
xs=saturate(x,-1,1);
T=table(t,x,xma,xs,'VariableNames',{'time_s','raw','moving_average','saturated'});
writetable(T,'matlab_basics_output.csv');

% first-order plant discrete
K=1; tau=1.5; u=ones(size(t)); y=zeros(size(t));
for k=2:numel(t)
    y(k)=y(k-1)+Ts/tau*(-y(k-1)+K*u(k));
end
figure; plot(t,y); grid on; xlabel('Time (s)'); ylabel('y'); title('First-order step response');

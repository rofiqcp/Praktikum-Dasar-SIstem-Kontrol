clear; clc; close all; s=tf('s'); G=0.8/(45*s+1);
controllers={2, 2+0.05/s, 2+0.05/s+5*s/(0.5*s+1)};
names={'P','PI','PID filtered-D'};
figure; hold on; grid on;
for i=1:numel(controllers)
    T=feedback(controllers{i}*G,1); [y,t]=step(T,200); plot(t,60*y,'DisplayName',names{i});
    fprintf('\n%s\n',names{i}); disp(stepinfo(y,t,1));
end
xlabel('s'); ylabel('Scaled output'); legend;

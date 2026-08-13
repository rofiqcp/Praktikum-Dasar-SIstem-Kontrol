clear; clc; close all; s=tf('s');
G=0.8/(120*s+1);
controllers={pid(2,0,0), pid(2,0.03,0), pid(2,0.03,8)};
names={'P','PI','PID'};
figure; hold on;
for i=1:numel(controllers)
    T=feedback(controllers{i}*G,1);
    [y,t]=step(T,600); plot(t,y,'DisplayName',names{i});
    fprintf('%s\n',names{i}); disp(stepinfo(y,t,1));
end
grid on; legend; xlabel('s'); ylabel('normalized temperature');

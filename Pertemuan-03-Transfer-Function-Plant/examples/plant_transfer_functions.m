clear; clc; close all; s=tf('s');
% Water heater first-order model
KT=0.8; tauT=45; Gt=KT/(tauT*s+1);
% DC motor parameters
J=0.01; b=0.1; K=0.01; R=1; L=0.5;
Gw=K/((J*s+b)*(L*s+R)+K^2);
Gtheta=Gw/s;
plants={Gt,Gw,Gtheta}; names={'Water heater','DC motor speed','DC motor position'};
for i=1:3
    figure(i); step(plants{i}); grid on; title(names{i}); disp(names{i}); disp(stepinfo(plants{i}));
end

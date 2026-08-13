clear; clc; close all; s=tf('s');
%% Water heater FOPDT example (replace after identification)
Kth=0.8; tau=120; Ld=8;
Gth0=Kth/(tau*s+1);
[numD,denD]=pade(Ld,1); Gdelay=tf(numD,denD);
Gth=Gth0*Gdelay;
figure; step(Gth,700); grid on; title('Water heater FOPDT (Pade delay)');
disp('Water heater poles'); disp(pole(Gth));
%% DC motor speed
R=2; La=0.5; Km=0.1; J=0.02; b=0.2;
Gspeed=Km/((J*s+b)*(La*s+R)+Km^2);
figure; step(Gspeed,5); grid on; title('DC motor speed');
disp(stepinfo(Gspeed));
%% DC motor position
Gpos=Gspeed/s;
figure; step(Gpos,5); grid on; title('DC motor position (open-loop voltage to angle)');
%% Save variables
save('plant_models.mat','Gth','Gspeed','Gpos');

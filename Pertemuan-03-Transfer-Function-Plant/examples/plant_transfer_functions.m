clear; clc; close all;
s = tf('s');

%% Plant 1: water heater (temperature rise / normalized input)
Kth = 35;          % degC / p.u.
tau_th = 120;     % s
Gth = Kth/(tau_th*s + 1);

fprintf('=== Water heater ===\n');
disp(Gth);
disp('Poles:'); disp(pole(Gth));
fprintf('DC gain = %.4f\n',dcgain(Gth));
disp(stepinfo(Gth));
figure('Name','P03 Water Heater');
step(Gth,600); grid on; title('Water heater - first order model');

%% Plant 2: DC motor speed
J = 0.01;          % kg.m^2
b = 0.1;           % N.m.s
Kt = 0.01;         % N.m/A
Ke = 0.01;         % V.s/rad
R = 1;             % ohm
L = 0.5;           % H
Gspeed = Kt/((L*s + R)*(J*s + b) + Ke*Kt);

fprintf('\n=== DC motor speed ===\n');
disp(Gspeed);
disp('Poles:'); disp(pole(Gspeed));
fprintf('DC gain = %.6f\n',dcgain(Gspeed));
disp(stepinfo(Gspeed));
figure('Name','P03 Motor Speed');
step(Gspeed,5); grid on; title('DC motor speed model');

%% Plant 3: DC motor position
Gpos = Gspeed/s;
fprintf('\n=== DC motor position ===\n');
disp(Gpos);
disp('Poles:'); disp(pole(Gpos));
figure('Name','P03 Motor Position');
step(Gpos,5); grid on; title('DC motor position - open loop');

%% Optional FOPDT extension for heater
heater_dead_time_s = 8;
[numDelay,denDelay] = pade(heater_dead_time_s,1);
Gth_fopdt = Gth*tf(numDelay,denDelay);

%% Save for P4 and other scripts
save('plant_models.mat','Gth','Gth_fopdt','Gspeed','Gpos', ...
    'Kth','tau_th','J','b','Kt','Ke','R','L');
fprintf('\nSaved plant_models.mat\n');

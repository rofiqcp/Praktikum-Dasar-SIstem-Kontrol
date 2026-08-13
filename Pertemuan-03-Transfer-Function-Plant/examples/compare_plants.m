clear; clc; close all;
thisDir = fileparts(mfilename('fullpath'));
run(fullfile(thisDir,'plant_transfer_functions.m'));

fprintf('\n=== Ringkasan model ===\n');
fprintf('Heater DC gain : %.4f\n',dcgain(Gth));
fprintf('Speed DC gain  : %.4f\n',dcgain(Gspeed));
fprintf('Position memiliki integrator sehingga interpretasi DC gain berbeda.\n');

disp('Pole heater:'); disp(pole(Gth));
disp('Pole speed:'); disp(pole(Gspeed));
disp('Pole position:'); disp(pole(Gpos));

figure('Name','P03 Step Responses');
tiledlayout(3,1);
nexttile; step(Gth,600); grid on; title('Water heater');
nexttile; step(Gspeed,5); grid on; title('DC motor speed');
nexttile; step(Gpos,5); grid on; title('DC motor position');

figure('Name','P03 Frequency Comparison');
bodemag(Gth,Gspeed,Gpos); grid on;
legend('heater','speed','position','Location','best');

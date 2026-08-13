%% P09 - Temperature sensor linear calibration
clear; clc; close all;

% Replace these values with laboratory measurements.
voltage_V   = [0.25 0.35 0.45 0.55 0.65]';
reference_C = [25.1 35.0 44.8 55.2 65.0]';

assert(numel(voltage_V)==numel(reference_C) && numel(voltage_V)>=3, ...
    'Need at least three calibration points.');

p = polyfit(voltage_V,reference_C,1);
predicted_C = polyval(p,voltage_V);
residual_C = reference_C-predicted_C;
rmse_C = sqrt(mean(residual_C.^2));

fprintf('Calibration: T = %.6f*V + %.6f\n',p(1),p(2));
fprintf('RMSE = %.4f degC\n',rmse_C);

T = table(voltage_V,reference_C,predicted_C,residual_C);
disp(T);

figure('Color','w');
plot(voltage_V,reference_C,'o','DisplayName','Reference'); hold on;
vq=linspace(min(voltage_V),max(voltage_V),100)';
plot(vq,polyval(p,vq),'-','DisplayName','Linear fit');
grid on; xlabel('Voltage (V)'); ylabel('Temperature (degC)');
legend('Location','best'); title('P09 Temperature Sensor Calibration');

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'), mkdir(outDir); end
writetable(T,fullfile(outDir,'temperature_calibration.csv'));
exportgraphics(gcf,fullfile(outDir,'temperature_calibration.png'),'Resolution',180);
save(fullfile(outDir,'temperature_calibration.mat'),'p','rmse_C');

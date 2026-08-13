%% P09 - Temperature sensor linear calibration
clear; clc; close all;

% Replace these values with laboratory measurements.
voltage_V   = [0.25 0.35 0.45 0.55 0.65]';
reference_C = [25.1 35.0 44.8 55.2 65.0]';

assert(numel(voltage_V)==numel(reference_C) && numel(voltage_V)>=3, ...
    'Need at least three paired calibration points.');
assert(all(isfinite(voltage_V)) && all(isfinite(reference_C)), ...
    'Calibration data contains NaN or Inf.');
assert(range(voltage_V)>0,'Calibration voltages must contain more than one distinct value.');

p = polyfit(voltage_V,reference_C,1);
predicted_C = polyval(p,voltage_V);
residual_C = reference_C-predicted_C;
rmse_C = sqrt(mean(residual_C.^2));
max_abs_residual_C=max(abs(residual_C));

fprintf('Calibration: T = %.6f*V + %.6f\n',p(1),p(2));
fprintf('Voltage range     = %.4f .. %.4f V\n',min(voltage_V),max(voltage_V));
fprintf('Reference range   = %.4f .. %.4f degC\n',min(reference_C),max(reference_C));
fprintf('RMSE              = %.4f degC\n',rmse_C);
fprintf('Max abs residual  = %.4f degC\n',max_abs_residual_C);

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
summary=table(p(1),p(2),rmse_C,max_abs_residual_C,min(voltage_V),max(voltage_V), ...
    min(reference_C),max(reference_C), ...
    'VariableNames',{'slope_degC_per_V','offset_degC','rmse_degC','max_abs_residual_degC', ...
    'voltage_min_V','voltage_max_V','reference_min_degC','reference_max_degC'});
writetable(summary,fullfile(outDir,'temperature_calibration_summary.csv'));
exportgraphics(gcf,fullfile(outDir,'temperature_calibration.png'),'Resolution',180);
save(fullfile(outDir,'temperature_calibration.mat'),'p','rmse_C','max_abs_residual_C');

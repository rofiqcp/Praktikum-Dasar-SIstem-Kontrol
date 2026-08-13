% Put multiple DAQ CSV files in a folder named runs and compare PV curves.
clear; close all; files=dir(fullfile('runs','*.csv')); figure; hold on;
for k=1:numel(files)
 T=readtable(fullfile(files(k).folder,files(k).name));
 plot(T.time_s,T.PV_C,'DisplayName',files(k).name);
end
grid on; legend('Interpreter','none'); xlabel('s'); ylabel('C');

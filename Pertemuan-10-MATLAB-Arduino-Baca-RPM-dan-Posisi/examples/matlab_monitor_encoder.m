%% P10 - MATLAB serial monitor for encoder stream
clear; clc; close all;
PORT="COM5"; BAUD=115200; DURATION=30;

s=serialport(PORT,BAUD,'Timeout',1);
configureTerminator(s,"LF"); flush(s);

rows=[];
tic;
while toc < DURATION
    if s.NumBytesAvailable>0
        line=strtrim(readline(s));
        if startsWith(line,"#"), fprintf('%s\n',line); continue; end
        v=str2double(split(line,","));
        if numel(v)==6 && all(isfinite(v))
            rows(end+1,:)=v.'; %#ok<AGROW>
        end
    end
    pause(0.005);
end

clear s
if isempty(rows),error('No telemetry received');end
t=(rows(:,1)-rows(1,1))/1000;

figure('Color','w');
subplot(2,1,1);
plot(t,rows(:,3),'LineWidth',1.2);grid on;ylabel('Position (deg)');
subplot(2,1,2);
plot(t,rows(:,4),t,rows(:,5),t,rows(:,6),'LineWidth',1.0);
grid on;xlabel('Time (s)');ylabel('RPM');legend('raw','MA','LPF');

outDir=fullfile(fileparts(mfilename('fullpath')),'output');
if ~exist(outDir,'dir'),mkdir(outDir);end
T=array2table([t rows(:,2:end)],'VariableNames', ...
 {'time_s','count','position_deg','rpm_raw','rpm_ma','rpm_lpf'});
writetable(T,fullfile(outDir,'encoder.csv'));
exportgraphics(gcf,fullfile(outDir,'encoder.png'),'Resolution',180);

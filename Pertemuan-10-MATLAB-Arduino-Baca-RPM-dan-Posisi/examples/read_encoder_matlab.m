clear; clc; close all;
port="COM5"; s=serialport(port,115200); configureTerminator(s,"LF"); flush(s);
PPR=600; t=[]; count=[]; rpm=[]; angle=[]; t0=tic;
writeline(s,"Z"); writeline(s,"M,80"); cleanup=onCleanup(@()writeline(s,"STOP"));
while toc(t0)<10
    line=strtrim(readline(s)); parts=split(line,',');
    if numel(parts)==4 && parts(1)=="T"
        ms=str2double(parts(2)); c=str2double(parts(3)); r=str2double(parts(4));
        t(end+1,1)=ms/1000; count(end+1,1)=c; rpm(end+1,1)=r; angle(end+1,1)=c/PPR*360; %#ok<SAGROW>
    end
end
writeline(s,"STOP"); T=table(t,count,angle,rpm); writetable(T,'encoder_log.csv');
figure; tiledlayout(2,1); nexttile; plot(t,rpm); grid on; ylabel('RPM'); nexttile; plot(t,angle); grid on; ylabel('deg'); xlabel('s');

%% P11 compatibility entry point
% The official P11 workflow uses matlab_speed_pid_experiment.m together
% with arduino_speed_pid/arduino_speed_pid.ino.  This file is kept only so
% older course links continue to work without introducing a second serial
% protocol or a second PID implementation.
run(fullfile(fileparts(mfilename('fullpath')),'matlab_speed_pid_experiment.m'));

%% Compatibility entry point for P12
% The maintained P12 workflow uses arduino_position_pid.ino together with
% matlab_position_pid_experiment.m. This file is kept so old links still work
% without introducing a second, incompatible serial protocol.
baseDir=fileparts(mfilename('fullpath'));
run(fullfile(baseDir,'matlab_position_pid_experiment.m'));

%% P11 simulation entry point
% Keep this wrapper path-independent so it can be called from the module
% directory, the repository root, or build scripts.
baseDir=fileparts(mfilename('fullpath'));
run(fullfile(baseDir,'pid_response_offline.m'));

% Example only for a conditioned 0-5V transmitter.
% Set offset/scale from your actual sensor calibration.
a=arduino(); offset_C=0; scale_C_per_V=20;
for k=1:100
    V=readVoltage(a,'A0'); T=offset_C+scale_C_per_V*V;
    fprintf('V=%.3f, T=%.2f C\n',V,T); pause(0.1);
end

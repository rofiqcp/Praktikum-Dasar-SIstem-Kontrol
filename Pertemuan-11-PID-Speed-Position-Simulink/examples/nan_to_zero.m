function y = nan_to_zero(u)
%#codegen
if isnan(u), y=0; else, y=u; end
end

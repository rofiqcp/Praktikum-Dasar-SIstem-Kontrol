function y=saturate(x,lo,hi)
%SATURATE Limit x between lo and hi.
y=min(max(x,lo),hi);
end

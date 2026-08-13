function M = response_metrics(t, y, sp)
%RESPONSE_METRICS Basic step-response metrics for measured lab data.
% t  : time [s]
% y  : process value
% sp : scalar or vector setpoint

t = t(:); y = y(:);
if isscalar(sp), sp = repmat(sp,size(y)); else, sp = sp(:); end
assert(numel(t)==numel(y) && numel(y)==numel(sp),'Input length mismatch');

ok = isfinite(t) & isfinite(y) & isfinite(sp);
t=t(ok); y=y(ok); sp=sp(ok);
t=t-t(1);

nTail=max(3,round(0.10*numel(y)));
y0=mean(y(1:min(3,end)));
spf=mean(sp(end-nTail+1:end));
yss=mean(y(end-nTail+1:end));
delta=spf-y0;
amp=abs(delta);

M.initial_value=y0;
M.final_setpoint=spf;
M.final_value=yss;
M.delay_time_s=NaN;
M.rise_time_s=NaN;
M.peak_time_s=NaN;
M.settling_time_s=NaN;
M.maximum_overshoot_pct=NaN;
M.steady_state_error=spf-yss;

if amp < eps, return; end
sgn=sign(delta); if sgn==0, sgn=1; end

cross = @(level) localCross(t,y,level,sgn);
t10=cross(y0+0.10*delta);
t50=cross(y0+0.50*delta);
t90=cross(y0+0.90*delta);
M.delay_time_s=t50;
if isfinite(t10) && isfinite(t90), M.rise_time_s=t90-t10; end

if sgn>0, [peak,idx]=max(y); else, [peak,idx]=min(y); end
M.peak_time_s=t(idx);
M.maximum_overshoot_pct=max(0,sgn*(peak-spf)/amp*100);

band=max(0.02*amp,eps);
inside=abs(y-spf)<=band;
for k=1:numel(inside)
    if all(inside(k:end))
        M.settling_time_s=t(k);
        break
    end
end
end

function tc = localCross(t,y,level,sgn)
if sgn>0, idx=find(y>=level,1,'first'); else, idx=find(y<=level,1,'first'); end
if isempty(idx), tc=NaN; else, tc=t(idx); end
end

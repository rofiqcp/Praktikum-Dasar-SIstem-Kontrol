clear; clc; close all;
t = linspace(0,10,1001);
f = 0.5;
y = sin(2*pi*f*t);
A = [1 2; 3 4]; B = [2; 1]; x = A\B;
fprintf('Solusi A*x=B: x1=%.3f x2=%.3f\n',x(1),x(2));
figure; plot(t,y,'LineWidth',1.2); grid on; xlabel('t (s)'); ylabel('sin(2\pi f t)'); title('Dasar Plot MATLAB');

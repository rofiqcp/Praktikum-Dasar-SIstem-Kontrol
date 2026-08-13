clear;clc;Ts=0.05;Kp=1.0;Ki=0.5;Kd=0.02;N=20;
C=pid(Kp,Ki,Kd,1/N,Ts); disp(C);
% Example discrete plant approximation for speed
Gd=c2d(tf(1,[0.2 1]),Ts,'zoh'); T=feedback(C*Gd,1); step(T,5);grid on;title('Reference discrete PID response');

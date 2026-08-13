clear;clc;close all;s=tf('s'); Gw=5/(0.25*s+1); Gp=Gw/s;
Cs=pid(0.8,2.0,0.01); Cp=pid(2.0,0.2,0.05);
figure;step(feedback(Cs*Gw,1),5);grid on;title('PID Speed Reference Model');
figure;step(feedback(Cp*Gp,1),8);grid on;title('PID Position Reference Model');

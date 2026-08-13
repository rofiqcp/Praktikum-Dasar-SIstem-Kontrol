clear; clc;
x1 = 0.5; y1 = 10;
x2 = 4.5; y2 = 90;
m = (y2-y1)/(x2-x1);
b = y1-m*x1;
fprintf('y = %.6f*x + %.6f\n',m,b);

clear; clc; close all;

Ts = 0.1;
t = 0:Ts:10;
data = 20 + 5*sin(2*pi*0.2*t);

fprintf('Jumlah sampel : %d\n',length(data));
fprintf('Mean          : %.3f\n',mean(data));
fprintf('Minimum       : %.3f\n',min(data));
[maxValue,maxIndex] = max(data);
fprintf('Maximum       : %.3f pada indeks %d\n',maxValue,maxIndex);

selected = data(data > mean(data));
fprintf('Jumlah data di atas mean: %d\n',length(selected));

A = [2 1;1 3];
b = [5;7];
x = A\b;
disp('Solusi A*x=b:');
disp(x);

disp('Verifikasi A*x:');
disp(A*x);

figure('Name','P02 Vector Matrix Lab');
plot(t,data,'LineWidth',1.5); grid on;
xlabel('Time (s)'); ylabel('Value');
title('Vector, indexing, dan statistik dasar');

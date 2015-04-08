intervals = load('intervals.csv');



data = load('noise.csv'); % test data, noisy intervals

delta = data - intervals;

sum_delta = sum(abs(delta), 2)

A = intervals(:,1);
B = intervals(:,2);
C = intervals(:,3);

D = data(:,1);
E = data(:,2);
F = data(:,3);

G = delta(:,1);
H = delta(:,2);
I = delta(:,3);

%ternplot(data(:,1), data(:,2), data(:,3), 'scatter')
%ternplot(D, E, F, 'scatter')

%terncontour(A, B, sum_delta);
%ternpcolor(A,B,C,sum_delta);

ternvelocity(A, B, C, D, E, F);
ternlabel('Interval 1', 'Interval 2', 'Interval 3');
title('Error quiver plot');
legend('Original intervals', 'Performance', 'Error');

'hallo'
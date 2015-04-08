intervals = load('intervals.csv');


data = load('noise.csv'); % test data, noisy intervals

% Difference performance/original
delta = data - intervals;

%Length of these error vectors
length_delta = sqrt(sum(abs(delta).^2,2))

% Original
A = intervals(:,1);
B = intervals(:,2);
C = intervals(:,3);

% Performance
D = data(:,1);
E = data(:,2);
F = data(:,3);


%ternpcolor(A,B,C,length_delta);
%terncontour(A,B,length_delta);

set(0,'DefaultTextFontSize',16)
ternlabel('Interval 1', 'Interval 2', 'Interval 3');

%ternplot(A, B, C, 'scatter', 'filled', 'k')
%ternplot(D, E, F, 'scatter', 'filled', 'r')

ternvelocity(A, B, C, D, E, F, 'b', 'Linewidth', 1.8);

legend('Error vector');

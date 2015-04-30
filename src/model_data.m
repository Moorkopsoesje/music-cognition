clear all
intervals = load('all_intervals.csv');

data = load('intervals/average_intervals.csv'); % Experiment data
entropy = load('intervals/entropy.csv');

data = data(:,2:end); % Remove first column


% Difference performance/original
delta = data - intervals;

%Length of these error vectors
length_delta = sqrt(sum(delta.^2,2))

% Original
A = intervals(:,1);
B = intervals(:,2);
C = intervals(:,3);

% Performance
D = data(:,1);
E = data(:,2);
F = data(:,3);

%hold on
figure(1)
ternlabel('Interval 1', 'Interval 2', 'Interval 3');

legend('Error');
ternpcolor(A,B,C,length_delta);
hold on
ternpcolor(A,B,C,length_delta);
%hold on



figure(2)
terncontour(A,B,length_delta);
figure(3)
ternpcolor(A,B,entropy);
%terncontour(A,B,entropy);

set(0,'DefaultTextFontSize',16)
%ternlabel('Interval 1', 'Interval 2', 'Interval 3');

%ternplot(A, B, C, 'scatter', 'filled', 'k')
%ternplot(D, E, F, 'scatter', 'filled', 'r')

%ternvelocity(A, B, C, D, E, F, 'b', 'Linewidth', 1.8);

%legend('Error vector');

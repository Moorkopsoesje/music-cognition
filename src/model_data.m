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
set(0,'DefaultTextFontSize',14)


figure(100)
hold on
figure(1)
ternpcolor(A,B,C,length_delta);
colorbar
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');

figure(2)
terncontour(A,B,length_delta);
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');

figure(3)
ternpcolor(A,B,entropy);
colorbar
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');


figure(4)
terncontour(A,B,entropy);
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');

figure(5)
%ternplot(A, B, C, 'scatter', 'filled', 'k')
%ternplot(D, E, F, 'scatter', 'filled', 'r')
ternvelocity(A, B, C, D, E, F, 'b', 'Linewidth', 1.8);
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');

figure(6)
hold on
ternplot(A, B, C, 'scatter', 'filled','k')
%ternplot(D, E, F, 'scatter', 'filled', 'r')
ternvelocity(A, B, C, D, E, F, 'b', 'Linewidth', 1.8);
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');


figure(7)
hold on
ternlabel('\leftarrow Interval 1', '\leftarrow Interval 2', '\leftarrow Interval 3');
ternplot(A, B, C, 'scatter', 'filled','k')
ternplot(D, E, F, 'scatter', 'filled', 'r')
ternvelocity(A, B, C, D, E, F, 'b', 'Linewidth', 1.8);

%print('-f1','graphs/error_color','-dpng')
%print('-f2','graphs/error_contour','-dpng')
%print('-f3','graphs/entropy_color','-dpng')
%print('-f4','graphs/entropy_contour','-dpng')
%print('-f5','graphs/quiver','-dpng')
%print('-f6','graphs/quiver_withfrom','-dpng')
%print('-f7','graphs/quiver_withfromto','-dpng')



%legend('Error vector');

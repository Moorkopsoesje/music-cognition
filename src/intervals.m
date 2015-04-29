interv = csvread('all_intervals.csv')
length=size(interv,1)

for i = 1:length
    interv(i,4) = i
end

%e01 = csvread('filtered-indices-e01.csv')
file_e01 = horzcat(e01, csvread('filtered-intervals-e01.csv'))

e02 = csvread('filtered-indices-e02.csv')
file_e02 = horzcat(e02, csvread('filtered-intervals-e02.csv'))

%e03 = csvread('filtered-indices-e03.csv')
file_e03 = horzcat(e03, csvread('filtered-intervals-e03.csv'))

%e04 = csvread('filtered-indices-e04.csv')
file_e04 = horzcat(e04, csvread('filtered-intervals-e04.csv'))

%e05 = csvread('filtered-indices-e05.csv')
file_e05 = horzcat(e05, csvread('filtered-intervals-e05.csv'))

o01 = csvread('filtered-indices-o01.csv')
file_o01 = horzcat(o01, csvread('filtered-intervals-o01.csv'))

o02 = csvread('filtered-indices-o02.csv')
file_o02 = horzcat(o02, csvread('filtered-intervals-o02.csv'))

o03 = csvread('filtered-indices-o03.csv')
file_o03 = horzcat(o03, csvread('filtered-intervals-o03.csv'))

o04 = csvread('filtered-indices-o04.csv')
file_o04 = horzcat(o04, csvread('filtered-intervals-o04.csv'))

files = vertcat(file_e01, file_e02, file_e03, file_e04, file_e05, file_o01, file_o02, file_o03, file_o04)

[values, order] = sort(files(:,1));
sortedmatrix = files(order,:)

 
j=0;
i=1;
startpos=1;
counter = 1;
B = zeros(66,4);

for k=1:66
    while(sortedmatrix(i,1) == j && counter <582)
        counter = counter +1
        i = i +1;
    end
        B(k,:)=mean(sortedmatrix(startpos:counter-1,:))
        startpos=counter;
        j=j+1;
    
end

csvwrite('average_intervals.csv',B)


    

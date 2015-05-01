clear all;

% (First you need to run the files to read in the intervals per participant)

interv = csvread('all_intervals.csv');
length=size(interv,1);

%for i = 1:length
%    interv(i,4) = i;
%end

part_names = ['e01'; 'e02'; 'e03'; 'e04'; 'e05'; 'e06'; 'o01'; 'o02'; 'o03'; 'o04'; 'o05'; 'o06'];

% Errors

all = 0;

for i = 1:size(part_names,1)
    % Read recorded intervals per participant
    filename_indices = strcat('intervals/filtered-indices-', part_names(i,:),'.csv');
    filename_intervals = strcat('intervals/filtered-intervals-', part_names(i,:),'.csv');
    
    indices = csvread(filename_indices);
    intervals_ = csvread(filename_intervals);
    ind_intervals = horzcat(indices, intervals_);
    
    if all == 0
        all = ind_intervals;
        
    else
        all = vertcat(all, ind_intervals);
    end
    % Calculate errors per participant
    dist_sum = 0;
    for j = 1:size(ind_intervals,1)
        index = ind_intervals(j,1)+1;
        vect = ind_intervals(j,2:end);
        vect_original = interv(index,:);
        dist_sum = dist_sum + dist(vect, vect_original');
    end
    
    error_pp(i) = dist_sum / size(ind_intervals,1)
    
end
csvwrite('intervals/error_per_person.csv',error_pp);
    


files = all;

[values, order] = sort(files(:,1));
sortedmatrix = files(order,:);


% Average per participant
 
j=0;
i=1;
startpos=1;
counter = 1;
B = zeros(66,4);

% loop over all different original intervals
for k=1:66
    % loop over the amount of recorded intervals for the original interval
    while(sortedmatrix(i,1) == j && counter < size(sortedmatrix,1))
        counter = counter +1;
        i = i +1;
    end
    % average the recorded intervals per participant per original
    % interval
    B(k,:)=mean(sortedmatrix(startpos:counter-1,:));
    startpos=counter;
    j=j+1;
    
end

csvwrite('intervals/average_intervals.csv',B);


% Entropy 
j=0;
i=1;
startpos = 1;
counter = 1;
entropy = zeros(66,1);

% loop over original intervals
for k=1:66
    % loop over all recorded intervals for the original interval
    sdist = 0;
    n = 0;
    while(sortedmatrix(i,1) == j && counter < size(sortedmatrix,1))
        counter = counter +1;
        % calculate distance of recorded interval to average (entropy) 
        % of intervals of participant
        from = sortedmatrix(i,2:4);
        to = B(k,2:4);
        sdist = sdist + dist(from, to');
        % count how many intervals per participant
        n = n + 1;
        i = i +1;
    end
    startpos=counter;
    j=j+1;
        
    % Normalize over how many intervals per participant
    entropy(k) = sdist/n;
        
    n = 0;
    
end

csvwrite('intervals/entropy.csv',entropy);
%entropy;
    

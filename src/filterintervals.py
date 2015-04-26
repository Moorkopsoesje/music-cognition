# -*- coding: utf-8 -*-
# Filter performed intervals, write to file with corresponding index..
from __future__ import division
import csv
import numpy as np
import matchintervals

#Split intervals per performance
def split_intervals(subject):
    
    
    with open('intervals/'+subject+'.txt') as f:
        intervals = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        intervals = [x for x in intervals]
        intervals.append([6.45])
        
        split = [];
        
        current = [];
        
        for interval in intervals:
            interval = interval[0]   
            
            if interval > 1:
                if interval > 6.5:
                    raise Exception("wtf, ?!?!")
                    
                split.append(current);
                current = []
                continue
            
            current.append(interval)
            
        
        return split
    
    
def split_timestamps(subject):
    with open('timestamps/'+subject+'.txt') as f:
        timestamps = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        timestamps = [x[0]+2 for x in timestamps]
        
        split = [];
        
        
        for i in range(99):
            fr = i*6+1
            to = fr + 5
            
            current = []
            
            for ts in timestamps:
                if ts >= fr and ts < to:
                    current.append(ts)
                    
            split.append(current)
        
        
        return split

def timestamps_to_intervals(split):
    
    intervals = []
    
    for x in split:
        interval = []
        for i in range(len(x)-1):
            j = i + 1
            interval.append(np.array(x[j])-np.array(x[i]))
    
        intervals.append(interval)
    return intervals        
        
def filter_intervals(labeled):
    
    filtered = []
    
    for label, interval in labeled:
        if len(interval) == 3:
            filtered.append((label,interval))
            
    return filtered
    
def normalize_intervals(labeled):
    normalized = []

    for label, interval in labeled:
        i_sum = sum(interval)
        
        normalized.append((label,np.array(interval)/i_sum))
            
    return normalized
    
def first_el(item):
    return item[0]    
    
def print_len(item):
    print len(item)    
    
if __name__ == '__main__':
    
    subject = 'e01'
    
    split = split_timestamps(subject);
    intervals = timestamps_to_intervals(split)
    
      
    #e01 becomes even-p01
    if subject.startswith('o'):
        original_interval_name = 'odd-p'+subject[-2:]
    else:
        original_interval_name = 'even-p'+subject[-2:]
    
    
    #Indices of experiment indices the subject heard
    order = matchintervals.get_interval_indices(original_interval_name)
    
    #Repeat every item in order 3 times (as subjects heard the same 3 times)
    order_x3 = [x for x in order for i in range(3)]
    
    #Tuples of (index, list of intervals)
    labeled =   zip(order_x3, intervals)  
    
    #Normalize so they sum to one
    labeled = normalize_intervals(labeled)    
    
    #Sort the intervals by index
    sorted_labeled = sorted(labeled, key=first_el)
    
    
    
    filtered = filter_intervals(sorted_labeled)  
    map(matchintervals._print, filtered)
    
    print 'N Before filtering failed ones: ', len(intervals)
    print 'N After filtering: ', len(filtered)
    
    f_labels, f_intervals = zip(*filtered)
    
    np.savetxt('./intervals/filtered-intervals-'+subject+'.csv', f_intervals, delimiter=',')
    np.savetxt('./intervals/filtered-indices-'+subject+'.csv', f_labels, delimiter=',', fmt="%1.d")
# -*- coding: utf-8 -*-
# Filter performed intervals, write to file with corresponding index..
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
    
def first_el(item):
    return item[0]    
    
def print_len(item):
    print len(item)    
    
if __name__ == '__main__':
    
    subject = 'e04'
    
    split = split_timestamps(subject);
    intervals = timestamps_to_intervals(split)
    
      
    
    if subject.startswith('o'):
        original_interval_name = 'odd-p'+subject[-2:]
    else:
        original_interval_name = 'even-p'+subject[-2:]
    
    
    #Indices of experiment indices the subject heard
    order = matchintervals.get_interval_indices(original_interval_name)
    
    #Repeat every item in order 3 times (as subjects heard the same 3 times)
    order_x3 = [x for x in order for i in range(3)]
    
    #Tuples of 'index, list of intervals'
    labeled =   zip(order_x3, intervals)  
    
    sorted_labeled = sorted(labeled, key=first_el)
    #print sorted_labeled
    
    map(matchintervals._print, sorted_labeled)
    
    filtered = filter_intervals(sorted_labeled)    
    
    #print split
    #print [len(x) for x in split]
    #print [len(x) for x in intervals] 
    #print [sum(x) for x in intervals]
    print len(split)
    print len(intervals)
    print len(filtered)
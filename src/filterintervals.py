# -*- coding: utf-8 -*-
# Filter performed intervals, write to file with corresponding index..
import csv
import numpy as np

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
        
        
    
if __name__ == '__main__':
    split = split_timestamps('o04');
    intervals = timestamps_to_intervals(split)
    
    #print intervals    
    
    #print split
    print [len(x) for x in split]
    print [len(x) for x in intervals] 
    print [sum(x) for x in intervals]
    print len(split)
    print len(intervals)
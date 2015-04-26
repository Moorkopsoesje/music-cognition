# -*- coding: utf-8 -*-
import csv


def match_intervals(all_intervals, experiment_intervals):
    
    #print [x for x in experiment_intervals]    
    
    indices = []
    for interval in experiment_intervals:
        index = find_closest(interval, all_intervals)
        indices.append(index)


    return indices        
        


def find_closest(interval, list_of_intervals):
    
    closest_index = -1
    closest_distance = 100000
    
    for i, src in enumerate(list_of_intervals):
        
        distance = abs(interval[0] - src[0]) +  abs(interval[1] - src[1]) + abs(interval[2] - src[2])
        
        if distance < closest_distance:
            closest_index = i
            closest_distance = distance
            
    
    #print list_of_intervals[closest_index], '\n', interval, '\n----'
    
    return closest_index
    
def get_interval_indices(subject='odd-p01'):
    with open('all_intervals.csv') as f:
        all_intervals = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        
        with open(('exp/'+subject+'-intervals.csv')) as g:
            exp_intervals = csv.reader(g, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            
            exp_intervals = [x for x in exp_intervals]
            all_intervals = [x for x in all_intervals]
            
            
            #print exp_intervals
            indices = match_intervals(all_intervals, exp_intervals)
    return indices
def _print(a):
    print(a)

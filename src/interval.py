from __future__ import division
import numpy as np
import random
import makemidi
import os

#Multidimensional range
def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step


def gen_intervals(resolution = 19, minimal_interval=0):
    
    
    pos = [x for x in drange(1/resolution, (resolution-1)/resolution, 1/resolution)]
    
    intervals = []
    err = 0.00001
    
    for x1 in pos:
        for x2 in pos:
            for x3 in pos:
                
                # Has a total length of 1 second
                if x1 + x2 + x3 > 1.0 - err and x1 + x2 + x3 < 1.0 + err:
                   # Doesn't have very short intervals
                   if x1 > minimal_interval and x2 > minimal_interval and x3 > minimal_interval:
                        intervals.append( [x1,x2,x3])

    return intervals
    
    
def write_to_csv(intervals, filename='./intervals.csv'):
    np.savetxt(filename, intervals, delimiter=',')
    
    
def gen_intervals_with_noise(resolution=19, minimal_interval=0.157):
    
    base = gen_intervals(resolution, minimal_interval)
    
    for intervals in base:
        for i in range(len(intervals)):
            intervals[i] += random.random()*0.03-0.015
            
            
    
    return base
    
def take_even_uneven(intervals):
    even = []
    uneven = []    

    for i, interval in enumerate(intervals):
        if i % 2 == 0:
            even.append(interval)
        else:
            uneven.append(interval)
            
    return even, uneven
    
def generate_for_subject(name, resolution=19, minimum_interval=0.157):
    
    if not os.path.exists('../data'):
            os.makedirs('../data')    
    
    intervals = gen_intervals(resolution, minimum_interval)
    
    even, uneven = take_even_uneven(intervals)
    random.seed(name)
    random.shuffle(even)
    random.shuffle(uneven)
    
    
    for is_even in [True, False]:
        
        if is_even:
            intervals = even
            filename = '../data/even-' + name
        else:
            intervals = uneven
            filename = '../data/uneven-' + name
            
        write_to_csv(intervals, filename+'-intervals.csv')
        makemidi.makemidi(intervals, filename)

if __name__ == '__main__':
    #intervals = gen_intervals(19, 0.157)
    #noisy_intervals = gen_intervals_with_noise(19, 0.157)
    #write_to_csv(intervals)
    #write_to_csv(noisy_intervals, './noise.csv')
    generate_for_subject('senna')
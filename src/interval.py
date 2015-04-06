from __future__ import division

#Multidimensional range
def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step


def gen_intervals(resolution = 16, minimal_interval=0):
    
    
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
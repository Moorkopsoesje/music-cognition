from __future__ import division

def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step


def gen_intervals(resolution = 16):
    
    
    pos = [x for x in drange(1/resolution, (resolution-1)/resolution, 1/resolution)]
    
    intervals = []
    err = 0.00001
    
    for x1 in pos:
        for x2 in pos:
            for x3 in pos:
                if x1 + x2 + x3 > 1.0 - err and x1 + x2 + x3 < 1.0 + err:
                    intervals.append( [x1,x2,x3])

    return intervals


if __name__ == '__main__':
    intervals = gen_intervals(8)
    print len(intervals), intervals
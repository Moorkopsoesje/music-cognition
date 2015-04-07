'''
Created on 6 apr. 2015

@author: Senna
'''

import interval
import makemidi

if __name__ == '__main__':
    intervals = interval.gen_intervals(19, 0.15)
    print len(intervals), intervals
    testphase = True
    makemidi.makemidi(intervals, testphase)
    print len(intervals), intervals
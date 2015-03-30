from __future__ import division
import terplot
import pylab

def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step

resolution = 16


pos = [x for x in drange(1/resolution, (resolution-1)/resolution, 1/resolution)]

intervals = []
err = 0.00001

for x1 in pos:
    for x2 in pos:
        for x3 in pos:
            if x1 + x2 + x3 > 1.0 - err and x1 + x2 + x3 < 1.0 + err:
                intervals.append( [x1,x2,x3])


#print intervals
print len(intervals)
data = pylab.vstack(intervals)
#terplot.ternaryPlot(data)
s=1000

newdata,ax = terplot.ternaryPlot(data)

ax.scatter(
    newdata[:,0],
    newdata[:,1],
    s=64,
    alpha=0.8,
    )
pylab.show()
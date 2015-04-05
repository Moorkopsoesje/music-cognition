# -*- coding: utf-8 -*-

from matplotlib import pyplot
import ternary
import math


steps = 30

ax = ternary.draw_boundary(steps)
ternary.draw_horizontal_line(ax, steps, 10)
ternary.draw_left_parallel_line(ax, steps, 15, linewidth=2., color='red')
ternary.draw_right_parallel_line(ax, steps, 15, linewidth=3., color='blue')

ax.set_title("Various Lines")

pyplot.show()



def shannon_entropy(p):
    """Computes the Shannon Entropy at a distribution in the simplex."""
    s = 0.
    for i in range(len(p)):
        try:
            s += p[i] * math.log(p[i])
        except ValueError:
            continue
    return -1.*s


func = shannon_entropy
pyplot.figure()
ax = ternary.function_heatmap(func, steps=steps, boundary=True, style="triangular")
ternary.draw_boundary(steps, ax=ax)
ax.set_title("Shannon Entropy Heatmap")

pyplot.show()

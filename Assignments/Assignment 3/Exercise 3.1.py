#Exercise 3.1 - Plotting experimental data

from pylab import plot,show
from math import sin
from numpy import linspace

xpoints = []
ypoints = []

for x in linspace(0,10,100):
    xpoints.append(x)
    ypoints.append(sin(x))

plot(xpoints,ypoints)
show()

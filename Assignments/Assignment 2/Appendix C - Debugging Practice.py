import numpy as np
import math as m
from visual.graph import *

def px(x,v,t,a):
    return x + v*t + 0.5*a*t**2
    #return v*t + .5*a*t*t

x0 = 1.0
vx0 = 70.0

y0 = 0.0
vy0 = 80.0

ax = 0.0
ay = -9.8

delt = 0.1
t = 0.0

x = []
y = []

for i in range(170):
    x.append(px(x0,vx0,t,ax))
    y.append(px(y0,vy0,t,ay))
    t = t + delt

    if t > 1.0:
        break

plotWindow = gdisplay(xtitle="Time", ytitle="Y Position")
plot = gcurve(color=color.cyan)
for j in range(len(x)):
    plot.plot(pos=(x[j], y[j]))

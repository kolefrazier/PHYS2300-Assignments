import numpy as np
import math as m
from visual.graph import *

def px(x,v,t,a):
    #return x + v*t + 0.5*a*t**2
    return v*t + .5*a*t*t

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

plotWindow = gdisplay(xtitle="Time", ytitle="Y Position")

for i in range(170):
    print('i: {0}\tt: {1}'.format(str(i), str(t)))
    
    #x.append(px(x0,vx0,t,ax))
    x.append(t)
    y.append(px(y0,vy0,t,ay))
    print('x[i]: {0}\ty[i]: {1}'.format(x[i], y[i]))
    t = t + delt

    if t > 1.0:
        print('BREAK!\ti: {0}\ty[i]: {1}'.format(str(i), str(y[i])))
        break
    
    plot = gcurve(color=color.cyan)
    for j in range(len(x)):
        plot.plot(pos=(x[j], y[j]))

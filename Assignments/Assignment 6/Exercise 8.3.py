#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 8.3
#
# Usage: python "Exercise 8.3.py"
#
# Description: Calculate and plot the Lorenz Equations
#
# Inputs: N/A
#
# Outputs: Two different plots, one for Part A (Y versus Time) and Part B (Z versus X)
#
# Auxiliary Files: N/A
#
# Special Instructions: N/A
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------

import matplotlib
import matplotlib.pyplot as plot
from numpy import array, arange
    
def f(r, t):
    x = r[0]
    y = r[1]
    z = r[2]
    
    fx = sigma * (y-x)
    fy = (constR*x) - y - (x*z)
    fz = (x*y) - (b*z)
    
    return array([fx, fy, fz],float)

#Time Variables
timeStart = 0
timeEnd = 50

#Variables and Constants required for Lorenz equations
x = 0.0
y = 1.0
z = 0.0
sigma = 10.0
constR = 28.0
b = (8.0/3.0)

N = 1000
h = abs(y - x)/N

#Plot data containers
xPoints = []
yPoints = []
zPoints = []
tPoints = arange(timeStart, timeEnd,h) #Time

r = array([1.0, 1.0, 1.0], float)

for t in tPoints:
    #Calculate X values then Y values
    xPoints.append(r[0])
    yPoints.append(r[1])
    zPoints.append(r[2])
    
    #Runge-Kutta Method    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    
#Plot data
#--Part A--
plot.figure()
plot.title('Part-A: Y-Points versus Time')
plot.plot(tPoints, yPoints, 'b', linewidth=2.0)
plot.xlabel('Time (t)')
plot.ylabel('Y-Points')
plot.show()

#--Part B--
plot.figure()
plot.title('Part-B: Z-Points versus X-Points')
plot.plot(zPoints, xPoints, 'b', linewidth=2.0)
plot.xlabel('Z-Points')
plot.ylabel('X-Points')
plot.show()
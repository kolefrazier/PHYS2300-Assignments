#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 8.2 - The Lotka-Volterra Equations
#
# Usage: python "Exercise 8.2.py"
#
# Description: Calculates populations of two groups (Prey and Predators) over time.
#
# Inputs: N/A
#
# Outputs: Plot of Predator and Prey populations versus Time
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

def preyReproduction(x, y, t):
    return (alpha * x) - (beta * x * y)
    
def predatorReproduction(x, y, t):
    return (gamma*x*y)-(delta*y)
    
def f(x, y, t):
    return h*preyReproduction(x,y,t), h*predatorReproduction(x,y,t)

#Predator and Prey values.
#  Must be a multiple of 0.001, as each whole int (eg 1.0) represents a thousand of the population.
x = 2.0 #Prey (rabbits)
y = 3.0 #Predators (foxes)

#Time Variables
timeStart = 0
timeEnd = 30

#Runge-Kutta Values I *think* are needed?
N = 1000
h = abs(y - x)/N

#Constants required for Lotka-Volterra equations
alpha = 1.0
beta = 0.5
gamma = 0.5 #Looks like a lower-case y
delta = 2.0 #Looks like a lower-case d

xPoints = [] #Prey
yPoints = [] #Predator
tPoints = arange(timeStart, timeEnd) #, h) #arange(x,y,h) #Time

r = array([1.0,1.0], float)
print(r)

for t in tPoints:
    #Calculate X values then Y values
    xPoints.append(r[0])
    yPoints.append(r[1])
    
    #Runge-Kutta Method    
    dx1, dy1 = f(x, y, t) #Results are multipled by H inside function f(). //h*f(x, y, t)
    dx2, dy2 = f(r+0.5*dx1, r+0.5*dy1, t+0.5*h)
    dx3, dy3 = f(r+0.5*dx2, r+0.5*dy2*h, t+0.5*h)
    dx4, dy4 = f(r+dx3, r+dy3, t+h)
    
    r += (dx1 + 2*dx2 + 2*dx3 + dx4)/6
    #r[1] += (dy1 + 2*dy2 + 2*dy3 + dy4)/6
    
# print '--- DEBUG ---'
# print 'X Points: {0}'.format(xPoints)
# print 'Y Points: {0}'.format(yPoints)
# print 'R Values: {0}'.format(r)
    
#Plot data
plot.figure()
plot.plot(tPoints, xPoints) #, 'g', linewidth=2.0)
plot.plot(tPoints, yPoints) #, 'r', linewidth=2.0)
plot.xlabel('Time (t)')
plot.ylabel('Prey (green) & Predator (red) Populations')
plot.show()
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
# Version: alpha-3.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------
# Exercise Questions
#--------------------------------------------------------------------------------
#   B) Describe in words what is going on in the system.
#
#   The Lotka-Volterra equations represent proportional populations over time.
#   As the population of prey increases, it provides the predators opportunity to feed/prosper and 
#    increase their population. But as the population of prey decreases, the predators no longer have
#    the resources to sustain their population and begin to lose population over time. 
#   This creates a cycle of population cause-and-effect.
#
#   If the population data points were graphed as a Prey-Population versus Predator-Population, the resulting
#    graph becomes a circle instead of a linear result.
#--------------------------------------------------------------------------------

import matplotlib
import matplotlib.pyplot as plot
from numpy import array, arange
    
def f(r, t):
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y-delta*y
    return array([fx,fy],float)

#Predator and Prey values.
#  Must be a multiple of 0.001, as each whole int (eg 1.0) represents a thousand of the population.
x = 2.0 #Prey (rabbits)
y = 3.0 #Predators (foxes)

#Time Variables
timeStart = 0
timeEnd = 30

N = 1000
h = abs(y - x)/N

#Constants required for Lotka-Volterra equations
alpha = 1.0
beta = 0.5
gamma = 0.5 #Looks like a lower-case y
delta = 2.0 #Looks like a lower-case d

xPoints = [] #Prey
yPoints = [] #Predator
tPoints = arange(timeStart, timeEnd,h) #, h) #arange(x,y,h) #Time

r = array([1.0,1.0], float)

for t in tPoints:
    #Calculate X values then Y values
    xPoints.append(r[0])
    yPoints.append(r[1])
    
    #Runge-Kutta Method    
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    
#Plot data
plot.plot(tPoints, xPoints, 'g', linewidth=2.0)
plot.plot(tPoints, yPoints, 'r', linewidth=2.0)
plot.xlabel('Time (t)')
plot.ylabel('Prey (green) & Predator (red) Populations')
plot.show()
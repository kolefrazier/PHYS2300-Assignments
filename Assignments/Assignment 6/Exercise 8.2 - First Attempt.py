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

def preyReproduction(x, y, alpha, beta):
    return (alpha * x) - (beta * x * y)
    
def predatorReproduction(x, y, gamma, delta):
    return (gamma*x*y)-(delta*y)
    
def f(x, t):
    print 'something here'
    
def rungeKutta(h, x, t, fx):
    #From page 338 in the text
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f(x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)
    x = (k1 + 2*k2 + 2*k3 + k4)/6

#Predator and Prey values.
#  Must be a multiple of 0.001, as each whole int (eg 1.0) represents a thousand of the population.
x = 2.0 #Prey (rabbits)
y = 3.0 #Predators (foxes)

#Constants required for Lotka-Volterra equations
alpha = 1.0
beta = 0.5
gamma = 0.5 #Looks like a lower-case y
delta = 2.0 #Looks like a lower-case d

#Time Variables
timeStart = 0
timeEnd = 30

#Runge-Kutta Values I *think* are needed?
N = 1000
h = (y - x)/N

preyPops = [] #Prey
predatorPops = [] #Predator
t = [] #Time

for t in range(timeStart, timeEnd):
    t = float(t)
    #Prey Calculation
    preyPops.append(rungeKutta(h, preyReproduction(x, y, alpha, beta), t))
    predatorPops.append(rungeKutta(h, predatorReproduction(x, y, gamma, delta), t))
    
#Plot data
plot.figure()
plot.plot(t, preyPops, 'g', linewidth=2.0)
plot.plot(t, predatorPops, 'r', linewidth=2.0)
plot.xlabel('Time (t)')
plot.ylabel('Prey (green) & Predator (red) Populations')
plot.show()
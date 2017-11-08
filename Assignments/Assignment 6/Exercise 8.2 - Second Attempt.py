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

#Constants required for Lotka-Volterra equations
alpha = 1.0
beta = 0.5
gamma = 0.5 #Looks like a lower-case y
delta = 2.0 #Looks like a lower-case d

def preyReproduction(x, y, t):
    return (alpha * x) - (beta * x * y)
    
def predatorReproduction(x, y, t):
    return (gamma*x*y)-(delta*y)
    
def f(x, y, t):
    return preyReproduction(x,y,t), predatorReproduction(x,y,t)
    
def rungeKutta(h, x, y, xt, yt, t):
    #From page 338 in the text
    
    #Prey = dx, Predators = dy
    dx1, dy1 = h*f(x, y, t)
    dx2, dy2 = h*f(x+0.5*dx1, y+0.5*dy1, t+0.5*h)
    dx3, dy3 = h*f(x+0.5*dx2, y+0.5*dy2, t+0.5*h)
    dx4, dy4 = h*f(x+dx3, y+dy3, t+h)
    
    dx4 += (dx1 + 2*dx2 + 2*dx3 + dx4)/6
    dy4 += (dy1 + 2*dy2 + 2*dy3 + dy4)/6
        
    return dx4, dy4

#Predator and Prey values.
#  Must be a multiple of 0.001, as each whole int (eg 1.0) represents a thousand of the population.
x = 2.0 #Prey (rabbits)
y = 3.0 #Predators (foxes)

#Time Variables
timeStart = 0
timeEnd = 30

#Runge-Kutta Values I *think* are needed?
N = 10
h = abs(y - x)/N

preyPops = [x] #Prey
predatorPops = [y] #Predator
times = [0] #Time

for t in range(timeStart, timeEnd):
    #Prey Calculation
    newPrey, newPredator = rungeKutta(h, preyPops[t], predatorPops[t], t)
    
    preyPops.append(newPrey)
    predatorPops.append(newPredator)
    times.append(t)
    
print '--- Prey ---\n{0}\n\n--- Pred ---\n{1}'.format(preyPops, predatorPops)
    
#Plot data
plot.figure()
plot.plot(times, preyPops, 'g', linewidth=2.0)
plot.plot(times, predatorPops, 'r', linewidth=2.0)
plot.xlabel('Time (t)')
plot.ylabel('Prey (green) & Predator (red) Populations')
plot.show()
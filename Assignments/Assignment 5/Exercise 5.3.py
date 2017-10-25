#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 5.3
#
# Usage: python "Exercise 5.3.py"
#
# Description: Calculates E(x) over a range of 0 to 3 (in 0.1 steps) then graphs the values.
#
# Inputs: None
#
# Outputs: Console data
#
# Auxiliary Files: None
#
# Special Instructions: None
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------


import math #for math.exp(x), which returns e^x
import numpy
import matplotlib
import matplotlib.pylab as plot
import matplotlib.patches as mpatches

def f(x):
    return math.exp(-x**2)

#Limits of integration
a = 0.0
b = 3.0

#Other values needed
N = 1000
h = (b-a)/N

eXValues = []
stepValues = []

s = 0.5*f(a) + 0.5*f(b)
for k in numpy.arange(a, b+0.1, 0.1): #b+0.1 takes the range from 0 to 3 instead of from 0 to 2.9.
    x = f(a+k*h)
    eXValues.append(k)
    stepValues.append(x)
    s += x
    
#Plot data
plot.figure()
plot.plot(eXValues, stepValues, 'b', linewidth=2.0)
velocityLegendEntry = mpatches.Patch(color='blue', label='Velocity (m/s) over time')
plot.title('Graph of E(x) as a function of X')
plot.xlabel('X-Values')
plot.ylabel('E(x) Values')
plot.show()

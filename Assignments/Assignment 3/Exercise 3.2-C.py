#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.2-C
#
# Usage: Plot Fey's Function
#
# Description: Visually plot Fey's function
#
# Inputs: None
#
# Outputs: Graph of the Fey's function.
#
# Auxiliary Files: None
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------

from pylab import plot, ylim, xlabel, ylabel, show, legend
from numpy import linspace, sin, cos, pi
from math import e

# --- Part C ---
CartesianX = []
CartesianY = []
for theta in linspace(0, 10*pi, 1000):
    r = e**(cos(theta))-(2.0*cos(4.0*theta))+(sin(theta/12.0)**5) #Fey's Function
    #Convert to Cartesian Coordinates
    CartesianX.append(r*cos(theta))
    CartesianY.append(r*sin(theta))

# General graph setup and plotting/activation
xlabel("x axis")
ylabel("y axis")

plot(CartesianX, CartesianY, 'b-')
show()
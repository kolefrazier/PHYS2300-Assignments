#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.2-B
#
# Usage: Plot the Galilean Spiral
#
# Description: Using hard-coded trigonometry equations, calculate polar then cartesian
#   coordinates and plot them to visualize the Galilean Spiral.
#
# Inputs: None
#
# Outputs: Graph of the Galilean Spiral.
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

# --- Part B ---
CartesianX = []
CartesianY = []

for theta in linspace(0, 10*pi, 300):
    r = theta**2 #Galilean Spiral, r, for each theta in the range.
    #Convert to Cartesian Coordinates
    CartesianX.append(r*cos(theta))
    CartesianY.append(r*sin(theta))

# General graph setup and plotting/activation
xlabel("x axis")
ylabel("y axis")

plot(CartesianX, CartesianY, 'b-')
show()
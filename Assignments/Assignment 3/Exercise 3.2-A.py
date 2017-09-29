#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.2-A
#
# Usage: Plot trigometric curves
#
# Description: Plot a simple deltoid curve from hard-coded trigonometry equations.
#
# Inputs: None
#
# Outputs: Graph of the deltoid curve.
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

# --- Part A ---
x = linspace(0,2*pi,100)
xpoints = 2*cos(x)+cos(2*x)
ypoints = 2*sin(x)-sin(2*x)

plot(xpoints,ypoints,"g-", label="Part A")
ylim(-10,10)

# General graph parts
xlabel("x axis")
ylabel("y axis")
show()
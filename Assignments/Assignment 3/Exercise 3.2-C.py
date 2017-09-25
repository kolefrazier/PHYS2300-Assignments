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
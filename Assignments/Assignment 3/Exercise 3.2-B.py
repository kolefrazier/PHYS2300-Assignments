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
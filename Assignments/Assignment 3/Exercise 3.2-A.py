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
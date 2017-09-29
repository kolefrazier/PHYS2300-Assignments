#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.6 - Feigenbaum Plot
#
# Usage: Graph the Feigenbaum plot for a small range of numbers.
#
# Description: This program generates a sample of the Feigenbaum plot for a small range.
#
# Inputs: None
#
# Outputs: Graphical Feigenbaum plot.
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------
# Answers to Exercise Questions
#--------------------------------------------------------------------------------
# --A--
#	A fixed point would look like a simple line over time. On a heat map, the point would be very large as the point repeats over time.
#	A limit cycle would look more like a small loop - closer to a low-polygon circle or a diamond.
#	Chaos would look like, well, chaos. Points everywhere, potentially filling the space for a given range.
#
# --B--
# Things start looking more chaotic around r=2000, but get really chaotic around 4=2500.

# Exercise 3.6 - Feigenbaum Plot
import matplotlib
import matplotlib.pylab as plot

def Feigenbaum(r, x):
    #Recursing 1000 times is too much for Python, so while loop it is!
    i = 0
    while (i < 1000):
        i += 1
        x = r*x*(1-x)
    return x
    
def FeigenbaumList(r,x):
    xvalues = []
    #Recursing 1000 times is too much for Python, so while loop it is!
    i = 0
    while (i < 1000):
        i += 1
        x = r*x*(1-x)
        xvalues.append(x)
    return xvalues

rValues = [] #Horizontal axis values
xValues = [] #Vertical axis values
xBase = 0.5 #For a given value of r, start with x=0.5

Start = 1.1
End = 4.0
Step = 0.001
Current = Start #More for keeping track of variables

while Current <= End:
    #Iterate r a thousand times to settle down or limit cycle
    #Then iterate a thousand more times to get the point to plot.
    FirstThousand = Feigenbaum(Current, xBase)
    SecondThousand = FeigenbaumList(Current, FirstThousand) #The book does NOT make it clear that you need to save (and plot) either of the thousands.
    
    rValues.append(Current)
    xValues.append(SecondThousand)
    
    #Increase Start by the Step amount for the next iteration
    Current += Step

print('[DEBUG] Finished calculating, now on to graphing.')
#Graphing time
plot.figure()
plot.title("Feigenbaum Plot")
plot.plot(rValues, xValues, ".k")
plot.plot(xValues, "ko")
plot.xlabel("R-Values")
plot.ylabel("Y-Values")
print('[DEBUG] Finished plotting, show() time!\nNOTE: This is (inefficiently) plotting a LOT of points, give it a moment.')
plot.show()
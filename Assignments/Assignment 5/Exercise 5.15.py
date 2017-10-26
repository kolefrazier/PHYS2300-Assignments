#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 5.15
#
# Usage: python "Exercise 5.15.py"
#
# Description: Uses a central difference to calculate the derivative of the function in a range.
#
# Inputs: None
#
# Outputs: Graphed data
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

import math #for math.tanh and math.sec
import matplotlib
import matplotlib.pylab as plot

def f(x):
    return (1.0 + (1.0/2.0)*math.tanh(2.0*x))
    
def centralDifference(lower, upper, h):
    #Uses formula (5.95) from Page 191 in the text
    CentralDifferences = []
    XValues = []
    
    for x in range(lower, upper+1, 1):
        result = (f(x + h/2.0) - f(x - h/2.0))/h
        CentralDifferences.append(result)
        XValues.append(x)
        
    return CentralDifferences, XValues
    
def derivativeF(lower, upper):
    #Using this as my "analytical" formula for the derivative...
    #   (Due to the book nor my calculus education not really defining such ideas)
    #It is essentially the derivative of f(x), calculated for X using symbolic constants.
    AnalyticDerivatives = []
    for x in range(lower, upper+1, 1):
        result = math.tan(2*x)**2+1 #sec*82 = tan**2+1
        AnalyticDerivatives.append(result)
    
    return AnalyticDerivatives
    

lowerBoundary = -2
upperBoundary = 2
h = 10e-10 #Arbitrarily small number to represent H. Inspired from Page 190's discussion about error values in the text.

CentralDifferences, XValues = centralDifference(lowerBoundary, upperBoundary, h)
AnalyticResults = derivativeF(lowerBoundary, upperBoundary)

#Plot data
plot.figure()
plot.plot(XValues, CentralDifferences, 'g', linewidth=2.0)
plot.plot(XValues, AnalyticResults, 'b', linewidth=2.0)
plot.show()
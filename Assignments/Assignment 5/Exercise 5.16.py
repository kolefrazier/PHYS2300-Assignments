#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 5.16
#
# Usage: python "Exercise 5.16.py"
#
# Description: Helps estimate average error for an arbitrary function, f(x), using
#   the Forward Difference and Central Difference methods.
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
#   Exercise Responses
#--------------------------------------------------------------------------------
#   When h is greater than ~10e-7, the average Forward Difference error for an arbitrary polynomial
#   is smaller than the average Central Difference error.
#   Numbers smaller than ~10e-8 will result in larger or approximately equal error between the two methods.
#--------------------------------------------------------------------------------

import math #for math.tanh and math.sec
import numpy as np

def f(x):
    #Some easy to work with function, x^4+x^2
    return x**4+x**2

def derivativeF(x):
    return 4*x**3+2*x
    
def secondDerivativeF(x):
    return 12*x**2+2

def thirdDerivativeF(x):
    return 24*x
    
    
def centralDifference(lower, upper, h, c):
    #Uses formula (5.95) from the text
    CentralDifferences = []
    CentralDiffError = []
    
    for x in range(lower, upper+1, 1):
        result = (f(x + h/2.0) - f(x - h/2.0))/h
        CentralDifferences.append(result)
        
        approxError = (2*c*abs(f(x)))/h + ((1.0/24.0) * h**2 * abs(thirdDerivativeF(x)))
        CentralDiffError.append(approxError)
        
    return CentralDifferences, CentralDiffError
    
def forwardDifference(lower, upper, h, c):
    #Uses formula (5.87) from the text
    ForwardDifferences = []
    ForwardDiffError = []
    
    for x in range(lower, upper+1, 1):
        result = (f(x+h) - f(x))/h
        ForwardDifferences.append(result)
        
        approxError = ((2*c*abs(f(x)))/h)+(0.5*h*abs(secondDerivativeF(x)))
        ForwardDiffError.append(approxError)
        
    return ForwardDifferences, ForwardDiffError

lowerBoundary = -2
upperBoundary = 2
h = 10e-7 #Arbitrarily small number to represent H. Inspired from Page 190's discussion about error values in the text.
c = 10e-16 #Error constant C (page 190 in text)

#Start looking about the same around 10e-10
#So, numbers that are > 10e-8

CentralDifferences, CentralDifferenceError = centralDifference(lowerBoundary, upperBoundary, h, c)
ForwardDifferences, ForwardDifferenceError = forwardDifference(lowerBoundary, upperBoundary, h, c)

CentralAverageError = np.mean(CentralDifferenceError)
ForwardAverageError = np.mean(ForwardDifferenceError)

print('Central Difference average error: {0}\nForward Difference average error: {1}'.format(CentralAverageError, ForwardAverageError))
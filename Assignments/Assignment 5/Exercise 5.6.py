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
#   Exercise Responses
#--------------------------------------------------------------------------------
#    The calculated error is a bit off from the integral's result when N=10. 
#    This is primarily due to the small amount of slices being taken.
#    The accuracy is not going to be as accurate as it could be due to the small amount of slices being taken.
#    If we were to increase the number of slices being taken, the error would go down.
#--------------------------------------------------------------------------------

import math #for math.exp(x), which returns e^x

def f(x):
    return x**4 - 2*x + 1
    
def ErrorCalculate(one, two):
    return ((1.0/3.0)*(two - one))

a = 0.0
b = 2.0

# --- N=10 ---
N = 10
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
    

nOne = (h*s)

# --- N=20 ---
N = 20
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
    
nTwo = (h*s)

CalculatedError = ErrorCalculate(nOne, nTwo)

print('N=10\t= {0}\nN=20\t= {1}\nCalculated error: {2}\nAbsolute error: {3}'.format(nOne, nTwo, CalculatedError, abs(CalculatedError)))


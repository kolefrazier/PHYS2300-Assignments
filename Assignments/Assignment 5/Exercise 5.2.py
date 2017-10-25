#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 5.2
#
# Usage: python "Exercise 5.2.py"
#
# Description: Calculate a pre-defined integral using Simpson's rule with varied "slices"
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
#    The result I receive on this exercuse, using Simpson's Rule yields ~4.4.
#    At N=1000, the margin of error is ~0.08. As N increases by a factor of 10, 
#       the margin of error decreases by 10% to ~0.008.
#
#   See console output for N=10, N=100 and N=1000
#
#   The trapezoidal rule for this same equation 4.5 at 10 slices, 4.401 at 100 and 4.40001 at 1000 slices.
#   So, the trapezoidal rule is more accurate.
#
#--------------------------------------------------------------------------------


def f(x):
    return x**4-2*x+1
    
def simpson(N,a,b):
    #Using Simpson's Rule:
    h=(b-a)/N
    s=f(a)+b*f(b)
    
    for k in range(1, N+1, 2): #Odds
        s += 4.0*f(a+k*h)
    for k in range(2, N-1, 2): #Evens
        s += 2.0*f(a+k*h)
		
    return (1.0/3.0)*h*s

#Limits of integration
a = 0.0
b = 2.0

#Slices
N = 10
print('N = {0}\t\t= {1}'.format(N, simpson(N,a,b)))

N = 100
print('N = {0}\t\t= {1}'.format(N, simpson(N,a,b)))

N = 1000
print('N = {0}\t= {1}'.format(N, simpson(N,a,b)))

N = 10000
print('N = {0}\t= {1}'.format(N, simpson(N,a,b)))

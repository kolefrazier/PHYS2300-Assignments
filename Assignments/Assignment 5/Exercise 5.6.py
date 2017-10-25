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


import math #for math.exp(x), which returns e^x

def f(x):
    return x**4 - 2*x + 1
    
def ErrorCalculate(one, two):
    return (1/3)*(two - one)

N = 10
a = 0.0

# --- N=10 ---
b = 2.0
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)

nOne = (h*2)

# --- N=20 ---
N = 20
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
    
nTwo = (h*2)

CalculatedError = ErrorCalculate(nOne, nTwo)


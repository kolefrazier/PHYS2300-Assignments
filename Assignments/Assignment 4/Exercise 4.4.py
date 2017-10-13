# #--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 4.4
#
# Usage: python "Exercise 4.4.py"
#
# Description: Calculates a given integral
#
# Inputs: None
#
# Outputs: Console data, result and runtime (timing) information for the integral calculation
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

# --- Exercise 4.4 ---
# ======================
#    EXERCISE ANSWERS
# ======================
# On my computer, N=250,000 is the approximate limit for "integral slices calculated per second".
# Of course, this may vary depending on the computer's available resources (CPU speed, number of CPUs or chained GPUs, etc.)
#
#---------------------------------------------

from math import sqrt
import time

#Function to calculate "X-sub(k)."
#   Hard-coded equation, not universally dynamic.
def xk(h, k):
    return -1+h*k

#Function to calculate "Y-sub(k)" using the pre-calculated xk() value. 
#   Hard-coded equation, not universally dynamic.
def yk(xk):
    return sqrt(1-xk**2)

#Calculate an integral using the "Trapezoid"/"slices" method.
#   Based on the in-class examples.
def trapezoid(N, a, b):
    h = 2.0/N 
    y = 0.0
    for k in range (1, N):
        x = xk(h, k)
        y += yk(x)
    return y*h
    
#Integral and series values. 'a' and 'b' are the limits of integration.
#N = 250000 #The approximate amount of slices you can calculate in a single second.
N = 100
a = 1.0
b = -1.0

#Start a timer, calculate the integral, end the timer.
#   Elapsed time is calculated and printed in the print statement after the end timer.
start = time.time()
result = trapezoid(N, a, b)
end = time.time()

print 'N={0}\tI={1}\tTime Elapsed: {2} seconds'.format(N, result, (end-start))
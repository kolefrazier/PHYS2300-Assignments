# #--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 4.3
#
# Usage: python "Exercise 4.3.py"
#
# Description: Calculates a given derivative
#
# Inputs: None
#
# Outputs: Console data - derivative solution
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
# --- Exercise 4.3 ---
# ======================
#    EXERCISE ANSWERS
# ======================
# -A-
#   The analytical answer (~1.1) and the computer's answer (1.01) differ due to
#   rounding errors and the fact that humans estimate and computers work for precision.
# -B-
#   It gets better as the calculated value gets smaller and more precise.
#   But when it hits about 10^-10, the value starts getting less accurate.
#   This is due to rounding errors in the floating-point math. Computers cannot
#   handle decimal numbers naturally, so special methods have to be used to handle
#   these values. As decimal values increase in place values, the computer becomes
#   less accurate.
#--------------------------------------------------------------------------------

#Calculates a pre-defined function, f(x).
def f(x):
    return x*(x-1)

#Calculates a derivative using pre-defined function, f(x), using a given a text-provided polynomial
def derivative(x, delta):
    return (f(x+delta) - f(x))/(delta)

#Calculate the derivative for many different delta values. This helps represent/visualize the calculated limit.
for n in range(-2, -16, -2):
    delta = 10**n
    x = 1
    print 'x: {0} & delta: 10**{1}\t=>\tdf/dx: {2}'.format(x, n, derivative(x, delta))
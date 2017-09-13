#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.8
#
# Usage: Utilize the Numpy Python package to perform calculations on arrays.
#
# Description: Calculate interger values based on given arrays using
#   the Numpy Python package.
#
# Inputs: None
#
# Outputs: Array calculations
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

from numpy import array

#Setup arrays used in parts A, B and C
a = array([1,2,3,4],int)
b = array([2,4,6,8],int)

#Print solution to each section
print('Part A (b/a+1): ' + (b/a+1))
print('Part B (b/(a+1)): ' + (b/(a+1)))
#print('Part C (1/a): ' + (1/a))


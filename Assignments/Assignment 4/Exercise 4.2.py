# #--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 4.2
#
# Usage: python "Exercise 4.2.py"
#
# Description: Calculates quadratic roots
#
# Inputs: User input - values for polynomial coefficients, "A", "B", and "C".
#
# Outputs: Console data - Quadratic roots
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
# --- Exercise 4.2 ---
# ----- EXERCISE QUESTIONS -----
# -B-
#   When the values get really small, Python struggles to calculate accurate floating point numbers.
#   So, the "0.001x^2" (A) and "0.001" (C) make the answer incorrect or much less precise.
#   The "first method"/regular Quadratic Equation feels more accurate for numbers that aren't super small.
#   The "second method" feels more accurate for numbers that are much smaller.
# -C-
#   Based on my findings for part -B-, I designed the "Part C" part of my program to use the regular Quad. Equation
#   if a number is larger than an arbitrarily small number (eg 0.01), and use the "second" Quad. Equation if any of
#   the polynomial's coefficients are smaller than this arbitrarily small number.

from math import sqrt

def QuadraticNormal(a, b, c):
    PositiveRoot = ((-b) + sqrt(b**2 - 4*a*c))/(2*a)
    NegativeRoot = ((-b) - sqrt(b**2 - 4*a*c))/(2*a)
    return PositiveRoot, NegativeRoot
    
def QuadraticOtherWay(a, b, c):
    PositiveRoot = ((2*a)/((-b) + sqrt(b**2 - 4*a*c)))
    NegativeRoot = ((2*a)/((-b) - sqrt(b**2 - 4*a*c)))
    return PositiveRoot, NegativeRoot

#Get user input, cast to floats
a = float(input('Enter A: '))
b = float(input('Enter B: '))
c = float(input('Enter C: '))

print('--- Part A ---') #"Normal" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)
print('Positive root:\n\t{0}\n\tNegative root: {1}\n'.format(PositiveRoot, NegativeRoot))

print('--- Part B ---') #"Second" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticOtherWay(a, b, c)
print('Positive root:\n\t{0}\n\tNegative root: {1}\n'.format(PositiveRoot, NegativeRoot))

print('--- Solving 0.001x^2+100X+0.001=0 ---')
#Calculate 0.001x^2+100X+0.001=0 using both methods
#Reassign a, b, c
a = 0.0001
b = 1000.0
c = 0.001

#Simply reuse the above written statements.
#"Normal" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)
print('("Normal")\n\tPositive root: {0}\n\tNegative root: {1}'.format(PositiveRoot, NegativeRoot))
#"Second" Quadratic Formula
PositiveRoot, NegativeRoot = QuadraticOtherWay(a, b, c)
print('("Second")\n\tPositive root: {0}\n\tNegative root: {1}'.format(PositiveRoot, NegativeRoot))

print('--- Part c ---')
ArbitrarySmallNum = 0.01
if(a < ArbitrarySmallNum or b < ArbitrarySmallNum or c < ArbitrarySmallNum):
    PositiveRoot, NegativeRoot = QuadraticOtherWay(a, b, c)
    print('("Second")\n\tPositive root: {0}\n\tNegative root: {1}'.format(PositiveRoot, NegativeRoot))
else:
    PositiveRoot, NegativeRoot = QuadraticNormal(a, b, c)
    print('("Normal")\n\tPositive root: {0}\n\tNegative root: {1}'.format(PositiveRoot, NegativeRoot))
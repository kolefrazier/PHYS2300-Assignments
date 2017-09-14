#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.13 - Part B
#
# Usage: Calculate greatest common divisor of two numbers, recursively.
#
# Description: This program will calculate the greatest common divisor of two
#   nonnegative integers using Euclid's findings, which give us the following:
#       g(m,n) =
#           m           if n=0
#           g(n,m%n)    if n>0
#
# Inputs: Two integer numbers, m and n.
#
# Outputs: The greatest common divisor.
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

#GCD - Greatest Common Divisor
#Parameters:
#   M: A positive integer, given by user on first call.
#   N: A positive integer, given by user on first call.
#
#Recursively determines the GCD of M and N based on the following formula:
#   g(m,n) =
#       m           if n=0
#       g(n,m%n)    if n>0
def gcd(m, n):
    if (n == 0):
        return m
    elif (n > 0):
        return gcd(n, m%n)


m = int(input('Enter the first number, m: '))
n = int(input('Enter the second number, n: '))

print('The GCD of m({0}) and n({1}) is {2}'.format(str(m), str(n), gcd(m,n)))

#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.13 - Part A
#
# Usage: Calculate Catalan numbers recursively
#
# Description: This program will calculate a list of Catalan numbers recursively
#   up to the requested Nth Catalan number.
#
# Inputs: N - the Nth Catalan number requested.
#
# Outputs: The Nth Catalan number.
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

#reusable function to calculate the next number in the series.
#NextCatalanNumber parameters:
#   n is the current number
#   Cn is the Catalan number for n
#   goal is where we want to recurse (word?) to.
def NextCatalanNumber(n, Cn, goal):
    if(goal == 0):
        return 1
    
    elif(n == goal):
        #print('[DEBUG][GOAL HIT] Given: goal: {2} and n: {0} and Cn: {1}\t\t'.format(n, Cn, goal))
        return Cn
    else:
        #Calculate next Catalan number and print out this recurse's result.
        CatalanNumberForN = (((4*n) + 2)/(n + 2))*Cn
        #print('[DEBUG] Given: goal: {2} and n: {0} and Cn: {1}\t\t'.format(n, Cn, goal))

        #Increment n then recurse further.
        n += 1
        return NextCatalanNumber(n, CatalanNumberForN, goal)

#Helper variables
#   Cn = The current Catalan number at position 'n'
#   n = the positional counter for the Catalan number sequence.
#
#   Numbers are set with decimals to enforce float math instead of int math
Cn = 1.0        #Initialize Current as C0, or, 1.
n = int(input('Which Catalan number do you want?'))

print('C({0}) = {1}'.format(n, NextCatalanNumber(1, Cn, n)))
#From Exercise 2.7, we know that C(100) is: 3.53334332088e+57
    
    

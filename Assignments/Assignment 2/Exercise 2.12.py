#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.12
#
# Usage: Prime number calculation
#
# Description: 
#
# Inputs: 
#
# Outputs: 
#
# Auxiliary Files:
#
# Special Instructions:
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------

import math as m

#Setup working values
#   Program requirements state that our list of primes must begin with the number two already in it.
#   Then, we start n (or CurrentNumber) at 3 and work towards 10,000 (or EndNumber).
PrimeNumbers = [2]
CurrentNumber = 3
EndNumber = 10000

while(CurrentNumber <= EndNumber):
    #Calculate Square root of CurrentNumber
    SqrtCurNum = m.sqrt(CurrentNumber)

    #Our factor check control
    HasFactors = False
    
    #Iterate through the PrimeNumbers list
    for n in PrimeNumbers:
        #If CurrentNumber modulated by n is zero, then n is a factor of CurrentNumber.
        #   If this is the case, then CurrentNumber is not prime. Mark as such and stop checking.
        if((CurrentNumber % n) is 0):
            HasFactors = True
            break;

        #Only need to check up to the square root of CurrentNumber
        if (n > SqrtCurNum):
            break

    #If no factors were found, append CurrentNumber to the PrimeNumbers list.
    if(HasFactors is False):
        PrimeNumbers.append(CurrentNumber)
        print(CurrentNumber) #The comma allows more text to be printed on the same line.

    #Increase CurrentNumber
    CurrentNumber += 1

#Finally, print the total number of primes found
TotalNumberPrimes = len(PrimeNumbers)
print('Total prime numbers found: ' + str(TotalNumberPrimes))

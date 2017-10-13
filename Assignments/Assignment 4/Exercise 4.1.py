#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 4.1
#
# Usage: python "Exercise 4.1.py"
#
# Description: Calculates the factorial for a user-given number.
#
# Inputs: User input - number to calculate factorial for.
#
# Outputs: Console data - factorial for given number.
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
# --- Exercise 4.1 ---

#Calculate the factorial using integers numbers.
def FactorialInt(number):
    FinalValue = int(number)
    for n in range((number-1), 1, -1):
        FinalValue *= int(n)
        #print('DBG: n={0} && FinalValue={1}'.format(n, FinalValue))
    
    return FinalValue

#Calculate the factorial using floating point numbers.
def FactorialFloat(number):
    FinalValue = float(number)
    for n in range((number-1), 1, -1):
        FinalValue *= float(n)
        #print('DBG: n={0} && FinalValue={1}'.format(n, FinalValue))
    
    return FinalValue

#Get user input, raw - not casted to float or int.
Input = input('Enter a number to calculate a factorial for: ')

#Get factorial for input as an int and float.
print('Factorial for int({0}) is: {1}'.format(int(Input), FactorialInt(Input)))
print('Factorial for float({0}) is: {1}'.format(float(Input), FactorialFloat(Input)))
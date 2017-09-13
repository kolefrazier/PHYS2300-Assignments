#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.7
#
# Usage: Calculate Catalan numbers
#
# Description: This program will calculate a list of Catalan numbers that are
#   less than or equal to one billion.
#
# Inputs: None
#
# Outputs: List of numbers (integers) in the Catalan sequence.
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
def NextCatalanNumber(n, Cn):
    #print('[DEBUG] Given: n: {0} and Cn: {1}\t\t'.format(n, Cn)),
    return (((4*n) + 2)/(n + 2))*Cn

#Helper variables
#   Cn = The current Catalan number at position 'n'
#   n = the positional counter for the Catalan number sequence.
#
#   Numbers are set with decimals to enforce float math instead of int math
Cn = 1.0        #Initialize Current as C0, or, 1.
n = 0.0         #Output variable, simply the number in the series.
OneBillion = 1000000000.0 #Comma'd: 1,000,000,000 #For readability

#Calculate and print all Catalan numbers that are <= OneBillion
while(Cn <= OneBillion):
    Cn = NextCatalanNumber(n, Cn)
    print('[C{0}]\t{1}'.format(int(n), Cn)) #Cast n as int, as we don't care about number "C1.2", etc.
    n += 1
    
    

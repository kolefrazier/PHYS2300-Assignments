#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.1 - Another ball dropped from a tower
#
# Usage: Calculates time a dropped object takes to hit the ground.
#
# Description: Calculates the time it takes for a ball to hit the ground
#   when dropped from a user-entered height.
#
# Inputs: Height (number) which the ball is dropped from.
#
# Outputs: Time taken to hit the ground.
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

#Function to calculate height of an object based on time
def CalculateHeight(time):
    #Taken from the book on page 28, s=(1/2)gt^2
    #   This represents how far an object (the ball in this case) falls in the given time.
    return 9.81*time**2/2

#Get user input for height of tower
Height = float(input("Enter the height (in meters) of the tower: "))

#Time Variables
Time = 0 #CurrentTime
TimeStep = 0.1 #Amount to increment time per loop

while(True):
    #Calculate the height
    Height -= CalculateHeight(Time)

    #Debug printout
    print('Current height: {0} at {1} seconds.'.format(Height, Time))

    #Check if height is at or below zero.
    #   If so, print the results and break.
    if (Height <= 0):
        print('The ball hit the ground at {0} seconds.'.format(Time))
        break

    #Finally, increase time for the next iteration
    Time += TimeStep



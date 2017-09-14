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
# Version: 2.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------
import math as m

#Get user input for height of tower
#   In kinematic equations, this will be treated as the total distance, or 'y'.
Height = float(input("Enter the height (in meters) of the tower: "))

#Calculate final velocity based on known information:
#   y0 = 0, v0 = 0, y = Height
# v^2 = v0^2 + 2(y-y0) => v = sqrt(v0^2 + 2(y-y0)) = FinalVelocity
InitialVelocity = 0.0 #Enforce floating point math instead of truncating-int math.
InitialHeight = 0.0
GravityAcceleration = 9.8

FinalVelocity = m.sqrt((InitialVelocity**2)+2*(Height-InitialHeight))

#Now calculate time
#   From: v=v0+at, we can see that t=(v-v0)/a
#       Or, Time = (FinalVelocity-InitialVelocity)/GravityAcceleration
Time = (FinalVelocity-InitialVelocity)/GravityAcceleration

#Print out the result.
print('Falling from {0} meters, the ball hits the ground moving at {1} m/s after {2} seconds have passed'.format(Height, FinalVelocity, Time))



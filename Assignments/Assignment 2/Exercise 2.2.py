#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.2 - Altitude of a satellite
#
# Usage: Calculate the altitude of an orbiting object based on its orbit time.
#
# Description: Calculates the altitude of an object orbiting Earth based on the
#   time it takes to complete one orbit.
#
# Inputs: Time of one orbit.
#
# Outputs: Orbiting altitude of the object.
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

Time = float(input('Enter time (in seconds) for one orbit: '))

#Constants
Pi = 3.14
Gravity = 6.67*(10**-11)    #Newton's gravitational constant
Mass = 5.97*10**24          #Mass of the Earth
Radius = 6371.0 * 1000.0    #Earth's radius (in KM) converted to meters (km*1000)

#Note: The cube root had to be set as a float to prevent integer math.
Height = ((Gravity*Mass*(Time**2))/(4*(Pi**2)))**(1.0/3.0) - Radius

print('The altitude is: {0} meters'.format(Height))

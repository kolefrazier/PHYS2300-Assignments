#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 2.6 - Planetary Orbits
#
# Usage: Calculate information for planetary orbits
#
# Description: Given basic information about an orbiting body, calculate the
#   planetary orbit information for said orbiting body and a second object that
#   is orbiting around the first body.
#
# Inputs: Distance to the Sun (length) and velocity at perihelion.
#
# Outputs: The second orbiting body's distance to the sun (L2) and velocity (v2)
#   of the second body, the Orbital period (T) and the orbital eccentricity (e)
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

#Get user input for Object 1
L1 = float(input('Enter distance to the sun: '))
v1 = float(input('Enter velocity at perihelion: '))

#Constants and necessary values
G = 6.6738*10**-11 #Gravitational Constant
M = 1.9891*10**30  #Mass of the Sun
Pi = 3.141         #Pi

#For Object 2, calculate its velocity (V2) then distance to the Sun (L2)
v2 = -v1**2 + ((2*G*M)/L1) #Pretty sure this isn't right, but I cannot find anything to correct this.
L2 = (L1*v1)/v2
print('v2: {0}\tL2: {1}'.format(v2, L2))

#Calculate T and e using a and b
a = (0.5)*(L1+L2)       #Semi-major axis
b = (L1*L2)**(1.0/2.0)   #Semi-minor axis
T = (2*Pi*a*b)/(L1*v1)  #Orbital period
e = (L2 - L1)/(L2 + L1) #Orbital eccentricity

print('T: {0}\te:{1}'.format(T,e))




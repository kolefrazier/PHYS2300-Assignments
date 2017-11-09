#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Assignment06
#
# Usage: python "Assignment06.py"
#
# Description: Simulates a swinging pendulum.
#
# Inputs: None
#
# Outputs: Visual simulation
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
#--------------------------------------------------------------------------------

from visual import *
from numpy import *

def getTorque(theta):
    return -1.0 * L * m * g * sin(theta)

def momentInertia(m, L): #I
    return m*(L**2)

def angularAcceleration(theta)

def damping(theta):
    reutnr -1*(g/L)*sin(theta)-

#Simulation constants
g = 9.8     #Gravity
L = 1.0     #Bar length, meters
DBar = 0.1  #Bar diameter
DBall = 0.5 #Ball diameter
MBall = 3.0 #Ball mass
A = 

c = 1.0
w = 1.0

#Positional Vals
x = 0
y = 0
z = 0

#Setup Shapes
bar = cylinder(pos=vector(0,0,0), radius = DBar, color=color.yellow)

while True:
    rate(60)

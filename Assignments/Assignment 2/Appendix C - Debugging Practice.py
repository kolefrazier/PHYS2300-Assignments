#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Appendix C - Debugging Practice
#
# Usage: Calculate the trajectory of an object.
#
# Description: This program is intended to calculate and plot the trajectory
#   of a thrown/launched object. However, it is riddled with bugs.
#
# Inputs: None
#
# Outputs: A graph of the trajectory information.
#
# Auxiliary Files:
#
# Special Instructions:
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
#
# Version: 2.0
#
#--------------------------------------------------------------------------------
# Bug Fixes
#--------------------------------------------------------------------------------
#--Syntax Errors--
#   Variable ay has a random period after its assigned value (-9.8.). Removed this random period. (-9.8)
#   The for loop calls function p(), but only px() is defined. Changed function definition to position()
#       as Y-values are being calculated, too.
#
#--Runtime Errors--
#   The y-check in the for loop creates an index out of bounds. See Logic Errors for the resolution to this.
#
#--Logic Errors--
#   The X-axis is labeled as Time but is being filled with position(x0,vx0,t,ax)). Changed it to fill with the current time.
#   Changed coordinate-calculation loop to break if the Y position is less-than zero.
#       Also changed this to only add X and Y coordinates to their respective lists if the calculated
#       Y-position is not less than zero.
#
#--Other Fixes--
#   Updated all variable names to be more verbose about their purpose and consistently 
#--------------------------------------------------------------------------------

import numpy as np
import math as m
from visual.graph import *

def position(x,v,t,a):
    return x + v*t + 0.5*a*t**2

xInitial = 1.0
xVelocityInitial = 70.0

yInitial = 0.0
yVelocityInitial = 80.0

xAcceleration = 0.0
yAcceleration = -9.8

timeDelta = 0.1
time = 0.0

xCoordinates = []
yCoordinates = []

plotWindow = gdisplay(xtitle="Time", ytitle="Y Position")

for i in range(170):
    newYPosition = position(yInitial,yVelocityInitial,time,yAcceleration)
    if(newYPosition < 0.0):
        break
    else:
        xCoordinates.append(time)
        yCoordinates.append(newYPosition)
        
    time = time + timeDelta    
    
plot = gcurve(color=color.cyan)
for j in range(len(xCoordinates)):
    plot.plot(pos=(xCoordinates[j], yCoordinates[j]))

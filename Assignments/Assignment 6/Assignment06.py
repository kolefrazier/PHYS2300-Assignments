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
from numpy import sin, cos

def momentInertia(m, L): #I
    return m*(L**2)

def angularAcceleration(theta): #alpha
    return -g/L*sin(theta)

def getDampedOn(a, w):
    return a-(c*w)

def angularVelocity(a, t): #w=w0+angularAccel*t => w += (a*t)
    return a*t

def DThetaDT(theta, t):
    acceleration = angularAcceleration(theta)
    dampedVelocity = angularVelocity(w0, a, t) #* c
    frequency = A*sin(f*t)
    return accel - dampedVelocity + frequency

#def rk4():
    

#Simulation constants
g = 9.8         #Gravity
L = 1.0         #Bar length, meters
DBar = 0.05     #Bar diameter
DBall = 0.5     #Ball diameter
MBall = 3.0     #Ball mass
A = .1          #Natural Frequency Coefficient (?? - Just given as a variable in the text)
f = 2.0/3.0     #Frequency
c = 1.0         #Damping Coefficient
theta = 2.0 * pi / 3.0  #Starting Theta
Velocity = 0.0          #Starting Velocity

#Initial Positional Values
x = 0
y = 0
z = 0

#Time
TStart = 0
TEnd = 50
TStep = 0.01

xPoints = []
yPoints = []
zPoints = []
vPoints = []
tPoints = arange(TStart, TEnd, TStep)

#Setup Shapes
bar = cylinder(pos=array([0,0,0]), radius = DBar, color=color.yellow)
bar.axis = (L*sin(theta), -L*cos(theta),0)

for t in tPoints:
    rate(60)

    #Log current coordinates
    xPos = L*sin(theta)
    yPos = -L*cos(theta)
    zPos = 0
    xPoints.append(xPos)
    yPoints.append(yPos)
    zPoints.append(zPos)

    #Calculate new acceleration, apply damping
    newAccel = angularAcceleration(theta)
    newAccel -= c*Velocity

    #Calculate velocity
    Velocity += (newAccel * TStep) #V = V0 + at => v += at
    
    #Calculate new Theta
    theta += Velocity * TStep

    #Update pendulum visual position
    bar.axis = (L*sin(theta), -L*cos(theta),0)




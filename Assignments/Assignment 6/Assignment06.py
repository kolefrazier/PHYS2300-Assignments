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
# Outputs: Visual simulation and live-generated graph
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
from visual.graph import *
from numpy import sin, cos

def momentInertia(m, L): #I
    return m*(L**2)

def angularAcceleration(theta): #alpha
    return -g/L*sin(theta)

def getDampedOn(a, w, c):
    return a-(c*w)

def angularVelocity(a, t): #w=w0+angularAccel*t => w += (a*t)
    return a*t

#def rk4():
    

#Simulation constants
g = 9.8         #Gravity
L = 1.0         #Bar length, meters
DBar = 0.03     #Bar diameter
RBall = 0.12    #Ball radius
MBallOne = 3.0  #Ball mass
MBallTwo = 3.0     
A = .1          #Natural Frequency Coefficient (?? - Just given as a variable in the text)
f = 2.0/3.0     #Frequency
cOne = 0.3        #Damping Coefficient
cTwo = 0.5
thetaOne = 2.0 * pi / 3.0  #Starting Theta
thetaTwo = 1.5 * pi / 4.0  
VelocityOne = momentInertia(MBallOne, L) #Starting Velocity
VelocityTwo = momentInertia(MBallTwo, L)

#Initial Positional Values
x = 0
y = 0
z = 0

#Time
TStart = 0
TEnd = 30
TStep = 0.01
tPoints = arange(TStart, TEnd, TStep)

#Setup Shapes
ceiling = box(pos=(0,0,0), size=(0.4, 0.02, 0.4), color=color.red)
barOne = cylinder(pos=(0,0,0), radius = DBar, color=color.yellow)
barOne.axis = (L*sin(thetaOne), -L*cos(thetaOne),0)
ballOne = sphere(pos=(barOne.axis), color=barOne.color, radius=RBall)

barTwo = cylinder(pos=(0,0,0), radius = DBar, color=color.green)
barTwo.axis = (L*sin(thetaTwo), -L*cos(thetaTwo),0)
ballTwo = sphere(pos=(barTwo.axis), color=barTwo.color, radius=RBall)

#Start Plots
Plot1 = gcurve(color=barOne.color)
Plot2 = gcurve(color=barTwo.color)

#Start the simulation
for t in tPoints:
    rate(60)

    #---------- Bar 1 ----------
    #Plot current coordinates
    Plot1.plot(pos=(t, VelocityOne))

    #Calculate new acceleration, apply damping, apply driving term
    newAccel = angularAcceleration(thetaOne)
    newAccel -= cOne*VelocityOne
    newAccel += A*sin(f*t)

    #Calculate velocity
    VelocityOne += (newAccel * TStep) #V = V0 + at => v += at
    
    #Calculate new Theta
    thetaOne += VelocityOne * TStep

    #Update objects visual position
    barOne.axis = (L*sin(thetaOne), -L*cos(thetaOne),0)
    ballOne.pos = barOne.axis

    #---------- Bar 2 ----------
    #Plot current coordinates
    Plot2.plot(pos=(t, VelocityTwo))

    #Calculate new acceleration, apply damping, apply driving term
    newAccel = angularAcceleration(thetaTwo)
    newAccel -= cTwo*VelocityTwo
    newAccel += A*sin(f*t)

    #Calculate velocity
    VelocityTwo += (newAccel * TStep) #V = V0 + at => v += at
    
    #Calculate new Theta
    thetaTwo += VelocityTwo * TStep

    #Update objects visual position
    barTwo.axis = (L*sin(thetaTwo), -L*cos(thetaTwo),0)
    ballTwo.pos = barTwo.axis

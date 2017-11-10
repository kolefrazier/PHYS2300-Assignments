#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Assignment06
#
# Usage: python "Assignment06.py"
#
# Description: Simulates a set of damped pendulums
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

def angularVelocity(a, t): #w=w0+angularAccel*t => w += (a*t)
    return a*t

def rk4(r, t):
    #Acceleration
    newAccel = angularAcceleration(thetaOne)
    newAccel -= cOne*VelocityOne
    newAccel += A*sin(f*t)
    #Velocity
    newVeloc = r[1]
    newVeloc += (newAccel * TStep)
    return array([newAccel, newVeloc], float)

#Simulation constants
g = 9.8         #Gravity
L = 1.0         #Bar length, meters - used for both pendulums
DBar = 0.03     #Bar diameter - used for both pendulums
RBall = 0.12    #Ball radius - used for both pendulums
MBallOne = 3.0  #Ball masses
MBallTwo = 3.0     
A = .1          #Natural Frequency Coefficient (?? - Just given as a variable in the text)
f = 2.0/3.0     #Frequency - used for both pendulums
cOne = 0.3      #Damping Coefficients
cTwo = 0.5
thetaOne = 2.0 * pi / 3.0  #Starting Thetas
thetaTwo = 1.5 * pi / 4.0
VelocityOne = momentInertia(MBallOne, L) #Starting Velocities
VelocityTwo = momentInertia(MBallTwo, L)

#Time
TStart = 0
TEnd = 100
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
PlotDisplay = gdisplay(title='Angular Position vs Velocity', xtitle='Angular Position (theta)', ytitle='Velocity (v)')
Plot1 = gcurve(color=barOne.color)
Plot2 = gcurve(color=barTwo.color)

#[Velocity, Acceleration]
r1 = array([1.0, VelocityOne], float)
r2 = array([1.0, 1.0], float)
h = TStep

#Start the simulation
for t in tPoints:
    rate(60)

    #---------- Bar 1 ----------
    #Plot current coordinates
    #Plot1.plot(pos=(t, VelocityOne)) #Velocity versus time
    Plot1.plot(pos=(thetaOne, VelocityOne)) #Angular position versus velocity

##    k1 = h*rk4(r1, t)
##    k2 = h*rk4(r1+0.5*k1, t+0.5*h)
##    k3 = h*rk4(r1+0.5*k2, t+0.5*h)
##    k4 = h*rk4(r1+k3, t+h)
##    r1 += (k1 + 2*k2 + 2*k3 + k4)/6
##
##    #newAccel = r1[0]
##    VelocityOne = r1[1]

    #Calculate new acceleration, apply damping, apply driving term
    newAccel = angularAcceleration(thetaOne)
    newAccel -= cOne*VelocityOne
    newAccel += A*sin(f*t)

    #Calculate velocity
    VelocityOne += (newAccel * TStep) #V = V0 + at => v += at
    
    #Calculate new Theta
    thetaOne += VelocityOne * TStep
    #thetaOne += r1[1] * TStep

    #Update objects visual position
    barOne.axis = (L*sin(thetaOne), -L*cos(thetaOne),0)
    ballOne.pos = barOne.axis

    #---------- Bar 2 ----------
    #Plot current coordinates
    #Plot2.plot(pos=(t, VelocityTwo)) #Velocity versus time
    Plot2.plot(pos=(thetaTwo, VelocityTwo)) #Angular position versus velocity

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

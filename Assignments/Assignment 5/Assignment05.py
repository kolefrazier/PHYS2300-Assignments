#Assignment05
from visual import *
import math as m
import numpy

def acceleration(F, m):
    return (F/m)

def velocity(v0, a, t0, t):
    #v=v0+a*DeltaT
    return (v0 + a*(t-t0))

def position(x0, v, t0, t):
    #x = x0 + v*DeltaT
    return (x0 + v*(t-t0))

def airResistance(v, A):
    p = 0.0 #air density
    cd = 0.5 #drag coefficient, 0.5 is a recommended estimate
    F = -(1.0/2.0)*p*v*cd*A*v

    return F

#Get user inputs
print('--- Initial Positional Values ---')
x = float(input('Enter initial X: '))
y = float(input('Enter initial Y: '))
z = float(input('Enter initial Z: '))


print('--- Initial Velocity Values ---')
vx = float(input('Enter initial VX: '))
vy = float(input('Enter initial VY: '))
vz = float(input('Enter initial VZ: '))

print('--- Other Values ---')
timeStep = float(input('Enter time step: '))
timeRun = int(input('Enter simulation run length (whole seconds): '))

#Establish other values
gravitationalAcceleration = vector(0, -9.8, 0)

#Setup visual aspects
scene = display(title='Velocity of an un-air-laden ball versus an air-laden ball')
ballNoDrag = sphere(pos = (x,y,z), radius=0.5, color=color.green)
ballNoDrag.velocity = vector(vx, vy, vz)

ballAirDrag = sphere(pos = (x,y,z), radius=0.5, color=color.blue)
ballAirDrag.velocity = vector(vx, vy, vz)

t0 = 0
for t in numpy.arange(0, timeRun, timeStep):
    rate(5000)
    
    ballNoDrag.velocity = ballNoDrag.velocity + gravitationalAcceleration * timeStep
    ballNoDrag.pos = ballNoDrag.pos = ballNoDrag.velocity * timeStep

#def position(x0, v, t0, t):
    if(ballNoDrag.pos.y > 0):
        ballNoDrag.pos.x = position(ballNoDrag.pos.x, ballNoDrag.velocity.x, t0, t)
        ballNoDrag.pos.y = position(ballNoDrag.pos.y, ballNoDrag.velocity.y, t0, t)
        ballNoDrag.pos.z = position(ballNoDrag.pos.z, ballNoDrag.velocity.z, t0, t)

    #Store the previous time to assist in calculating DeltaT.
    t0 = t

#Assignment05
from visual import *
import math as m
import numpy

def acceleration(F, m):
    return (F/m)

def velocity(v0, a, t0, t):
    #v=v0+a*DeltaT
    print('\tVelocity: v0:{0} a:{1} t0:{2} t:{3}'.format(v0, a, t0, t))
    return (v0 + a*(t-t0))

def position(x0, v, t0, t):
    #x = x0 + v*DeltaT
    return (x0 + v*(t-t0))

def crossSectionalArea(radius):
    return m.pi * radius**2

def airResistance(v, A):
    p = 0.0 #air density
    cd = 0.5 #drag coefficient, 0.5 is a recommended estimate
    F = -(1.0/2.0)*p*v*cd*A*v

    return F

#Get user inputs
print('--- Initial Positional Values ---')
x = float(input('Enter initial X-Position: '))
y = float(input('Enter initial Y-Position: '))
z = float(input('Enter initial Z-Position: '))


print('\n--- Initial Velocity Values ---')
vx = float(input('Enter initial X-Velocity: '))
vy = float(input('Enter initial Y-Velocity: '))
vz = float(input('Enter initial Z-Velocity: '))

print('\n--- Other Values ---')
timeRun = int(input('Enter simulation run length (whole seconds): '))
timeStep = float(input('Enter time step: '))


#Establish other values
gravitationalAcceleration = -9.8

#Setup visual aspects
scene = display(title='Thrown Ball - Air Drag and No Air Drag')
ballNoDrag = sphere(pos = (x,y,z), radius=0.5, color=color.green)
ballNoDrag.velocity = vector(vx, vy, vz)
ballNoDrag.trail = curve(color=ballNoDrag.color)

ballAirDrag = sphere(pos = (x,y,z), radius=0.5, color=color.blue)
ballAirDrag.velocity = vector(vx, vy, vz)
ballAirDrag.trail = curve(color=ballAirDrag.color)

t0 = 0
t = 0
#for t in numpy.arange(0, timeRun, timeStep):
while(t <= timeRun):
    rate(100)
    print('Time: ' + str(t))
    
    #ballNoDrag.velocity = ballNoDrag.velocity + gravitationalAcceleration * timeStep
    #ballNoDrag.pos = ballNoDrag.pos = ballNoDrag.velocity * timeStep

    if(ballNoDrag.pos.y >= 0): #Allows for y=0 to allow for starting position = 0.
        #Calculate velocity changes first
        #   def velocity(v0, a, t0, t):
        ballNoDrag.velocity.x = velocity(ballNoDrag.velocity.x, 0, t0, t)
        ballNoDrag.velocity.y = velocity(ballNoDrag.velocity.y, gravitationalAcceleration, t0, t)
        ballNoDrag.velocity.z = velocity(ballNoDrag.velocity.z, 0, t0, t)
        print('BallND.vel = ' + str(ballNoDrag.velocity))
        
        #Calculate position changes second
        #   def position(x0, v, t0, t):
        ballNoDrag.pos.x = position(ballNoDrag.pos.x, ballNoDrag.velocity.x, t0, t)
        ballNoDrag.pos.y = position(ballNoDrag.pos.y, ballNoDrag.velocity.y, t0, t)
        ballNoDrag.pos.z = position(ballNoDrag.pos.z, ballNoDrag.velocity.z, t0, t)
        print('BallND.pos = ' + str(ballNoDrag.pos))

        #Update trail
        ballNoDrag.trail.append(pos=ballNoDrag.pos)

    #Store the previous time to assist in calculating DeltaT.
    t0 = t
    t += timeStep

print ('Completed!')

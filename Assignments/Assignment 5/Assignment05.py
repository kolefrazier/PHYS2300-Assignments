#Assignment05
from visual import *
import math as m
import numpy

def velocity(v0, a, t0, t):
    #v=v0+a*DeltaT
    return (v0 + a*(t-t0))

def position(x0, v, t0, t):
    #x = x0 + v*DeltaT
    return (x0 + v*(t-t0))

def crossSectionalArea(radius):
    return m.pi * radius**2.0

def airResistance(v, A):
    p = 1.225 #air density, ~1.225 kg/m^3 at sea level according to Wikipedia
    cd = 0.5 #drag coefficient, 0.5 is a recommended estimate
    F = -(1.0/2.0)*p*v*cd*A*v
    return F

#Get user inputs
print('--- Initial Positional Values ---')
print('(Lowest starting position can be (0,0,0))')
x = float(input('Enter initial X-Position: '))
y = float(input('Enter initial Y-Position: '))
z = float(input('Enter initial Z-Position: '))


print('\n--- Initial Velocity Values ---')
print('(Decent sized numbers work much better! >= 15)')
vx = float(input('Enter initial X-Velocity: '))
vy = float(input('Enter initial Y-Velocity: '))
vz = float(input('Enter initial Z-Velocity: '))

print('\n--- Other Values ---')
timeRun = int(input('Enter simulation run length (whole seconds): '))
timeStep = float(input('Enter time step: '))

#Establish other values
gravitationalAcceleration = -9.8

#Setup visual aspects
scene = display(title='Projectiles and Air Drag')
#scene.background(src='clouds.jpeg') #http://vpython.org/contents/docs/materials.html
ballNoDrag = sphere(pos = (x,y,z), radius=0.5, color=color.green)
ballNoDrag.velocity = vector(vx, vy, vz)
ballNoDrag.trail = curve(color=ballNoDrag.color)

ballAirDrag = sphere(pos = (x,y,z), radius=0.5, color=color.red)
ballAirDrag.velocity = vector(vx, vy, vz)
ballAirDrag.trail = curve(color=ballAirDrag.color)
ballADCrossSectionalArea = crossSectionalArea(ballAirDrag.radius)

scene.visible = True
scene.autocenter = True
scene.autoscale = True

t0 = 0.0
t = 0.0
#for t in numpy.arange(0, timeRun, timeStep):
while(t <= timeRun):
    rate(100)
    
    #ballNoDrag.velocity = ballNoDrag.velocity + gravitationalAcceleration * timeStep
    #ballNoDrag.pos = ballNoDrag.pos = ballNoDrag.velocity * timeStep

    #Allows for y=0 to allow for starting position = 0.
    #Then, as soon as the ball impales itself into the ground (Y<0), it stops.
    #This also prevents balls that are stuck into the ground from being kicked out of the ground
    if(ballNoDrag.pos.y >= 0): 
        #Calculate velocity changes
        ballNoDrag.velocity.x = velocity(ballNoDrag.velocity.x, 0, t0, t)
        ballNoDrag.velocity.y = velocity(ballNoDrag.velocity.y, gravitationalAcceleration, t0, t)
        ballNoDrag.velocity.z = velocity(ballNoDrag.velocity.z, 0, t0, t)
        
        #Calculate position changes
        ballNoDrag.pos.x = position(ballNoDrag.pos.x, ballNoDrag.velocity.x, t0, t)
        ballNoDrag.pos.y = position(ballNoDrag.pos.y, ballNoDrag.velocity.y, t0, t)
        ballNoDrag.pos.z = position(ballNoDrag.pos.z, ballNoDrag.velocity.z, t0, t)

        #Update trail
        ballNoDrag.trail.append(pos=ballNoDrag.pos)

    if(ballAirDrag.pos.y >= 0):
        #Calculate air drag
        xDrag = airResistance(ballAirDrag.velocity.x, ballADCrossSectionalArea)
        yDrag = airResistance(ballAirDrag.velocity.y, ballADCrossSectionalArea)
        zDrag = airResistance(ballAirDrag.velocity.z, ballADCrossSectionalArea)
        #print('AIR\tX:{0} || Y:{1} || Z:{2}'.format(xDrag, yDrag, zDrag))
        
        #Calculate velocity changes
        ballAirDrag.velocity.x = velocity(ballAirDrag.velocity.x, 0 + xDrag, t0, t)
        ballAirDrag.velocity.y = velocity(ballAirDrag.velocity.y, gravitationalAcceleration + yDrag, t0, t)
        ballAirDrag.velocity.z = velocity(ballAirDrag.velocity.z, 0 + zDrag, t0, t)
        
        #Calculate position changes
        ballAirDrag.pos.x = position(ballAirDrag.pos.x, ballAirDrag.velocity.x, t0, t)
        ballAirDrag.pos.y = position(ballAirDrag.pos.y, ballAirDrag.velocity.y, t0, t)
        ballAirDrag.pos.z = position(ballAirDrag.pos.z, ballAirDrag.velocity.z, t0, t)

        #Update trail
        ballAirDrag.trail.append(pos=ballAirDrag.pos)

    #Store the previous time to assist in calculating DeltaT.
    t0 = t
    t += timeStep

print ('Completed!')
print ('Final positions:\n\tNo air drag: {0}\n\tYes air drag: {1}'.format(str(ballNoDrag.pos), str(ballAirDrag.pos)))

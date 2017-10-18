#Assignment05
from visual import *
import math as m

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
timeRun = float(input('Enter simulation run length: '))

#Establish other values
gravitationalAcceleration = vector(0, -9.8, 0)

#Setup visual aspects
scene = display(title='Velocity of an un-air-laden ball versus an air-laden ball')
ballNoDrag = sphere(pos = (x,y,z), radius=0.5, color=color.green)
ballNoDrag.velocity = vector(vx, vy, vz)

ballAirDrag = sphere(pos = (x,y,z), radius=0.5, color=color.blue)
ballAirDrag.velocity = vector(vx, vy, vz)

for t in range(0, timeRun, timeStep):
    rate(5000)
    
    ballNoDrag.velocity = ballNoDrag.velocity + gravitationalAcceleration * timeStep
    ballNoDrag.pos = ballNoDrag.pos = ballNoDrag.velocity * timeStep
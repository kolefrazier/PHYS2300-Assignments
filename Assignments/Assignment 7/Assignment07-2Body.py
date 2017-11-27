import sys
import numpy as np
from visual import *

# ---------- Body Class ----------
#Class: Body extends vpython's sphere
#   Assists in data containment for ease in data management.
#   Managing multiple arrays of associated data manually just isn't
#     good practice when concepts to handle associated data - such as OOP - exist.
class Body(sphere):
    def __init__(self, name='', mass=1.1, radius=10.0, velocity=vector(0.0, 0.0, 0.0), acceleration=vector(0.0, 0.0, 0.0), position=vector(1.0, 1.0, 1.0), color=color.white, makeTrail=True, trailRetain=1500):
        self.name = name
        self.mass = mass
        self.acceleration = acceleration
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity, color=color, make_trail=makeTrail, retain=trailRetain)

    def PrintDetails(self):
        print '[{0}]\n\tMass: {1}\n\tAccel: {2}\n\tVeloc: {3}\n\tpos: {4}'.format(self.name, str(self.mass), str(self.acceleration), str(self.velocity), str(self.pos))

# ---------- Body Instantiation Functions ----------
def GetEarth():
    return Body(name='Earth', radius=10000, mass=5.97e24, velocity=vector(0.0, 3.0e4, 0.0), position=vector(1.5e11, 0.0, 0.0), color=BodyColors['Earth+Moon barycenter'])

def GetSun():
    return Body(name='Sun', radius=10000000, mass=1.99e30, velocity=vector(0.0, 0.0, 0.0), position=vector(0.0, 0.0, 0.0), color=BodyColors['Sun'], trailRetain=5000)

# ---------- Numerical and Other Constants ----------
G = 6.67e-11
RadiusScale = 10
BodyColors = {'Sun':color.yellow, 'Mercury':color.orange, 'Venus':color.orange, 'Earth+Moon barycenter':color.blue, 'Mars':color.red, 'Jupiter':color.orange, 'Saturn':color.orange, 'Uranus':color.cyan, 'Neptune':color.cyan, 'Pluto':color.magenta}

# ---------- Script Logic (a dirty Main) ----------
# ---------- Process File Input ----------
Bodies = [GetSun(), GetEarth()]

# ---------- Other VPython and Main-Loop Stuff ----------
scene = display(title='2-Body Simulation', width=600, height=500, visible=True, autoscale=False)
RunTime = 3.15e7 * 3
dt = 6.3e4
CurrentTime = 0.0
print('Beginning simulation. You may need to zoom in (middle house button) to see the some trails (such as the Sun\'s trail)')

# ---------- Simulation Loop ----------
while(CurrentTime <= RunTime):
    rate(60)
    
    for i in Bodies:
        i.acceleration = vector(0.0, 0.0, 0.0)
        for j in Bodies:
            if i != j:
                dist = j.pos - i.pos
                i.acceleration += G * j.mass * dist / mag(dist)**3 
        for i in Bodies:
            i.velocity += i.acceleration * dt   #deltaV1 = A1 * deltaT
            i.pos += i.velocity * dt            #deltaX1 = V1 * deltaT
     
    CurrentTime += dt

print('--- Finished! ---')



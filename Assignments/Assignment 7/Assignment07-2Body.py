import sys
import numpy as np
from visual import *

# ---------- Body Class ----------
#Class: Body extends vpython's sphere
#   Assists in data containment for ease in data management,
#     because there is no way in hell that managing multiple
#     arrays of associated data is reasonable.
class Body(sphere):
    def __init__(self, name='', mass=1.1, radius=10.0, velocity=vector(0.0, 0.0, 0.0), acceleration=vector(0.0, 0.0, 0.0), position=vector(1.0, 1.0, 1.0), color=color.white):
        self.name = name
        self.mass = mass
        self.acceleration = acceleration
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity, color=color, make_trail=True, retain=5000)

    def PrintDetails(self):
        print '[{0}]\n\tMass: {1}\n\tAccel: {2}\n\tVeloc: {3}\n\tpos: {4}'.format(self.name, str(self.mass), str(self.acceleration), str(self.velocity), str(self.pos))

# ---------- Body Instantiation Functions ----------
def GetEarth():
    return Body(name='Earth', radius=10, mass=5.97e24, velocity=vector(0.0, 3.0e4, 0.0), position=vector(0.0, 0.0, 0.0), color=BodyColors['Earth+Moon barycenter'])

def GetSun():
    return Body(name='Sun', radius=10, mass=1.99e30, velocity=vector(0.0, 0.0, 0.0), position=vector(0.0, 0.0, 0.0), color=BodyColors['Sun'])

# ---------- Numerical and Other Constants ----------
G = 6.67e-11
RadiusScale = 10
BodyColors = {'Sun':color.yellow, 'Mercury':color.orange, 'Venus':color.orange, 'Earth+Moon barycenter':color.blue, 'Mars':color.red, 'Jupiter':color.orange, 'Saturn':color.orange, 'Uranus':color.cyan, 'Neptune':color.cyan, 'Pluto':color.magenta}

# ---------- Script Logic (a dirty Main) ----------
# ---------- Process File Input ----------
Bodies = [GetSun(), GetEarth()]

# ---------- Other VPython and Main-Loop Stuff ----------
scene = display(title='2-Body Simulation', width=600, height=500, visible=True, show_rendertime=True, autoscale=False)
RunTime = 3.15e7
TimeChange = 6.3e4
CurrentTime = 0

# ---------- Simulation Loop ----------
while(CurrentTime <= RunTime):
#for dt in arange(0, RunTime, TimeStep):
#for dt in np.linspace(0, RunTime, TimeChange):
    rate(3600)

    if CurrentTime == 0:
        dt = 0
    else:
        dt = TimeChange
    
    for i in Bodies:
        i.acceleration = vector(0,0,0)
        for j in Bodies:
            if i != j:
                dist = j.pos - i.pos
                i.acceleration = i.acceleration + G * j.mass * dist / mag(dist)**3
        for i in Bodies:
            i.velocity = i.velocity + i.acceleration * dt
            i.pos = i.pos + i.velocity * dt

print('--- Finished! ---')



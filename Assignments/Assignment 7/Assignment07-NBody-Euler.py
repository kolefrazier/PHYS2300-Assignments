#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Assignment07 - N-Body Version
#
# Usage: python "Assignment07-NBody.py"
#
# Description: Simulates an N-Body gravity simulation using the Euler method.
#
# Inputs: File input (see Auxiliary Files field)
#
# Outputs: Visual simulation of N-Body simulation.
#
# Auxiliary Files: planet_data_full.txt
#
# Special Instructions: N/A
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 2.1
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------

import sys
from visual import *

# ---------- Body Class ----------
#Class: Body extends vpython's sphere
#   Assists in data containment for ease in data management.
#   Managing multiple arrays of associated data manually just isn't
#     good practice when concepts to handle associated data - such as OOP - exist.
class Body(sphere):
    def __init__(self, name='', mass=0.0, radius=1000.0, velocity=vector(0.0, 0.0, 0.0), acceleration=vector(0.0, 0.0, 0.0), position=vector(1.0, 1.0, 1.0), color=color.white, makeTrail=True, trailRetain=5000):
        self.name = name
        self.mass = mass
        self.acceleration = acceleration
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity, color=color, make_trail=makeTrail, retain=TrailRetain[name])

    def PrintDetails(self):
        print '[{0}]\n\tMass: {1}\n\tAccel: {2}\n\tVeloc: {3}\n\tpos: {4}'.format(self.name, str(self.mass), str(self.acceleration), str(self.velocity), str(self.pos))

# ---------- IO Functions ----------
def ReadFileData(FileName):
    FileHandle = open(FileName)
    FileData = FileHandle.readlines()
    FileHandle.close()

    return FileData

def InterpretFileData(FileData):
    #File format - Format repeats every ~5 lines
    #PlanetName
    #xPos (AU) yPos (AU) zPos(AU)
    #vX AU/day) vY (AU/Day) vZ(AU/day)
    #Unknown
    #Mass (kg)
    
    DataLength = len(FileData)
    Bodies = []
    
    for i in range (0, DataLength, 5):
        #Get Data
        Name = FileData[i].strip()
        RawPositions = FileData[i+1]
        RawVelocities = FileData[i+2]
        RawUnknownData = FileData[i+3]
        RawMass = FileData[i+4]

        #Process position and velocity data
        PositionsSplit = RawPositions.split(' ')
        #Position = vector(float(PositionsSplit[0]), float(PositionsSplit[1]), float(PositionsSplit[2]))
        Position = vector(float(PositionsSplit[0])*AU, float(PositionsSplit[1])*AU, float(PositionsSplit[2])*AU)

        VelocitiesSplit = RawVelocities.split(' ')
        #Velocity = vector(float(VelocitiesSplit[0]), float(VelocitiesSplit[1]), float(VelocitiesSplit[2]))
        Velocity = vector(float(VelocitiesSplit[0])*AUDay, float(VelocitiesSplit[1])*AUDay, float(VelocitiesSplit[2])*AUDay)

        NewBody = Body(name=Name, radius=10000, mass=float(RawMass), velocity=Velocity, position=Position, color=BodyColors[Name])
        Bodies.append(NewBody)

    return Bodies

# ---------- Misc Body Functions (heh) ----------
def GetSun():
    return Body(name='Sun', radius=5.6378e4*3, mass=1.99e30, velocity=vector(0,0,0), position=vector(0,0,0), color=BodyColors['Sun'])

def DetailBodies(Bodies):
    for b in Bodies:
        b.PrintDetails()

# ---------- Conversion Functions ----------
def SumMasses(Bodies):
    Sum = 0.0
    for b in Bodies:
        Sum += b.mass

    return Sum

def ConvertToCM(MassSum, R):
    return (MassSum * R)

def TwoBodyConvertToCM(Mass1, Mass2, R):
    return (Mass1+Mass2)*R

# ---------- Numerical and Other Constants ----------
G = 6.67e-11
AU = (149.6e6 * 1000)
SingleDay = 24 * 3600 #Seconds in a day
AUDay = AU/SingleDay
BodyColors = {'Sun':color.yellow, 'Mercury':color.orange, 'Venus':color.orange, 'Earth+Moon barycenter':color.blue, 'Mars':color.red, 'Jupiter':color.orange, 'Saturn':color.orange, 'Uranus':color.cyan, 'Neptune':color.cyan, 'Pluto':color.magenta}
TrailRetain = {'Sun':20000, 'Mercury':2000, 'Venus':2000, 'Earth+Moon barycenter':2000, 'Mars':2500, 'Jupiter':20000, 'Saturn':20000, 'Uranus':50000, 'Neptune':50000, 'Pluto':50000}


# ---------- Script Logic (A Dirty Main Method) ----------
# ---------- Process File Input, Add Other Bodies ----------
Bodies = InterpretFileData(ReadFileData('planet_data_full.txt'))
Bodies.insert(0, GetSun())

#Convert to center-of-mass coordinates
CenterOfMass = vector(0,0,0)
CenterOfVelocity = vector(0,0,0)
TotalMass = 0.0

for body in Bodies:
    CenterOfMass += (body.pos * body.mass)
    CenterOfVelocity += (body.velocity * body.mass)
    TotalMass += body.mass

CenterOfMass = CenterOfMass / TotalMass

for body in Bodies:
    body.pos -= CenterOfMass

#Print pre-simulation details to console
#DetailBodies(Bodies)

# ---------- Other VPython and Main-Loop Stuff ----------
scene = display(title='N-Body Simulation', width=800, height=800, visible=True, autoscale=False)
RunTime = 2e15 #Some arbitrary run time
dt = 6.3e4
CurrentTime = 0.0
FirstStep = 0

print ('--- Starting Simulation ---')
print ('NOTE: The sun may be difficult to see without a trail. It\'s there - zoom in!')

# ---------- Simulation Loop ----------
while(CurrentTime <= RunTime):
    rate(3600)

    # --- Euler Method ---
    for i in Bodies:
        i.acceleration = vector(0,0,0)
        for j in Bodies:
            if i != j:
                dist = j.pos - i.pos
                i.acceleration = i.acceleration + G * j.mass * dist / mag(dist)**3
        for i in Bodies:
            i.velocity = i.velocity + i.acceleration*dt
            i.pos = i.pos + i.velocity * dt
     
    CurrentTime += dt

print('--- Finished! ---')
DetailBodies(Bodies)



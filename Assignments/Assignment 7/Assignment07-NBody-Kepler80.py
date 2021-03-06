#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Assignment07 - N-Body Version for Kepler 80
#
# Usage: python "Assignment07-NBody-Kepler80.py"
#
# Description: Simulates an N-Body gravity simulation for the exosystem Kepler 80.
#
# Inputs: File input (see Auxiliary Files field)
#
# Outputs: Visual simulation of N-Body simulation.
#
# Auxiliary Files: Kepler80_data.txt
#
# Special Instructions: N/A
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.1
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------
# NOTE: I tried to model this one, but I believe I messed up the data conversions, resulting in a bad model.
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
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity, color=color, make_trail=makeTrail, retain=trailRetain)

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
        Position = vector(float(PositionsSplit[0]), float(PositionsSplit[1]), float(PositionsSplit[2]))

        VelocitiesSplit = RawVelocities.split(' ')
        #Velocity = vector(float(VelocitiesSplit[0]), float(VelocitiesSplit[1]), float(VelocitiesSplit[2]))
        Velocity = vector(float(VelocitiesSplit[0]), float(VelocitiesSplit[1]), float(VelocitiesSplit[2]))

        NewBody = Body(name=Name, radius=10000, mass=float(RawMass), velocity=Velocity, position=Position, color=color.orange)
        Bodies.append(NewBody)

    return Bodies

# ---------- Misc Body Functions (heh) ----------
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

# ---------- Script Logic (A Dirty Main Method) ----------
# ---------- Process File Input, Add Other Bodies ----------
Bodies = InterpretFileData(ReadFileData('Kepler80_data.txt'))

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

    # --- Leap-Frog Method ---
    for i in Bodies:
        i.acceleration = vector(0.0, 0.0, 0.0)
        for j in Bodies:
            if i != j:
                distance = j.pos - i.pos
                i.acceleration += G * j.mass * distance / mag(distance)**3
    if FirstStep == 0:
        for i in Bodies:
            i.velocity += i.acceleration*dt/2.0
            i.pos += i.velocity*dt
        FirstStep = 1
    else:
        for i in Bodies:
            i.velocity += i.acceleration*dt
            i.pos += i.velocity*dt
     
    CurrentTime += dt

print('--- Finished! ---')
DetailBodies(Bodies)



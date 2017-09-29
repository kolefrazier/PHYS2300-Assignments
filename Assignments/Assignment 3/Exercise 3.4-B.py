#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.4-B
#
# Usage: Model an FCC Lattice
#
# Description: Model an front-centerered cubic (fcc) lattice of a singe cube of atoms
#    of a naturally occurring chrystal (such as Sodium Chloride)
#
# Inputs: None
#
# Outputs: None
#
# Auxiliary Files: None
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------


# --- Exercise 3.4-B ---
from visual import *
Distance = 5.0
HalfDist = Distance/2
Radius = 1
CubeSize = vector(5,5,5)

box(pos=vector(0,0,0), size=CubeSize, material=materials.unshaded)

#Cheating the creation of some corner connectors... "Subtracting" (ahem, blacking out) the insides of each face.
box(pos=vector(0,0,0), size=vector(5.001,4,4), color=color.black)
box(pos=vector(0,0,0), size=vector(4,5.001,4), color=color.black)
box(pos=vector(0,0,0), size=vector(4,4,5.001), color=color.black)

#pos=(x,y,z)
GreenSpherePos = [vector(HalfDist, HalfDist, HalfDist), vector(-HalfDist, HalfDist, HalfDist), vector(-HalfDist, -HalfDist, HalfDist), vector(HalfDist, -HalfDist, HalfDist), vector(HalfDist, -HalfDist, -HalfDist), vector(HalfDist, HalfDist, -HalfDist), vector(-HalfDist, HalfDist, -HalfDist), vector(-HalfDist, -HalfDist, -HalfDist)]
PinkSpherePos = [vector(HalfDist, 0, 0), vector(-HalfDist, 0, 0), vector(0, HalfDist, 0), vector(0, -HalfDist, 0), vector(0, 0, HalfDist), vector(0, 0, -HalfDist)]

for shape in GreenSpherePos:
    sphere(pos=shape, radius=Radius, color=color.green)

for shape in PinkSpherePos:
    sphere(pos=shape, radius=Radius, color=color.red)

ConnectorLength = Distance
ConnectorColor = color.blue
ConnectorRadius = 0.125
ConnectorLength = 5

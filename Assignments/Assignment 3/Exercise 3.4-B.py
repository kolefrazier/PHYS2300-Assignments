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

#Simple box to show how each molecule sits on the lattice.
box(pos=vector(0,0,0), size=CubeSize, material=materials.unshaded)

#pos=(x,y,z) - Sphere positions
GreenSpherePos = [vector(HalfDist, HalfDist, HalfDist), vector(-HalfDist, HalfDist, HalfDist), vector(-HalfDist, -HalfDist, HalfDist), vector(HalfDist, -HalfDist, HalfDist), vector(HalfDist, -HalfDist, -HalfDist), vector(HalfDist, HalfDist, -HalfDist), vector(-HalfDist, HalfDist, -HalfDist), vector(-HalfDist, -HalfDist, -HalfDist)]
PinkSpherePos = [vector(HalfDist, 0, 0), vector(-HalfDist, 0, 0), vector(0, HalfDist, 0), vector(0, -HalfDist, 0), vector(0, 0, HalfDist), vector(0, 0, -HalfDist)]

#Graph the spheres
for shape in GreenSpherePos:
    sphere(pos=shape, radius=Radius, color=color.green)

for shape in PinkSpherePos:
    sphere(pos=shape, radius=Radius, color=color.red)



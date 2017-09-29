#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.4-A - Sodium Chloride Lattice
#
# Usage: Model a sodium chloride lattice
#
# Description: Using 3D objects, this program will model a sodium chloride lattice.
#
# Inputs: None
#
# Outputs: 3D model
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


# --- Exercise 3.4-A ---
from visual import *
L = 5
R = 0.3
GreenOrBlue = True

for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if(GreenOrBlue == True):
                sphere(pos=[i,j,k],radius=R, color=color.green)
                GreenOrBlue = False
            else:
                sphere(pos=[i,j,k],radius=R, color=color.blue)
                GreenOrBlue = True
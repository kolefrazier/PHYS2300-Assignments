#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 3.3 - Scanning Tunneling Microscope
#
# Usage: Graph data from a scanning tunneling microscope (STM)
#
# Description: Given a data file from an STM, graph the STM's readings of a silicon surface.
#
# Inputs: File: stm.txt
#
# Outputs: Graph of the STM data
#
# Auxiliary Files: stm.txt
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------
#--- Exercise 3.3 ---
from pylab import imshow, show, gray
from numpy import loadtxt

FileName = 'stm.txt'

data = loadtxt(FileName, float)
imshow(data) #Holy one liners, Batman.
show()
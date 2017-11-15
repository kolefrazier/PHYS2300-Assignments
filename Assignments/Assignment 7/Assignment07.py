from visual import *

def Force(m1, m2, R1, R2):
    R12 = RDelta(R1, R2)
    return (G*m1*m2)/RAbs(R1, R2)**2 * R12

def RDelta(R1, R2):
    deltaX = R2.x - R1.x
    deltaY = R2.y - R1.y
    deltaZ = R2.z - R1.z
    returnVector = vector(deltaX, deltaY, deltaZ)
    return returnVector

def RAbs(R1, R2):
    deltaX = R2.x - R1.x
    deltaY = R2.y - R1.y
    deltaZ = R2.z - R1.z
    PreSquareRoot = deltaX**2 + deltaY**2 + deltaZ**2
    return (PreSquareRoot)**(1/2)

def VDelta(a, t0, t):
    return a * (t - t0)

def Acceleration(m, R1, R2):
    return (G * m / RAbs(R1, R2)**3) * RDelta(R1, R2)



#Constants
G = 1.0

PlanetRadius = 6
StarRadius = 100
RadiusScale = 10

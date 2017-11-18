from visual import *

# ---------- Calculation Functions ----------

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

def XDelta (v, t0, t):
    return v * (t - t0)

def Acceleration(m, R1, R2):
    return (G * m / RAbs(R1, R2)**3) * RDelta(R1, R2)

def VInitial(m1, R1, R2, t, t0):
    a = Acceleration(m1, R1, R2)
    v = v

# ---------- User Input ----------
Mass1 = float(input('Enter Mass 1: '))
Position1 = vector(float(input('Enter X-Pos 1: ')), float(input('Enter Y-Pos 1: ')), float(input('Enter Z-Pos 1: ')))
Velocity1 = vector(float(input('Enter X-Velocity 1: ')), float(input('Enter Y-Velocity 1: ')), float(input('Enter Z-Velocity 1: ')))

Mass2 = float(input('Enter Mass 2: '))
Position2 = vector(float(input('Enter X-Pos 2: ')), float(input('Enter Y-Pos 2: ')), float(input('Enter Z-Pos 2: ')))
Velocity2 = vector(float(input('Enter X-Velocity 2: ')), float(input('Enter Y-Velocity 2: ')), float(input('Enter Z-Velocity 2: ')))

Masses = [Mass1, Mass2]

#Constants
G = 1.0

PlanetRadius = 6
StarRadius = 100
RadiusScale = 10

#Objects/Bodies
Object1 = ball(pos=Position1, velocity=
objects = []

#Main loop
for o in objects:
    print(str(o))

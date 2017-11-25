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

def TDelta(t0, t):
    return (t - t0)

def Acceleration(m, R1, R2):
    return (G * m / RAbs(R1, R2)**3) * RDelta(R1, R2)

def VInitial(m1, R1, R2, t, t0):
    a = Acceleration(m1, R1, R2)
    v = v

# ---------- User Input ----------
##Mass1 = float(input('Enter Mass 1: '))
##Position1 = vector(float(input('Enter X-Pos 1: ')), float(input('Enter Y-Pos 1: ')), float(input('Enter Z-Pos 1: ')))
##Velocity1 = vector(float(input('Enter X-Velocity 1: ')), float(input('Enter Y-Velocity 1: ')), float(input('Enter Z-Velocity 1: ')))
##
##Mass2 = float(input('Enter Mass 2: '))
##Position2 = vector(float(input('Enter X-Pos 2: ')), float(input('Enter Y-Pos 2: ')), float(input('Enter Z-Pos 2: ')))
##Velocity2 = vector(float(input('Enter X-Velocity 2: ')), float(input('Enter Y-Velocity 2: ')), float(input('Enter Z-Velocity 2: ')))
##
##TimeLength = float(input('Enter total run time: '))
##TimeStep = float(input('Enter time step: '))
Mass1 = 50
Position1 = vector(0,0,0)
Velocity1 = vector(0,0,0)
Mass2 = 15
Position2 = vector(50,50,0)
Velocity2 = vector(15,15,0)
TimeLength = 1000
TimeStep = 0.25

Masses = [Mass1, Mass2]     #Good practice would be extending the sphere() object to include Masses and Accelerations
Accelerations = [0.0, 0.0]

#Constants
G = 1.0

PlanetRadius = 6
StarRadius = 100
RadiusScale = 10

#Objects/Bodies
Object1 = sphere(radius=20, pos=Position1, velocity=Velocity1, color=color.yellow, make_trail=True) #, retain=50)
Object2 = sphere(radius=20, pos=Position2, velocity=Velocity1, color=color.blue, make_trail=True) #, retain=50)
Objects = [Object1, Object2]

#Other VPython and Main-Loop Stuff
scene = display(title='N-Body Simulation', visible=True, show_rendertime=True)
CurrentTime = 0
PreviousTime = 0

#Main loop
while(CurrentTime <= TimeLength):
    rate(60)
    #Get the leap-frog item
    for i in Objects:
        #Update scene camera position
        scene.center = i.pos
        
        IndexI = Objects.index(i)
        iMass = Masses[IndexI]
        #iAccel = Accelerations.index(i)
        iAccel = vector(0,0,0)

        #Perform leap-frog
        for j in Objects:
            if(i != j):
                IndexJ = Objects.index(j)
                jMass = Masses[IndexJ]
                dist = j.pos - i.pos
                iAccel = iAccel + G * jMass * dist / mag(dist)**3
        for i in Objects:
            i.velocity = i.velocity + iAccel * TDelta(PreviousTime, CurrentTime)
            i.pos = i.pos + i.velocity * TDelta(PreviousTime, CurrentTime)

    #Update time
    PreviousTime = CurrentTime
    CurrentTime += TimeStep

print('--- Finished! ---')
print('Final times: cur={0} && prev={1}'.format(CurrentTime, PreviousTime))

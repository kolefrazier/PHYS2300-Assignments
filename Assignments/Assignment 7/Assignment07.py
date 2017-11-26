import sys
from visual import *

# ---------- Body Class ----------
#Class: Body extends vpython's sphere
#   Assists in data containment for ease in data management,
#     because there is no way in hell that managing multiple
#     arrays of associated data is reasonable.
class Body(sphere):
    def __init__(self, name='', mass=1.1, radius=10.0, velocity=vector(0,0,0), position=vector(1,1,1)): #acceleration=vector(0,0,0)
        self.name = name
        self.mass = mass
        #self.acceleration = acceleration
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity)

# ---------- IO Functions ----------
def ReadFileData(FileName):
    FileHandle = open(FileName)
    FileData = FileHandle.readlines()
    FileHandle.close()

    return FileData

def InterpretFileData(FileData):
    DataLength = len(FileData)
    Bodies = []
    
    for i in range (0, DataLength, 5): #for (i = 0; i < FileData.length; i += 5)
        #Get Data
        Name = FileData[i]
        RawPositions = FileData[i+1]
        RawVelocities = FileData[i+2]
        RawUnknownData = FileData[i+3]
        RawMass = FileData[i+4]

        #Process position and velocity data
        #File Format:
        #   xPos yPos zPos
        #   vX vY vZ
        PositionsSplit = RawPositions.split(' ')
        Position = vector(float(PositionsSplit[0]), float(PositionsSplit[1]), float(PositionsSplit[2]))

        VelocitiesSplit = RawVelocities.split(' ')
        Velocity = vector(float(VelocitiesSplit[0]), float(VelocitiesSplit[1]), float(VelocitiesSplit[2]))

        NewBody = Body(name=Name, mass=float(RawMass), velocity=Velocity, position=Position, color=color.green)
        Bodies.append(NewBody)

    return Bodies
        
# ---------- Calculation Functions ----------
def Force(m1, m2, R1, R2):
    R12 = RDelta(R1, R2)
    return (G*m1*m2)/RAbs(R1, R2)**2 * R12

def RDelta(R1, R2):
    return R2 - R1

def RAbs(R1, R2):
    delta = RDelta(R1, R2)
    PreSquareRoot = delta.x**2 + delta.y**2 + delta.z**2
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

# ---------- Numerical and Other Constants ----------
G = 6.67e-11
RadiusScale = 10
BodyColors = {'Mercury':color.orange, 'Venus':color.orange, 'Earth':color.blue, 'Mars':color.red, 'Jupiter':color.brown, 'Saturn':color.brown, 'Uranus':color.blue, 'Neptune':color.blue, 'Pluto':color.purple}

# ---------- Script Logic (a dirty Main) ----------
# ---------- Process File Input ----------
Bodies = InterpretFileData(ReadFileData('planet_data_full.txt'))

# ---------- Other VPython and Main-Loop Stuff ----------
scene = display(title='N-Body Simulation', width=600, height=500, visible=True, show_rendertime=True, autoscale=False)
RunTime = 2e1000
TimeStep = 1000

# ---------- Simulation Loop ----------
#while(CurrentTime <= RunTime):
for dt in len(0, RunTime, TimeStep):
    rate(60)
    #Get the leap-frog item
    for i in Bodies:
        print(str(i.name))
        iAccel = vector(0,0,0)

        #Perform leap-frog
        for j in Bodies:
            if(i != j):
                dist = j.pos - i.pos
                iAccel = iAccel + G * j.mass * dist / mag(dist)**3
                
    for i in Bodies:
        i.velocity = i.velocity + iAccel * dt
        pos = i.pos + i.velocity * dt

    #Update time
    CurrentTime += dt

print('--- Finished! ---')
print('Final times: cur={0} && prev={1}'.format(CurrentTime, PreviousTime))

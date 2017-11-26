import sys
from visual import *

# ---------- Body Class ----------
#Class: Body extends vpython's sphere
#   Assists in data containment for ease in data management,
#     because there is no way in hell that managing multiple
#     arrays of associated data is reasonable.
class Body(sphere):
    def __init__(self, name='', mass=1.1, radius=10.0, velocity=vector(0.0, 0.0, 0.0), acceleration=vector(0.0, 0.0, 0.0), position=vector(1.0, 1.0, 1.0), color=color.white):
        self.name = name
        self.mass = mass
        self.acceleration = acceleration
        sphere.__init__(self, radius=radius, pos=position, velocity=velocity, color=color, make_trail=True, retain=500)

    def PrintDetails(self):
        print '[{0}]\n\tMass: {1}\n\tAccel: {2}\n\tVeloc: {3}\n\tpos: {4}'.format(self.name, str(self.mass), str(self.acceleration), str(self.velocity), str(self.pos))

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
        Name = FileData[i].strip()
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

        NewBody = Body(name=Name, mass=float(RawMass), velocity=Velocity, position=Position, color=BodyColors[Name])
        Bodies.append(NewBody)

    return Bodies

def GetSun():
    return Body(name='Sun', mass=1.99e30, velocity=vector(0,0,0), position=vector(0,0,0), color=BodyColors['Sun'])

# ---------- Numerical and Other Constants ----------
G = 6.67e-11
RadiusScale = 10
BodyColors = {'Sun':color.yellow, 'Mercury':color.orange, 'Venus':color.orange, 'Earth+Moon barycenter':color.blue, 'Mars':color.red, 'Jupiter':color.orange, 'Saturn':color.orange, 'Uranus':color.cyan, 'Neptune':color.cyan, 'Pluto':color.magenta}

# ---------- Script Logic (A Dirty Main Method) ----------
# ---------- Process File Input, Add Other Bodies ----------
Bodies = InterpretFileData(ReadFileData('planet_data_full.txt'))
Bodies.insert(0, GetSun())

# ---------- Other VPython and Main-Loop Stuff ----------
scene = display(title='N-Body Simulation', width=600, height=500, visible=True, show_rendertime=True, autoscale=False)
RunTime = 10000000
TimeStep = 100

# ---------- Simulation Loop ----------
#while(CurrentTime <= RunTime):
for dt in range(0, RunTime, TimeStep):
    rate(60)
    for i in Bodies:
        i.acceleration = vector(0.0,0.0,0.0)
        for j in Bodies:
            if i != j:
                dist = j.pos - i.pos
                i.acceleration = i.acceleration + G * j.mass * dist / mag(dist)**3
        for i in Bodies:
            i.velocity = i.velocity + i.acceleration * dt
            i.pos = i.pos + i.velocity * dt

print('--- Finished! ---')



# --- Exercise 5.1 ---

def trapezoidalRule(x):
    #If I'm understanding this right, the rule is essentially:
    #   Sum of the equally spaced points
    #       First and last point are halved, however.
    #       Interior points (not first or last) are not modified.
    print('lol')
    
    
def readVelocitiesFile():
    # Open and read in velocities.txt file
    velocitiesData = open('velocities.txt', 'r')
    rawData = velocitiesData.readlines()
    velocitiesData.close()
    
    for line in rawData:
        parsedData = line.split('\t')
        
        #Data format: [0] = time step \t [1] = velocity value
        #After splitting data, stick the data in the right array
        dataTime.append(parsedData[0])
        dataVelocities.append(parsedData[1])
        
def distancedTravelled():
    print('lol')
    #This is a total distance travelled, regardless of forward/backwards placement.
    #Make a running total (total = 0)
    #Find a way to calculate distance between two points. absolute value and subtraction, perhaps?
    #Return the total distance.
    

#Data containers
dataTime = []
dataVelocities = []

#Time variables for loop
timeStart = 0
timeEnd = 100
timeStep = 1

#Trapezoidal rule values
N = 10
a = -1
b = 1

for t in range(timeStart, timeEnd+1, timeStep):
    print(t)
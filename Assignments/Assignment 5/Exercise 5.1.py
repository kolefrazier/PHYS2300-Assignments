#--------------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Exercise 5.1
#
# Usage: python "Exercise 5.1.py"
#
# Description: Calculate and plot distance traveled using given velocity and time data.
#       Uses trapezoid rule.
#
# Inputs: None
#
# Outputs: Console data AND a visual plot
#
# Auxiliary Files: velocity.txt
#
# Special Instructions: Script will output data into the console and display a visual plot - watch for both!
#
#--------------------------------------------------------------------------------
# C o d e H i s t o r y
#--------------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Kole Frazier
#
#--------------------------------------------------------------------------------

import math
import matplotlib
import matplotlib.pylab as plot
import matplotlib.patches as mpatches

def trapezoidRule(data):
    #If I'm understanding this right, the rule is essentially:
    #   Sum of the equally spaced points
    #       First and last point are halved, however.
    #       Interior points (not first or last) are not modified.
    
    Sum = 0.0
    Sum += (data[0]/2)
    Sum += (data[-1]/2) #[-1] is the last element of a list. Reference: https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
    
    #Iterate over the "inner" elements of the list.
    #S    kip the first ([0]) and last ([len(data)-1]) elements
    #    Len is 1-based, indexing is 0 based. Second to last item is (with conversion from 1 to 0 base) is -2.
    for x in range(1, len(data)-2): 
        Sum += data[x]
        
    return Sum
    
def readVelocitiesFile():
    # Open and read in velocities.txt file
    velocitiesData = open('velocities.txt', 'r')
    rawData = velocitiesData.readlines()
    velocitiesData.close()
    
    dataTime = []
    dataVelocities = []
    
    for line in rawData:
        parsedData = line.split('\t')
        
        #Data format: [0] = time step \t [1] = velocity value
        #After splitting data, stick the data in the right array
        dataTime.append(parsedData[0])
        dataVelocities.append(float(parsedData[1]))
        
    return dataTime, dataVelocities
        
def distanceTraveledTotal(data):
    #This is a total distance travelled, regardless of forward/backwards placement.
    #We know that velocity = (distance / time). Since we need distance, we can find it by modifying the v=(d/t) formula: (velocity * time) = distance.
    #   From there, we know that negative distances won't matter for this, so we can simply call abs on all values.
    
    runningTotal = 0.0
    
    for x in range(1, len(data), 1):
        distance = abs(data[x]) / x 
        
        runningTotal += abs(distance) #Enforce adding positive numbers only.
    
    return runningTotal
    
def distanceTraveledPoints(data):
    distancePoints = []
    distancePoints.append(0) #At time=0, the point had zero velocity. Add it in before hand, but prevent div-by-zero errors.
    
    for x in range(1, len(data), 1):
        distance = abs(data[x]) / x 
        
        distancePoints.append(abs(distance)) #Enforce adding positive numbers only.
        
    return distancePoints
    

#Get file data
dataTime, dataVelocities = readVelocitiesFile()

TrapezoidRuleResult = trapezoidRule(dataVelocities)
TotalDistanceTraveled = distanceTraveledTotal(dataVelocities)
DistanceTraveledPoints = distanceTraveledPoints(dataVelocities)

print('Trapezoid Rule result: {0}\nTotal distance travelled: {1}'.format(str(TrapezoidRuleResult), str(TotalDistanceTraveled)))

#Plot data
plot.figure()
plot.plot(dataTime, dataVelocities, 'b', linewidth=2.0)
velocityLegendEntry = mpatches.Patch(color='blue', label='Velocity (m/s) over time')
plot.plot(dataTime, DistanceTraveledPoints, 'y', linewidth=2.0)
distanceLegendEntry = mpatches.Patch(color='yellow', label='Distance (m) traveled over time')
plot.title('Distance over Time')
plot.xlabel('Time (seconds)')
plot.legend(handles=[velocityLegendEntry, distanceLegendEntry])
plot.show()
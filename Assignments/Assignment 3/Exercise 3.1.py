#Exercise 3.1 - Plotting experimental data

import pylab as plt

Sunspots = []
Months = []
RunningAverages = []

filename = "sunspots.txt"

try:
    datafile = open(filename, 'r')
    
    for line in datafile:
        try:
            data = line.split('\t')
            #[0] = Month, [1] = Sunspot number
            Months.append(data[0])
            Sunspots.append(data[1])
            
            SunspotSum = 0.0
            EntryCounter = 0
            for spot in Sunspots:
                SunspotSum += float(spot)
                EntryCounter += 1
                
            RunningAverages.append(SunspotSum/EntryCounter)
            
            if(len(Sunspots) >= 1000):
                break;
        except Exception as e:
            print('(file io) Error {0}'.format(e))
except Exception as e:
    print('(main) Error {0}'.format(e))
    
#print('Months: {0}\tSunspots: {1}\tAves: {2}'.format(len(Months), len(Sunspots), len(RunningAverages)))

HighestMonth = 0
for m in Months:
    if m > HighestMonth:
        HighestMonth = m
print('HighestMonth: ' + HighestMonth)

plt.plot(Months, Sunspots, 'bo')
plt.plot(Months, RunningAverages, 'yo')
plt.xlabel('Months since 1749')
plt.ylabel('Sunspots (Blue), Running Average (Yellow)')
plt.show()

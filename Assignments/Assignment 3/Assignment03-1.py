import sys
import matplotlib
import matplotlib.pylab as plot
import math as m
import numpy as np

def GetDecimalYear(year, month, day):
    DaysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    DaysInYear = 365.0 #Set as variable to allow for Leap Year adjustments.
    MonthCounter = 1
    TotalDays = 0.0
    while(MonthCounter < int(month)):
        TotalDays += DaysInMonths[MonthCounter]
        MonthCounter += 1
    
    TotalDays += int(day)
    LeapYear = IsLeapYear(year)
    if(LeapYear and (month > 2 or (month == 2 and day == 29))):
        #print('[DEBUG] We gots ourselves a leaps year')
        DaysInYear += 1
        TotalDays += 1
    
    #print('Total Days: ' + str(TotalDays) + ' Days in Year: ' + str(DaysInYear))
    
    #Return decimal of part year plus given full year
    #This way we're getting more than a random decimal value.
    #   Such as "1973.236" instead of just "0.236".
    return (TotalDays/DaysInYear + year) 
        
    
def IsLeapYear(year):
    #Leap Year Rules:
    #   Year IS divisible by 4
    #   Year IS NOT a multiple of 100 (EXCEPT multiples of year 400)
    #
    #Another way to do this is to take a known Leap Year (ie 1904) 
    #    and increment or decrement it by 4 for an arbitrary range (say, 30 Leap Years), skipping the years
    #       that meet the "Multiple of 100" or "Multiple of 400" rules.
    #   Then use a list comprehension (aka: python magic) to simply check: if(year in ListOfLeapYears).
    FourYearCheck = year % 4
    if(FourYearCheck == 0):
        HundredYearCheck = year % 100
        FourHundredYearCheck = year % 400
        if(HundredYearCheck != 0 or FourHundredYearCheck == 0):
            return True
    
    #All else, it's not a leap year.
    return False

LineSkips = 0   #Simple counter for debug purposes

#Holds temperatures on a per-month basis for easier standard deviation and means
meanMonthlyTemperatures = [[], [], [], [], [], [], [], [], [], [], [], []] #12 lists, one for each month.

#One-to-One values for plotting
meanTimes = []
meanTemperatures = []
maxTemperatures = []
minTemperatures = []

try:
    #filename = str(sys.argv[1])
    filename = 'OgdenWeatherData.txt'
    
    datafile = open(filename, 'r')
    datafile.readline() #skip the first line
    
    for line in datafile:
        data = line.split()
        
        #File Meta
        #    [2]    date
        #    [3]    mean temperature
        #    [17]    max temp reported on that day
        #    [18]    min temp reported on that day
        try:
            date = data[2]
            temperature = float(data[3])
            
            if(temperature == 999.9 or date == 999.9):
                continue;
                
            #parse date into day/month/year
            #convert it to decimal years
            year = float(date[0:4])
            month = float(date[4:6])
            day = float(date[6:8])
            
            #Record data to lists
            decimalYear = GetDecimalYear(year, month, day)
            meanMonthlyTemperatures[int(month)-1].append(temperature) #[month-1] to handle zero-based indexing
            meanTimes.append(decimalYear)
            meanTemperatures.append(temperature)
        
        except Exception as e:
            LineSkips += 1
            print('[Skips: {0}]\tIt skips the line: {1}'.format(LineSkips, str(e)))
        
        #--- For loop end ---
        
        #Cleanup
        datafile.close()
except (ValueError, IndexError) as e:
	print ('[Handled Exception] Value or Index exception encountered: {0}'.format(str(e)))
except Exception as e:
	print ('[Unhandled Exception] Unknown exception encountered: {0}'.format(str(e)))
	
#Plotting time
plot.figure()

#Setup and fill in decimal year plot
plot.subplot(2,1,1)
plot.title("Temperatures at Ogden, UT")
plot.plot(meanTimes, meanTemperatures, "bo")
plot.xlabel("Decimal Year")
plot.ylabel("Temperature, F")

#Setup and fill in monthly plot
plot.subplot(2,1,2)
plot.ylabel("Temperature, F")
MonthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
monthNumber = np.array(range(0,12,1))
plot.xlim([0.7, 13])
plot.ylim([0,90])
width = 0.8
height = 1.0

#Calculate the per-month temperature standard deviation
stdMonthTemps = []
for m in meanMonthlyTemperatures:
    stdMonthTemps.append(np.std(np.array(m)))
    
#Calculate the per-month temperature mean
MeansPerMonth = []
for m in meanMonthlyTemperatures:
    MeansPerMonth.append(np.mean(np.array(m)))

#Set graph data
plot.bar(monthNumber, MeansPerMonth, yerr=stdMonthTemps, width=width, color="lightgreen", ecolor="black", linewidth=1.5)
plot.xticks(monthNumber+width/2, MonthNames)

#Show the plots
plot.show()

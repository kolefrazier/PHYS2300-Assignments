#--------------------------------------------------------------------------------
import csv
import matplotlib
import matplotlib.pylab as plot
import math as m
import numpy as np

#--------------------------------------------------------------------------------
# File IO, Raw Data Functions
#--------------------------------------------------------------------------------

def ReadDataFile(FileName):
    FileHandle = open(FileName)
    FileData = FileHandle.readlines()
    FileHandle.close()
    print ('DBG: Finished reading in data for file: ' + FileName)
    return FileData

def OrganizeData(FileData):
    print('starting data organization')
    #Set up a dictionary for data fields
    DataDictionary = {}
    reader = csv.reader(FileData, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    DictionaryHeaders = next(reader)

    print('Prepping headers: ')
    #Prep data headers
    Headers = []
    for header in DictionaryHeaders:
        DataDictionary[header] = []
        Headers.append(header)

    print('Organizing the data: ')
    #Interpret the rest of the data
    LoopLen = len(FileData) - 1
    for line in range(1, LoopLen):
        DataSplit = next(reader)
        ParseLoopLen = len(DataSplit) - 1
        
        for value in range(0, ParseLoopLen):
            Key = Headers[value]
            DataDictionary[Key].append(DataSplit[value])

    return DataDictionary


def InterpretDailyFileData(FileData):
    print ('lol')

def InterpretYearlyFileData(FileData):
    print ('lol')

#--------------------------------------------------------------------------------
# Helper Methods
#--------------------------------------------------------------------------------

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
        DaysInYear += 1
        TotalDays += 1
    
    #Return decimal of part year plus given full year
    #This way we're getting more than a random decimal value.
    #   Such as "1973.236" instead of just "0.236".
    return (TotalDays/DaysInYear + year)

def IsLeapYear(year):
    #Leap Year Rules:
    #   Year IS divisible by 4
    #   Year IS NOT a multiple of 100 (EXCEPT multiples of year 400)
    FourYearCheck = year % 4
    if(FourYearCheck == 0):
        HundredYearCheck = year % 100
        FourHundredYearCheck = year % 400
        if(HundredYearCheck != 0 or FourHundredYearCheck == 0):
            return True
    
    #All else, it's not a leap year.
    return False

#--------------------------------------------------------------------------------
# Plotting and Data Methods
#--------------------------------------------------------------------------------
#Removes entries that have missing data from two given data sets.
#Non-removed entries are casted to floats and then appended to an array to be returned.
#	Ex: If X=2 and Y=null, this (X,Y) coordinate will be skipped.
def cleanData(x, y):
    floatx = []
    floaty = []
    
    for i in range(0, len(x)-1):
        if (x[i] == '' or y[i] == ''):
            continue
        floatx.append(float(x[i]))
        floaty.append(float(y[i]))
        
    return floatx, floaty

#Averages a list of data for each unique key in a list of keys
#   Example usage: A list of years (repeating keys, shuffled) with temperatures for each year entry
def AverageDataByKey(keys, data):
    print('DBG AverageDataByKey - START')
    #Helper Vars
    HandledKeys = []
    AverageForKey = []

    for i in range(0, len(keys)-1):
        if(keys[i] in HandledKeys):
            continue
        else:
            HandledKeys.append(keys[i])
            indexes = [a for a, x in enumerate(keys) if x == keys[i]] #List comprehension to find all indexes of the given key
            #print ('DBG: Key: {0} with len(indexes): {1}'.format(str(keys[i]), str(len(indexes))))
            
            Counter = len(indexes)
            Sum = 0
            for index in indexes:
                Sum += data[index]

            AverageForKey.append(float(Sum)/float(Counter))

    return HandledKeys, AverageForKey

#Plot some data and include a trend line in one easy to use method!
def PlotWithTrendLine(x, y):
    #Credit for this method: http://widu.tumblr.com/post/43624347354/matplotlib-trendline
    plot.plot(x, y, 'bo')
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plot.plot(x, p(x), "b--")

#--------------------------------------------------------------------------------
# Global Variables
#
# Notes
# The start of the year is August 1, according to the NOAA documentation for the "FZFx" data field.
#   https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/gsom-gsoy_documentation.pdf
#
#--------------------------------------------------------------------------------
YearStartMonth = 8
YearStartDay = 1

FileNames = {'Daily':'WeatherData-SLC-RegionDailyWeather.csv', 'Yearly':'WinterData-YearlySummaries.csv'}
DataYearly = OrganizeData(ReadDataFile(FileNames['Yearly']))
#DataDaily = OrganizeData(ReadDataFile(FileNames['Daily']))
print('Data read finished, beginning cleanup and plotting...')

print ('DBG: len[date]= {0}\tlen[tavg]={1}'.format(len(DataYearly['DATE']), len(DataYearly['TAVG'])))

#plotScatter(DataYearly['DATE'], DataYearly['TAVG'])
cleanedX, cleanedY = cleanData(DataYearly['DATE'], DataYearly['TAVG'])
Year, AveTemp = AverageDataByKey(cleanedX, cleanedY)

#--------------------------------------------------------------------------------
# Data Plotting
#--------------------------------------------------------------------------------
plot.figure()
plot.title('Average Temperature by Year')

PlotWithTrendLine(Year, AveTemp)
plot.show()
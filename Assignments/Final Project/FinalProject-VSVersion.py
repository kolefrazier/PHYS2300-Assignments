#--------------------------------------------------------------------------------
import csv
import matplotlib
import matplotlib.pylab as plot
import math as m
import numpy as np

#--------------------------------------------------------------------------------
# File IO, Raw Data Functions
#--------------------------------------------------------------------------------

#Method to read in all lines from given data file at once.
#   It reads them all in at once to speed up processing later.
#   (A read->process->read->process would be terribly inefficient.)
def ReadDataFile(FileName):
    FileHandle = open(FileName)
    FileData = FileHandle.readlines()
    FileHandle.close()
    return FileData

#Method to organize raw data.
#   A dictionary is set up, with keys based on the first row in the CSV file.
#   After setting up keys, values are read in and assigned to the matching key index.
#   Data is NOT sanitized, casted or trimmed. It is simply organized in its raw format.
def OrganizeData(FileData):
    #Set up a dictionary for data fields
    DataDictionary = {}

    #Utilize Python's native CSV reader to handle the quotes in the data set.
    #This is necessary, as a simple split(',') creates more values than headers (due to legitimate commas in some fields)
    reader = csv.reader(FileData, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    DictionaryHeaders = next(reader)

    #Prep data headers
    Headers = []
    for header in DictionaryHeaders:
        DataDictionary[header] = []
        Headers.append(header)

    #Interpret the rest of the data
    LoopLen = len(FileData) - 1
    for line in range(1, LoopLen):
        DataSplit = next(reader)
        ParseLoopLen = len(DataSplit) - 1
        
        for value in range(0, ParseLoopLen):
            Key = Headers[value]
            DataDictionary[Key].append(DataSplit[value])

    return DataDictionary

#Method to clean data, removing incomplete ordered pairs and casting to floats.
#Removes entries that have missing data from two given data sets.
#Non-removed entries are casted to floats and then appended to an array to be returned.
#	Ex: If X=2 and Y=null, this (X,Y) coordinate will be skipped.
def CleanDataFloat(x, y):
    floatx = []
    floaty = []
    
    for i in range(0, len(x)-1):
        if (x[i] == '' or y[i] == ''):
            continue
        floatx.append(float(x[i]))
        floaty.append(float(y[i]))
        
    return floatx, floaty

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

#Averages a list of data for each unique key in a list of keys
#   Example usage: A list of years (repeating keys, shuffled) with temperatures for each year entry
def AverageDataByKey(keys, data):
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
def PlotWithTrendLine(x, y, color='b', label='', labelLocation='upper left'):
    #Prepare plot design choices
    PointDesign = color + 'o'
    TrendDesign = color + '-'

    if(label != ''):
        plot.plot(x, y, PointDesign, label=label)
        plot.legend(loc=labelLocation)
    else:
        plot.plot(x, y, PointDesign)

    #Generate and plot the trend line
    #Credit for this method: http://widu.tumblr.com/post/43624347354/matplotlib-trendline
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plot.plot(x, p(x), TrendDesign)

#Plot only the trend line of some data with this one easy to use method!
def PlotTrendLineOnly(x, y, color='b', label='', labelLocation='upper left'):
    #Prepare plot design choices
    TrendDesign = color + '-'

    #Generate trend line data
    #Credit for this method: http://widu.tumblr.com/post/43624347354/matplotlib-trendline
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    
    #Plot with or without label
    if(label != ''):
        plot.plot(x, p(x), TrendDesign, label=label)
        plot.legend(loc=labelLocation)
    else:
        plot.plot(x, p(x), TrendDesign)
    
#--------------------------------------------------------------------------------
# Main Script Area
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
print('Completed reading in data sets.')

#--------------------------------------------------------------------------------
# Data Prep and Plotting
#   Figures are exported as individual plots, as PyPlot squishes the plots a bit too much for my taste.
#--------------------------------------------------------------------------------
print('Working on plot: '), #Leave trailing comma, keeps next print() on the same line.

#Average Temperature per Year
print('1 '),
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['TAVG'])
YearTemperatureAverage, AverageTemperature = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average Temperature by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Temperature')
PlotWithTrendLine(YearTemperatureAverage, AverageTemperature)
plot.savefig('AverageTemperature.png')

#Average Snowfall per Year
print('2 '),
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['SNOW'])
YearSnow, AverageSnow = AverageDataByKey(cleanedX, cleanedY)

#plot.figure()
plot.figure()
plot.title('Average Snowfall by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Snowfall')
PlotWithTrendLine(YearSnow, AverageSnow)
plot.savefig('AverageSnow.png')

#Average Snowfall per Year vs. Average Precipitation per Year
print('3 '),
#Snow averages were already calculated. So only Precipitation is needed.
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['PRCP'])
YearPrecipitation, AveragePrecipitation = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average Precipitation by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Precipitation')
PlotWithTrendLine(YearPrecipitation, AveragePrecipitation, labelLocation='upper right')
plot.tight_layout() #Prevent overlapping
plot.savefig('AveragePrecipitation.png')

#Average Snowfall per Year vs. Average Precipitation per Year
print('4 ')
plot.figure()
plot.title('Average Snowfall vs. Average Precipitation')
plot.xlabel('Year')
plot.ylabel('Amount')
PlotTrendLineOnly(YearSnow, AverageSnow, 'b', 'Snow', labelLocation='upper right')
PlotTrendLineOnly(YearPrecipitation, AveragePrecipitation, 'g', 'Precipitation', labelLocation='upper right')
plot.savefig('SnowVsPrecipitation.png', bbox_inches='tight')

print('Done!\n')
print('Finished plotting and exporting all graphs.\n')
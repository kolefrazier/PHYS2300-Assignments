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


def GetYearsFromDates(dates, splitChar='-'):
    years = []
    for date in dates:
        spliteDate = date.split(splitChar)
        years.append(spliteDate[0])

    return years
    

#--------------------------------------------------------------------------------
# Helper Methods
#--------------------------------------------------------------------------------

#Simple function to print each graph's number as they are parsed in the script.
def GraphCounter():
    global GraphCount
    GraphCount += 1
    return str(GraphCount) + ' '

#Averages a list of data for each unique key in a list of keys
#   Example usage: A list of years (repeating keys, shuffled) with temperatures for each year entry
def AverageDataByKey(keys, data):
    #Setup lists that will be returned
    HandledKeys = []
    AverageForKey = []

    for i in range(0, len(keys)-1):
        if(keys[i] in HandledKeys):
            continue
        else:
            #Add the key to the handled list so that it cannot be reparsed.
            HandledKeys.append(keys[i])

            #List comprehension to find all indexes of the given key
            indexes = [a for a, x in enumerate(keys) if x == keys[i]] 
            
            #Setup some values to aid
            Counter = len(indexes)
            Sum = 0

            #Parse values, take average
            for index in indexes:
                Sum += data[index]

            AverageForKey.append(float(Sum)/float(Counter))

    return HandledKeys, AverageForKey

#Filters out (key, data) pairs based on whether the data value is at or under value.
def FilterUnderEqualToValue(keys, data, value):
    #Setup lists that will be returned
    FilteredKeys = []
    FilteredData = []

    #Iterate over values. If it meets the condition, log its key and its data.
    for index, item in enumerate(data):
        if(item <= value):
            FilteredKeys.append(keys[index])
            FilteredData.append(item)

    return FilteredKeys, FilteredData

def FilterDataForKeyValue(Keys, Data1, Data2, Target):
	FilteredData1 = []
	FilteredData2 = []

	for index, item in enumerate(Keys):
		if(item == Target):
			FilteredData1.append(Data1[index])
			FilteredData2.append(Data2[index])

	return FilteredData1, FilteredData2

#Counts the number of values associated with each key.
#   Useful for "Total per X" situations.
def CountForKey(keys):
    #Setup lists that will be returned
    HandledKeys = []
    CountForKey = []

    #Iterative over keys. 
    #   If key has been handled, skip it.
    #   Else finds it matching values, count how many were found, log it.
    for index, key in enumerate(keys):
        if(key in HandledKeys):
            continue
        else:
            HandledKeys.append(key)
            indexes = [a for a, x in enumerate(keys) if x == key]
            CountForKey.append(len(indexes))

    return HandledKeys, CountForKey

#--------------------------------------------------------------------------------
# Plotting and Data Methods
#--------------------------------------------------------------------------------

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
GraphCount = 0

print('Starting data file import and parsing. These may take a moment to process!\n\t1) Yearly Data ... '),
FileNames = {'Daily':'WeatherData-SLC-Daily.csv', 'Yearly':'WeatherData-SLC-Yearly.csv'}
DataYearly = OrganizeData(ReadDataFile(FileNames['Yearly']))
print('Finished!\n\t2) Daily Data ... '),
DataDaily = OrganizeData(ReadDataFile(FileNames['Daily']))
print('Finished!\nCompleted reading and organizing data sets.')

#--------------------------------------------------------------------------------
# Data Prep and Plotting
#   Figures are exported as individual plots, as PyPlot squishes the plots a bit too much for my taste.
#	
#	I left the plotting flushed out on a per-plot basis. For a long-term project, this should be
#		cleaned up with helper plot funtions to reduce repeated plot setup and calls.
#--------------------------------------------------------------------------------
print('Parsing and generating plot: '), #Leave trailing comma, keeps the next print() on the same line.

# ----- Average Temperature per Year ----- 
print(GraphCounter()),
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['TAVG'])
YearTemperatureAverage, AverageTemperature = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average Temperature by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Temperature (F)')
PlotWithTrendLine(YearTemperatureAverage, AverageTemperature)
plot.savefig('AverageTemperature.png')

# ----- Average Snowfall per Year ----- 
print(GraphCounter()),
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['SNOW'])
YearSnow, AverageSnow = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average Snowfall by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Snowfall (Inches)')
PlotWithTrendLine(YearSnow, AverageSnow)
plot.savefig('AverageSnow.png')

# ----- Average Snowfall per Year vs. Average Precipitation per Year ----- 
print(GraphCounter()),
#Snow averages were already calculated. So only Precipitation is needed.
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['PRCP'])
YearPrecipitation, AveragePrecipitation = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average Precipitation by Year for Salt Lake Area')
plot.xlabel('Year')
plot.ylabel('Average Precipitation (Inches)')
PlotWithTrendLine(YearPrecipitation, AveragePrecipitation, labelLocation='upper right')
plot.tight_layout() #Prevent overlapping
plot.savefig('AveragePrecipitation.png')

# ----- Average First <32 Degrees Day ----- 
print(GraphCounter()),
#Snow averages were already calculated. So only Precipitation is needed.
cleanedX, cleanedY = CleanDataFloat(DataYearly['DATE'], DataYearly['FZF0'])
YearFreeze, AverageFreeze = AverageDataByKey(cleanedX, cleanedY)

plot.figure()
plot.title('Average First <32F Day of Season')
plot.xlabel('Year')
plot.ylabel('Average Number of Days Since Season Start (August 1)')
PlotWithTrendLine(YearPrecipitation, AveragePrecipitation, labelLocation='upper right')
plot.tight_layout() #Prevent overlapping
plot.savefig('AverageFreeze.png')

# ----- Average Snowfall per Year vs. Average Precipitation per Year ----- 
#No parsing for this one, only regraphing existing data.
print(GraphCounter()),
plot.figure()
plot.title('Average Snowfall vs. Average Precipitation')
plot.xlabel('Year')
plot.ylabel('Amount (Inches)')
PlotTrendLineOnly(YearSnow, AverageSnow, 'b', 'Snow', labelLocation='upper right')
PlotTrendLineOnly(YearPrecipitation, AveragePrecipitation, 'g', 'Precipitation', labelLocation='upper right')
plot.savefig('SnowVsPrecipitation.png', bbox_inches='tight')

# ----- Days Where Max Temp <= 32 Degegrees F. Per Year (Specific Location) ----
TargetLocation = 'SALT LAKE TRIAD CENTER, UT US'
FilteredDates, FilteredTemps = FilterDataForKeyValue(DataDaily['NAME'], DataDaily['DATE'], DataDaily['TMAX'], TargetLocation)
ExtractedYears = GetYearsFromDates(FilteredDates)
cleanedX, cleanedY = CleanDataFloat(ExtractedYears, FilteredTemps)
filteredX, filteredY = FilterUnderEqualToValue(cleanedX, cleanedY, 32)
YearCount, DayCount = CountForKey(filteredX)
print(GraphCounter()),
plot.figure()
plot.title('Days with Maximum Temperature <= 32 Degrees F.\n(All Locations)')
plot.xlabel('Year')
plot.ylabel('Number of Days')
PlotWithTrendLine(YearCount, DayCount)
plot.savefig('DaysUnder32-' + TargetLocation + '.png')

# ----- Days Where Max Temp <= 32 Degegrees F. Per Year (All Locations) ----
ExtractedYears = GetYearsFromDates(DataDaily['DATE'])
cleanedX, cleanedY = CleanDataFloat(ExtractedYears, DataDaily['TMAX'])
filteredX, filteredY = FilterUnderEqualToValue(cleanedX, cleanedY, 32)
YearCount, DayCount = CountForKey(filteredX)
print(GraphCounter()),
plot.figure()
plot.title('Days with Maximum Temperature <= 32 Degrees F.\n(All Locations)')
plot.xlabel('Year')
plot.ylabel('Number of Days')
PlotWithTrendLine(YearCount, DayCount)
plot.savefig('DaysUnder32-AllLocations.png')

#  ----- Final Messages ----- 
print('Done!\nFinished plotting and exporting all graphs.\n')
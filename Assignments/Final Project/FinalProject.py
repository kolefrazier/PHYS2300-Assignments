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
    return FileData

def OrganizeData(FileData):
    #Set up a dictionary for data fields
    DataDictionary = {}
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


def InterpretDailyFileData(FileData):
    print 'lol'

def InterpretYearlyFileData(FileData):
    print 'lol'

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

#--------------------------------------------------------------------------------
# Plotting Methods
#--------------------------------------------------------------------------------

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

FileNames = {'Daily':'./Winter Data/WeatherData-SLC-RegionDailyWeather.csv', 'Yearly':'./Winter Data/WinterData-YearlySummaries.csv'}
DataYearly = OrganizeData(ReadDataFile(FileNames['Yearly']))
DataDaily = OrganizeData(ReadDataFile(FileNames['Daily']))

print DataDaily[



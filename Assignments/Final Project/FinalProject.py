import csv
from visual import *
from visual.graph import *

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

FileNames = {'Daily':'./Winter Data/WeatherData-SLC-RegionDailyWeather.csv', 'Yearly':'./Winter Data/WinterData-YearlySummaries.csv'}
DataYearly = OrganizeData(ReadDataFile(FileNames['Yearly']))
DataDaily = OrganizeData(ReadDataFile(FileNames['Daily']))




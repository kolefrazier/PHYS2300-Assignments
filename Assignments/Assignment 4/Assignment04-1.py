#----------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#---------------------------------------------------------------------------
# Name: harbor.py
#
# Usage: python harbor.py
#
# Description: Code to correlate and interpolate temperature vs. time with altitude vs. time
#
# Inputs: Wxfile: contains the HARBOR weather data (WX)
# GPSfile: contains the HARBOR GPS track data
# DisplayOption: either "show" to screen or "save" to file
#
# Outputs: plots and analysis
#
# Auxiliary Files: None
#
# Special Instructions: None
#
#----------------------------------------------------------------------------
# C o d e H i s t o r y
#----------------------------------------------------------------------------
# Version: 1.0
#
# Author(s):
#
# Modifications:
#
#----------------------------------------------------------------------------
# -- Assignment04-1 --

#GPS data file is "BATS"
#Other is "PASCAL"
#slope (m) = (a2-a1)/(t2-t1), b=mt1-a1 (a1, t2, etc refers to a-subscript-2)
#pass in temp, 't'. Find 't' at 't'. return temp-subscript(1) 'a'.
#Keep in mind UTC to MDT/MST conversions. So either change one into UTC or into MDT.
#   Something like UTC-Offset.
#       7:00:00 Mountain Daylight Time
#       (UTC)13:00:00-(offset)6:00:00 = 7:00:00 (MDT)

import sys
import matplotlib
import matplotlib.pylab as plot
import math as m
import numpy as np

def decimalHour(hours, minutes, seconds):
    hours = float(hours)
    minutes = float(minutes)
    seconds = float(seconds)
    calculatedDecimalHour = hours + (minutes/60.0) + (seconds/(60.0*60.0))
    #print('DECIMAL HOUR: {0}:{1}:{2} => {3}'.format(hours, minutes, seconds, calculatedDecimalHour))
    return calculatedDecimalHour

# wxTimes, wxTemperatures = readWxData(wxFileName)
def readWxData(wxFileName):
    wxFile = open(wxFileName)
    wxFileData = wxFile.readlines()
    wxFile.close()
    return wxFileData
    
# gpsTimes, gpsAltitudes = readGPSData(gpsFileName)
def readGPSData(gpsFileName):
    #Read in all file data
    gpsFile = open(gpsFileName)
    gpsFileData = gpsFile.readlines()
    gpsFile.close()
    
    #The first two lines of the bats/RPS data file is header stuff. Start reading in at line 3.
    LineCount = 2 #0-based: 1,2,3=>0,1,2
    
    #Parse the data into two lists for return
    gpsTimes = []
    gpsAltitudes = []
    
    #Convert time columns into decimal hours & get altitude for each line.
    #   Hours [1], Min [2], Sec [3]
    #   Altitude [6]
    for line in gpsFileData:
        if(LineCount > 0):
            print('SKIPPING: ' + line)
            LineCount -= 1
            continue
            
        data = line.split('\t')

        gpsTimes.append(decimalHour(data[1], data[2], data[3]))
        gpsAltitudes.append(data[6])
    
    return gpsTimes, gpsAltitudes
    
def interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes):
    print('NOT YET IMPLEMENTED')
    
def plotAllFigs(display, wxTimes, wxTemperatures):
    plot.figure()
    plot.subplot(2,1,1)
    plot.plot(wxTimes, wxTemperatures,linewidth=2.0)
    plot.xlim(0,2.25)
    plot.title("Harbor Flight Data")
    plot.ylabel("Temperature, F")
    plot.subplot(2,1,2)
    plot.plot(gpsTimes, gpsAltitudes,linewidth=2.0)
    plot.xlim(0,2.25)
    plot.ylabel("Altitude, ft")
    plot.xlabel("Mission Elapsed Time, Hours")
    
    if display == "save":
        plot.savefig("fig2.2.1.png")
    elif display == "show":
        plot.show()
    else:
        print "Unrecognized output, ", display
        
    plot.figure()
    plot.subplot(1,2,1)
    plot.title("Harbor Ascent")
    plot.plot(wxCorrelatedTemperaturesUp,
    wxCorrelatedAltitudesUp,linewidth=2.0)
    plot.ylabel("Altitude, feet")
    plot.xlabel("Temperature, F")
    plot.ylim([0,100000])
    plot.subplot(1,2,2).set_yticklabels([])
    
    plot.title("Harbor Descent")
    plot.plot(wxCorrelatedTemperaturesDown, wxCorrelatedAltitudesDown ,linewidth=2.0)
    plot.xlabel("Temperature, F")
    plot.ylim([0,100000])
    
    if display == "save":
        plot.savefig("fig2.2.2.png")
    elif display == "show":
        plot.show()
    else:
        print "Unrecognized output, ", display
    
try:
    wxFileName = 'TempAndPressure.csv'
    gpsFileName = 'gpsData.txt'
    
    #read in temperature and time data
    #wxTimes, wxTemperatures = readWxData(wxFileName)
    gpsTimes, gpsAltitudes = readGPSData(gpsFileName)
    print('[RESULT] gpsTimes: {0}\tgpsAltitudes: {1}'.format(str(len(gpsTimes)), str(len(gpsAltitudes))))
    
    display = 'show' # or save
except (ValueError, IndexError), e:
    print ('[ERROR] File parsing error: ' + e)
    sys.exit()
    
sys.exit()
    
# #read in temperature and time data
# wxTimes, wxTemperatures = readWxData(wxFileName)
# gpsTimes, gpsAltitudes = readGPSData(gpsFileName)

#compute wx alts by interpolating from gps alts
wxCorrelatedAltitudesUp, wxCorrelatedAltitudesDown, wxCorrelatedTemperaturesUp, wxCorrelatedTemperaturesDown = interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes)

#Plot and quit
plotAllFigs(display)
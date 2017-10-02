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

def readWxData(wxFileName):
    print('NOT YET IMPLEMENTED')
    
def readGPSData(gpsFileName):
    print('NOT YET IMPLEMENTED')
    
def interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes):
    print('NOT YET IMPLEMENTED')
    
def plotAllFigs(display):
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
    wxFileName = 'TempAndPressure.txt'
    gpsFileName = 'gpsData.txt'
    display = 'show' # or save
except (ValueError, IndexError), e:
    print ('[ERROR] File parsing error: ' + e)
    
#read in temperature and time data
wxTimes, wxTemperatures = readWxData(wxFileName)
gpsTimes, gpsAltitudes = readGPSData(gpsFileName)

#compute wx alts by interpolating from gps alts
wxCorrelatedAltitudesUp, wxCorrelatedAltitudesDown, wxCorrelatedTemperaturesUp, wxCorrelatedTemperaturesDown = interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes)

#Plot and quit
plotAllFigs(display)
#----------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#---------------------------------------------------------------------------
# Name: Assignment04-1
#
# Usage: python Assignment04-1.py
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
# Author(s): Kole Frazier
#
# Modifications:
#
#----------------------------------------------------------------------------
# -- Assignment04-1 --
#
# ----- ANALYSIS QUESTIONS -----
# 1. - Switch "display" to "save" and it will save the graphs instead of opening them.
# 2. The difference between the ascent and descent temperatures is due to the weather balloon
#       changing in longitude and latitude simultaneously with altitude. This takes place over
#       multiple hours, too. Due to these factors, the weather balloon is not going to 
#       experience the same weather going up and going down.
# 3. Anomalies happen when sensors or measurement tools are unable to properly record data.
#       The tool may have been positioned oddly or its view/communication system may have been obstructed.
#       If the tool is relaying information wirelessly, it's possible that there was simply a transmission error
#       after taking its measurements. In the same frame of thought, it's possible that the recording program
#       received an error it couldn't handle, so it defaulted to a value and moved on to the next set of values.
#       These values could be arithmetic issues (eg divide by zero), precision issues for larger numbers, or
#       even corrupted data from transmission or failing memory.
#
# ----- Other Notes -----
#    The "Raw" graphs work as expected. 
#    However, the Ascend and Descend ones are ~half working.
#    The Ascend graph has the right data, plus some extra that I cannot pinpoint its source.
#    The Descend graph is only getting ~12 data points to plot. Again, I cannot pinpoint exactly where or why after many hours of trying to debug.

#GPS data file:                 bats_har090803.dat.txt
#Weather Balloon data file:     hat090803_pascal.csv

import sys
import matplotlib
import matplotlib.pylab as plot
import math as m
import numpy as np

#Calculate a decimal representation of an Hour:Minute:Second timestamp.
# See note at bottom of readGPSData()'s parsing for-loop.
#   (Basically, it's a fix for the data file.)
def decimalHour(hours, minutes, seconds, fiftyninecount): 
    hours = float(hours) + (fiftyninecount * float(60.0))
    minutes = float(minutes)
    seconds = float(seconds)
    calculatedDecimalHour = hours + (minutes/60.0) + (seconds/(60.0*60.0))
    return calculatedDecimalHour

#Read in the Weather Balloon's data (CSV file expected)
def readWxData(wxFileName):
    wxFile = open(wxFileName, 'r')

    wxTimes = []
    wxTemperatures = []

    index = 0
    while index < 17:
        wxFile.readline() # skip the first 17 lines - they're unnecessary data.
        index += 1
        
    firstLine = 0
    for line in wxFile:
        wxData = line.split(",")
        time = wxData[1].split(":")
        temperature = float(wxData[3])
        decimalHours = float(time[0]) + float(time[1])/60.0 + float(time[2])/60.0/60.0
        if firstLine == 0:
            decimalHoursRef = decimalHours
            firstLine = 1
        wxTimes.append(decimalHours - decimalHoursRef)
        wxTemperatures.append(temperature)
    # close data file
    wxFile.close()
    return wxTimes, wxTemperatures
    
#Read in the GPS's data file. 
#   (A '\t' delimited text file.)
def readGPSData(gpsFileName):
    #Read in all file data
    gpsFile = open(gpsFileName)
    gpsFileData = gpsFile.readlines()
    gpsFile.close()
    
    #The first two lines of the bats/RPS data file is header stuff. Start reading in at line 3.
    LineCount = 2 #0-based: 1,2,3=>0,1,2
    fiftyninecount = 0 #See note at bottom of parsing for-loop.
    
    #Parse the data into two lists for return
    gpsTimes = []
    gpsAltitudes = []
    
    #Convert time columns into decimal hours & get altitude for each line.
    #   Hours [1], Min [2], Sec [3]
    #   Altitude [6]
    for line in gpsFileData:
        
        if(LineCount > 0):
            LineCount -= 1
            continue
            
        data = line.split('\t')

        gpsTimes.append(decimalHour(data[1], data[2], data[3], fiftyninecount)/100.0)
        gpsAltitudes.append(data[6])
        
        #Basically, the hours in the data file only have a range of [0, 59].
        #   However, the data continues as though they were from the same run and not timed segments.
        #   So, instead of fixing the data file, this "fixes" the issue in the logging system.
        #   (Issue being hours can go BEYOND 59. Gotta love handling external issues in my homework.)
        #Mark this last to stop random spikes in the GPS graph.
        if(data[1] == '59'):
            #print '59 hours hit'
            fiftyninecount += 1
    
    return gpsTimes, gpsAltitudes
    
def myInterpolator(xLower, yLower, xUpper, yUpper, xInterp):
    #Y = Slope*x + Y-Intercept
    slope = (float(yUpper) - float(yLower))/(float(xUpper) - float(xLower))
    intercept = float(yLower) - float(slope)*float(xLower)
    
    return slope*float(xInterp) + intercept #y-mx+b
    
def interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes, wxTemperatures):
    #'Up' value lists
    wxCorrelatedAltitudesUp = []
    wxCorrelatedAltitudesDown = []
    
    #'Down' value lists
    wxCorrelatedTemperaturesUp = []
    wxCorrelatedTemperaturesDown = []
    
    #Other helper vars
    LastAltitude = 0.0
    FirstCheck = True
    AltitudeUp = True

    for wxindex in range(len(wxTimes)):
        for gpsindex in range(len(gpsTimes)-1):
            if wxTimes[wxindex] > gpsTimes[gpsindex] and wxTimes[wxindex] < gpsTimes[gpsindex+1]:
                #Set values to interpolation
                xLower = gpsTimes[gpsindex]
                yLower = gpsAltitudes[gpsindex]
                xUpper = gpsTimes[gpsindex+1]
                yUpper = gpsAltitudes[gpsindex+1]
                xInterp = wxTimes[wxindex]
                
                #Interpolate data, get current working temperature value.
                wxaltitude = myInterpolator(xLower, yLower, xUpper, yUpper, xInterp)
                wxtemperature = wxTemperatures[wxindex]
                
                #Set the first check value
                if(FirstCheck):
                    FirstCheck = False
                    LastAltitude = wxaltitude
                
                #Check if the altitude has gone down. This indicates the change from ascent to descent.
                if(wxaltitude < LastAltitude):
                    AltitudeUp = False
                    LastAltitude = wxaltitude
                    
                #AltitudeUp = true means that the balloon is ascending.
                #AltitudeUp = false means that the balloon is descending.
                #This indicates which list to append data to - Up or Down versions.
                if(AltitudeUp is True):
                    wxCorrelatedAltitudesUp.append(wxaltitude)
                    wxCorrelatedTemperaturesUp.append(wxtemperature)
                else:
                    wxCorrelatedAltitudesDown.append(wxaltitude)
                    wxCorrelatedTemperaturesDown.append(wxtemperature)

                #wxCorrelatedAltitudes.append(wxaltitude)
                #wxCorrelatedTemperatures.append(wxtemperature)
                
    #return wxCorrelatedAltitudes, wxCorrelatedTemperatures
    print '[DBG] List Sizes: AltUp:{0}, AltDown:{1}, TempUp:{2}, TempDown:{3}'.format(len(wxCorrelatedAltitudesUp), len(wxCorrelatedAltitudesDown), len(wxCorrelatedTemperaturesUp), len(wxCorrelatedTemperaturesDown))
    return wxCorrelatedAltitudesUp, wxCorrelatedAltitudesDown, wxCorrelatedTemperaturesUp, wxCorrelatedTemperaturesDown
    
#def plotAllFigs(display, wxTimes, wxTemperatures):
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
        #plot.savefig("fig2.2.1.png")
        plot.savefig("raw.png")
    elif display == "show":
        plot.show()
    else:
        print "Unrecognized output, ", display
        
    plot.figure()
    plot.subplot(1,2,1)
    plot.title("Harbor Ascent")
    plot.plot(wxCorrelatedTemperaturesUp, wxCorrelatedAltitudesUp,linewidth=2.0)
    plot.ylabel("Altitude, feet")
    plot.xlabel("Temperature, F")
    plot.ylim([0,100000])
    plot.subplot(1,2,2).set_yticklabels([])
    
    plot.title("Harbor Descent")
    plot.plot(wxCorrelatedTemperaturesDown, wxCorrelatedAltitudesDown ,linewidth=2.0)
    plot.xlabel("Temperature, F")
    plot.ylim([0,100000])
    
    if display == "save":
        #plot.savefig("fig2.2.2.png")
        plot.savefig("correlated.png")
    elif display == "show":
        plot.show()
    else:
        print "Unrecognized output, ", display
    
# ----- Global/Main Vars -----
#File Names - Standard
wxFileName = 'hat090803_pascal.csv'
gpsFileName = 'bats_har090803.dat.txt'

#File Names - Debug Files
# wxFileName = 'TempAndPressure.csv'
# gpsFileName = 'gpsData.txt'

#Graph display mode
display = 'show' # or 'save'
      
#read in temperature and time data
wxTimes, wxTemperatures = readWxData(wxFileName)
gpsTimes, gpsAltitudes = readGPSData(gpsFileName)

#compute wx alts by interpolating from gps alts
wxCorrelatedAltitudesUp, wxCorrelatedAltitudesDown, wxCorrelatedTemperaturesUp, wxCorrelatedTemperaturesDown = interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes, wxTemperatures)

#Plot and quit
#plotAllFigs(display, wxTimes, wxTemperatures)
plotAllFigs(display)

# display = 'save'
# plotAllFigs(display)

def myInterpolator(xLower, yLower, xUpper, yUpper, xInterp):
    
    slope = (yUpper - yLower)/(xUpper - xLower)
    intercept = yLower - slope*xLower
    
    return slope*xInterp + intercept

def interpolateWxFromGPS(wxTimes, gpsTimes, gpsAltitudes, wxTemperatures):
    wxCorrelatedAltitudes = []
    wxCorrelatedTemperatures = []

    for wxindex in range(len(wxTimes)):
        for gpsindex in range(len(gpsTimes)-1):
            if wxTimes[wxindex] > gpsTimes[gpsindex] and wxTimes[wxindex] < gpsTimes[gpsindex+1]:
                
                xLower = gpsTimes[gpsindex]
                yLower = gpsAltitudes[gpsindex]
                xUpper = gpsTimes[gpsindex+1]
                yUpper = gpsAltitudes[gpsindex+1]
                xInterp = wxTimes[wxindex]
                
                wxaltitude = myInterpolator(xLower, yLower, xUpper, yUpper, xInterp)
                wxtemperature = wxTemperatures[wxindex]
                
                wxCorrelatedAltitudes.append(wxaltitude)
                wxCorrelatedTemperatures.append(wxtemperature)
                
    return wxCorrelatedAltitudes, wxCorrelatedTemperatures

def readWxFile(wxFileName):
    wxFile = open(wxFileName, 'r')

    wxTimes = []
    wxTemperatures = []

    index = 0
    while index < 17:
        wxFile.readline() # skip the first 17 line
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
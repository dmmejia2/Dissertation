# -*- coding: utf-8 -*-
import csv


rawDataPrefix = "//Users//danielmejia//Documents//Ph.D.//Incident Data//"
modifiedDataPrefix = "//Users//danielmejia//Documents//workspace//IncidentImplement//"

removeIncidentColumnFile = "//Users//danielmejia//Documents//Ph.D.//CrashRemoveColumns.csv"

incidentDataFile14 = rawDataPrefix + "ELP Incidents 2014//ELP Public Incidents 2014 Crash.csv"
incidentDataFile15 = rawDataPrefix + "ELP Incidents 2015//ELP Public Incidents 2015 Crash.csv"
incidentDataFile16 = rawDataPrefix + "ELP Incidents 2016//ELP Public Incidents 2016 Crash.csv"
incidentDataFile17 = rawDataPrefix + "ELP Incidents 2017//ELP Public Incidents 2017 Crash.csv"
#String dataFile14a = rawDataPrefix + "AUSDALSAN Incidents 2014//AUSDALSAN Incidents 2014 Crash.csv";

incidentQueueList = list(())
incidentQueueList.append(incidentDataFile14)
incidentQueueList.append(incidentDataFile15)
incidentQueueList.append(incidentDataFile16)
incidentQueueList.append(incidentDataFile17)
incidentData = []
crashRemoveColumnValue = []
crashRemoveColumnIndex = []


def parseTime(time):
    currentTime = time.split(":")
    minutes = currentTime[1].split(" ")
    updatedTime = ""
    updatedHour = ""
    if len(minutes) == 2:
        parsedHour = int(currentTime[0])

        if parsedHour < 12 and minutes[1] == "PM":
            parsedHour += 12
            updatedHour = str(parsedHour)
        else:
            updatedHour = str(parsedHour)

        if parsedHour == 12 and minutes[1] == "AM":
            updatedHour = "00"

        if parsedHour < 10:
            updatedHour = "0"+str(parsedHour)

        updatedTime = updatedHour+":"+minutes[0]
    return updatedTime






#Reads all of the items from the CSV files
while incidentQueueList:

    tempFile = incidentQueueList.pop(0)
    with open(tempFile, "rb") as currentFile:
        reader = csv.reader(currentFile)
        for row in reader:
            #print(row)
            incidentData.append(row)


#Sets the unwanted columns
with open(removeIncidentColumnFile, "rb") as removeColumn:
    reader = csv.reader(removeColumn)
    tempIndex = 0
    for row in reader:
        for column in row:
            crashRemoveColumnValue.append(column)
        #print(value)


#Determines unwanted column indecies
for i in crashRemoveColumnValue:
    indexRemove = 0
    for j in incidentData[0]:
        if i == j:
            crashRemoveColumnIndex.append(indexRemove)
            break
        indexRemove += 1


tempDataSet = list(incidentData)
incidentData = []
for i in range(len(tempDataSet)):
    tempRow = tempDataSet[i]
    for j in crashRemoveColumnIndex:
        tempRow[j] = "*REMOVE*"
    incidentData.append(tempRow)




#Creates a new file with all data
file = open("IncidentsOnlyELP.csv", "w+")
iterationNumber = 0
for dataSet in incidentData:
    for dataPoint in dataSet:
        if dataPoint == "Crash_ID" and iterationNumber != 0:
            break
        elif dataPoint == "*REMOVE*":
            continue
        file.write(dataPoint)
        file.write(",")
    file.write("\n")
    iterationNumber += 1
file.close()


#Creates a new file with all numerical data
file = open("NumericalIncidentsOnlyELP.csv", "w+")
iterationNumber = 0
for dataSet in incidentData:
    for dataPoint in dataSet:
        if dataPoint == "Crash_ID" and iterationNumber != 0:
            break
        elif dataPoint == "*REMOVE*":
            continue

        currentDataPoint = dataPoint

        if currentDataPoint == "SUN":
            dataPoint = "0"
        elif currentDataPoint == "MON":
            dataPoint = "1"
        elif currentDataPoint == "TUE":
            dataPoint = "2"
        elif currentDataPoint == "WED":
            dataPoint = "3"
        elif currentDataPoint == "THU":
            dataPoint = "4"
        elif currentDataPoint == "FRI":
            dataPoint = "5"
        elif currentDataPoint == "SAT":
            dataPoint = "6"
        elif currentDataPoint == "Y":
            dataPoint = "1"
        elif currentDataPoint == "N":
            dataPoint = "0"
        elif ":" in currentDataPoint and currentDataPoint not in "MM:":
            dataPoint = parseTime(currentDataPoint)


        file.write(dataPoint)
        file.write(",")
    file.write("\n")
    iterationNumber += 1
file.close()


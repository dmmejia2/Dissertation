# -*- coding: utf-8 -*-
import csv
import pandas as pd


rawDataPrefix = "//Users//danielmejia//Documents//Ph.D.//Incident Data//"
modifiedDataPrefix = "//Users//danielmejia//Documents//workspace//IncidentImplement//"

removePersonColumnFile = "//Users//danielmejia//Documents//Ph.D.//CrashRemoveColumns.csv"
primePersonDataFile14 = rawDataPrefix + "ELP Incidents 2014//ELP Public Incidents 2014 PrimaryPerson.csv"
primePersonDataFile15 = rawDataPrefix + "ELP Incidents 2015//ELP Public Incidents 2015 PrimaryPerson.csv"
primePersonDataFile16 = rawDataPrefix + "ELP Incidents 2016//ELP Public Incidents 2016 PrimaryPerson.csv"
primePersonDataFile17 = rawDataPrefix + "ELP Incidents 2017//ELP Public Incidents 2017 PrimaryPerson.csv"
#dataFile14a = rawDataPrefix + "AUSDALSAN Incidents 2014//AUSDALSAN Incidents 2014 Crash.csv"

primePersonQueueList = list(())
primePersonQueueList.append(primePersonDataFile14)
primePersonQueueList.append(primePersonDataFile15)
primePersonQueueList.append(primePersonDataFile16)
primePersonQueueList.append(primePersonDataFile17)
personData = []
removePersonColumnValue = []
removePersonColumnIndex = []

#removePersonColumnFile = "//Users//danielmejia//Documents//Ph.D.//CrashRemoveColumns.csv"
secPersonDataFile14 = rawDataPrefix + "ELP Incidents 2014//ELP Public Incidents 2014 Persons.csv"
secPersonDataFile15 = rawDataPrefix + "ELP Incidents 2015//ELP Public Incidents 2015 Persons.csv"
secPersonDataFile16 = rawDataPrefix + "ELP Incidents 2016//ELP Public Incidents 2016 Persons.csv"
secPersonDataFile17 = rawDataPrefix + "ELP Incidents 2017//ELP Public Incidents 2017 Persons.csv"
#dataFile14a = rawDataPrefix + "AUSDALSAN Incidents 2014//AUSDALSAN Incidents 2014 Crash.csv"

secPersonQueueList = list(())
secPersonQueueList.append(secPersonDataFile14)
secPersonQueueList.append(secPersonDataFile15)
secPersonQueueList.append(secPersonDataFile16)
secPersonQueueList.append(secPersonDataFile17)
secPersonData = []
removeSecPersonColumnValue = []
removeSecPersonColumnIndex = []





#Reads all of the items from the CSV files
def readFiles(listQueue, dataStore):
    while listQueue:

        tempFile = listQueue.pop(0)
        with open(tempFile, "rb") as currentFile:
            reader = csv.reader(currentFile)
            for row in reader:
                #print(row)
                dataStore.append(row)
    return dataStore


#Sets the unwanted columns
def removeColumnValues(removeColumnFile, dataStore):
    with open(removeColumnFile, "rb") as removeColumn:
        reader = csv.reader(removeColumn)
        for row in reader:
            for column in row:
                dataStore.append(column)
            #print(value)
    return dataStore


#Determines unwanted column indecies
def removeColumnIndex(columnValues, indexDataStore, dataStore):
    for i in columnValues:
        indexRemove = 0
        for j in dataStore[0]:
            if i == j:
                indexDataStore.append(indexRemove)
                break
            indexRemove += 1
    return indexDataStore

#Sets data that is unwanted for removal
def removeUnwantedData(fullDataSet, removeIndex):
    tempDataSet = list(fullDataSet)
    for i in range(len(tempDataSet)):
        tempRow = tempDataSet[i]
        for j in removeIndex:
            tempRow[j] = "*REMOVE*"
            fullDataSet.append(tempRow)
    return fullDataSet




#Creates the file without the unwanted data
def createCSVFile(fileName, fullDataSet):
    # Creates a new file with all data
    file = open(fileName+".csv", "w+")
    iterationNumber = 0
    for dataSet in fullDataSet:
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

print("Person Parsing")

personData = readFiles(primePersonQueueList,personData)
removePersonColumnValue = removeColumnValues(removePersonColumnFile, removePersonColumnValue)
removePersonColumnIndex = removeColumnIndex(removePersonColumnValue,removePersonColumnIndex, personData)
personData = removeUnwantedData(personData, removePersonColumnIndex)
createCSVFile("ELPPrimaryPersons",personData)

secPersonData = readFiles(secPersonQueueList,secPersonData)
removeSecPersonColumnValue = removeColumnValues(removePersonColumnFile, removeSecPersonColumnValue)
removeSecPersonColumnIndex = removeColumnIndex(removeSecPersonColumnValue,removeSecPersonColumnIndex, secPersonData)
secPersonData = removeUnwantedData(secPersonData, removeSecPersonColumnIndex)
createCSVFile("ELPSecondaryPersons",secPersonData)

filenames = []
filenames.append("ELPPrimaryPersons.csv")
filenames.append("ELPSecondaryPersons.csv")
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined_csv.to_csv( "ELPAllPersons.csv", index=False )
print("Person Parsing Complete")
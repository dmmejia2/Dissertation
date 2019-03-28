# -*- coding: utf-8 -*-
import csv
import json
# import AccidentImplementation as accImp
import time

print("AccidentToJSON.py")
startTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
print("Start Time Seconds: ", startTime)
print("Local Time: ", localTime)

jsonPersonFileName = "AllPeople2014-2017JSONLD.json"
jsonAccidentFileName = "AllAccidents2014-2017.json"

contextValue = "http://schema.org/"
csvPersonFile = open("CompletePersons2014-2017.csv", 'r')
csvAccidentFile = open("AllAccidentsNumerical2014-2017.csv", 'r')

jsonPersonFile = open(jsonPersonFileName, 'w')
jsonAccidentFile = open(jsonAccidentFileName, 'w')


print("Person to JSON")
with open("CompletePersons2014-2017.csv", "rb") as currentFile:
    reader = csv.reader(currentFile)
    firstLine = next(reader)
    fieldnames = firstLine
    reader = csv.DictReader(csvPersonFile, fieldnames)
    next(reader)
    jsonPersonFile.write("[")
    for row in reader:
        del row['Unnamed: 27']
        del row['Unnamed: 32']
        # Prepend the context to the row??
        row["@context"] = contextValue
        row["@type"] = "Accident"
        row["@id"] = row["Crash_ID"]
        # currentContext = "@context: "+contextValue+","
        # row = currentContext + str(row)
        json.dump(row, jsonPersonFile, indent=4, sort_keys=True)
        jsonPersonFile.write(',\n')
    jsonPersonFile.write("{}]")
print("Person to JSON Complete")

print("Accident to JSON")
with open(accImp.numericalCSVFile+".csv", "rb") as currentFile:
    reader = csv.reader(currentFile)
    firstLine = next(reader)
    fieldnames = firstLine
    reader = csv.DictReader(csvAccidentFile, fieldnames)
    next(reader)
    jsonAccidentFile.write("[")
    for row in reader:
        del row['']

        json.dump(row, jsonAccidentFile, indent=4, sort_keys=True)
        jsonAccidentFile.write(',\n')
    jsonAccidentFile.write("{}]")
print("Accident to JSON Complete")

endTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
totalTime = (endTime-startTime)/60
print("End Time Seconds: ", startTime)
print("Total Time: ", totalTime)
print("Local Time: ", localTime)

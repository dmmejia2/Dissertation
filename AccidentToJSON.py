# -*- coding: utf-8 -*-
#########################################
# Author = Daniel Mejia                 #
# Email = "dmmejia2@miners.utep.edu     #
# Copyright = Copyright 2019            #
# The University of Texas at El Paso    #
# License = Common Creative License     #
#########################################
import csv
import json
import AccidentImplementation as accImp
import time

print("AccidentToJSON.py")
startTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
print("Start Time Seconds: ", startTime)
print("Local Time: ", localTime)


def get_year(accident_date):
    year = accident_date.split("/")
    year = year[2]
    return year


def get_day(accident_date):
    day = accident_date.split("/")
    day = day[1]
    return day


def get_month(accident_date):
    month = accident_date.split("/")
    month = month[0]
    return month


jsonPersonFileName = "AllPeople2014-2018-JSONLD.json"
jsonAccidentFileName = "AllAccidents2014-2018-JSONLD.json"
contextValue = "http://schema.org/"

csvPersonFile = open(accImp.completePersonsCSVFile+".csv", 'r')
csvAccidentFile = open(accImp.numericalCSVFile+".csv", 'r')

jsonPersonFile = open(jsonPersonFileName, 'w')
jsonAccidentFile = open(jsonAccidentFileName, 'w')


print("Person to JSON-LD")
with open(accImp.completePersonsCSVFile+".csv", "rb") as currentFile:
    reader = csv.reader(currentFile)
    firstLine = next(reader)
    fieldnames = firstLine
    reader = csv.DictReader(csvPersonFile, fieldnames)
    next(reader)
    jsonPersonFile.write("[")
    for row in reader:
        del row['Unnamed: 27']
        del row['Unnamed: 32']
        row["@context"] = contextValue
        row["@type"] = "Person"
        row["@id"] = row["Crash_ID"]
        json.dump(row, jsonPersonFile, indent=4, sort_keys=True)
        jsonPersonFile.write(',\n')
    jsonPersonFile.write("{}]")
print("Person to JSON-LD Complete")

print("Accident to JSON-LD")
with open(accImp.numericalCSVFile+".csv", "rb") as currentFile:
    reader = csv.reader(currentFile)
    firstLine = next(reader)
    fieldnames = firstLine
    reader = csv.DictReader(csvAccidentFile, fieldnames)
    next(reader)
    jsonAccidentFile.write("[")
    for row in reader:
        del row['']
        row["@context"] = contextValue
        row["@type"] = "Accident"
        row["@id"] = row["Crash_ID"]
        row["Crash_Year"] = get_year(row["Crash_Date"])
        row["Crash_Month"] = get_month(row["Crash_Date"])
        row["Crash_Day"] = get_day(row["Crash_Date"])
        json.dump(row, jsonAccidentFile, indent=4, sort_keys=True)
        jsonAccidentFile.write(',\n')
    jsonAccidentFile.write("{}]")
print("Accident to JSON-LD Complete")

endTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
totalTime = (endTime-startTime)/60
print("End Time Seconds: ", startTime)
print("Total Time: ", totalTime)
print("Local Time: ", localTime)



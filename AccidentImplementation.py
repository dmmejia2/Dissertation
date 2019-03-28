# -*- coding: utf-8 -*-
#########################################
# Author = Daniel Mejia                 #
# Email = "dmmejia2@miners.utep.edu     #
# Copyright = Copyright 2019            #
# The University of Texas at El Paso    #
# License = Common Creative License     #
#########################################


import csv
import pandas as pd
import time

print("AccidentImplementation.py")
startTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
print("Start Time Seconds: ", startTime)
print("Local Time: ", localTime)

rawDataPrefix = "//Users//danielmejia//Documents//Ph.D.//Incident Data//"
modifiedDataPrefix = "//Users//danielmejia//Documents//workspace//IncidentImplement//"


removeIncidentColumnFile = "//Users//danielmejia//Documents//Ph.D.//CrashRemoveColumns.csv"
allAccidentsCSVFile = "AllAccidents2014-2018"
numericalCSVFile = "AllAccidentsNumerical2014-2018"
primaryPersonsCSVFile = "AllPrimaryPersons2014-2018"
secondaryPersonsCSVFile = "AllSecondaryPersons2014-2018"
completePersonsCSVFile = "CompletePersons2014-2018"

incidentDataFileA14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 A//TEX Public Incidents 2014 A Crash.csv"
incidentDataFileB14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 B//TEX Public Incidents 2014 B Crash.csv"
incidentDataFileC14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 C//TEX Public Incidents 2014 C Crash.csv"
incidentDataFileD14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 D//TEX Public Incidents 2014 D Crash.csv"
incidentDataFileE14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 E//TEX Public Incidents 2014 E Crash.csv"
incidentDataFileF14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 F//TEX Public Incidents 2014 F Crash.csv"


incidentDataFileA15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 A//TEX Public Incidents 2015 A Crash.csv"
incidentDataFileB15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 B//TEX Public Incidents 2015 B Crash.csv"
incidentDataFileC15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 C//TEX Public Incidents 2015 C Crash.csv"
incidentDataFileD15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 D//TEX Public Incidents 2015 D Crash.csv"
incidentDataFileE15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 E//TEX Public Incidents 2015 E Crash.csv"
incidentDataFileF15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 F//TEX Public Incidents 2015 F Crash.csv"
incidentDataFileG15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 G//TEX Public Incidents 2015 G Crash.csv"


incidentDataFileA16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 A//TEX Public Incidents 2016 A Crash.csv"
incidentDataFileB16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 B//TEX Public Incidents 2016 B Crash.csv"
incidentDataFileC16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 C//TEX Public Incidents 2016 C Crash.csv"
incidentDataFileD16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 D//TEX Public Incidents 2016 D Crash.csv"
incidentDataFileE16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 E//TEX Public Incidents 2016 E Crash.csv"
incidentDataFileF16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 F//TEX Public Incidents 2016 F Crash.csv"
incidentDataFileG16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 G//TEX Public Incidents 2016 G Crash.csv"


incidentDataFileA17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 A//TEX Public Incidents 2017 A Crash.csv"
incidentDataFileB17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 B//TEX Public Incidents 2017 B Crash.csv"
incidentDataFileC17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 C//TEX Public Incidents 2017 C Crash.csv"
incidentDataFileD17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 D//TEX Public Incidents 2017 D Crash.csv"
incidentDataFileE17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 E//TEX Public Incidents 2017 E Crash.csv"
incidentDataFileF17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 F//TEX Public Incidents 2017 F Crash.csv"
incidentDataFileG17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 G//TEX Public Incidents 2017 G Crash.csv"


incidentDataFileA18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 A//TEX Public Incidents 2018 A Crash.csv"
incidentDataFileB18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 B//TEX Public Incidents 2018 B Crash.csv"
incidentDataFileC18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 C//TEX Public Incidents 2018 C Crash.csv"
incidentDataFileD18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 D//TEX Public Incidents 2018 D Crash.csv"
incidentDataFileE18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 E//TEX Public Incidents 2018 E Crash.csv"
incidentDataFileF18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 F//TEX Public Incidents 2018 F Crash.csv"
incidentDataFileG18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 G//TEX Public Incidents 2018 G Crash.csv"


incidentQueueList = list(())
incidentQueueList.append(incidentDataFileA14)
incidentQueueList.append(incidentDataFileB14)
incidentQueueList.append(incidentDataFileC14)
incidentQueueList.append(incidentDataFileD14)
incidentQueueList.append(incidentDataFileE14)
incidentQueueList.append(incidentDataFileF14)

incidentQueueList.append(incidentDataFileA15)
incidentQueueList.append(incidentDataFileB15)
incidentQueueList.append(incidentDataFileC15)
incidentQueueList.append(incidentDataFileD15)
incidentQueueList.append(incidentDataFileE15)
incidentQueueList.append(incidentDataFileF15)
incidentQueueList.append(incidentDataFileG15)

incidentQueueList.append(incidentDataFileA16)
incidentQueueList.append(incidentDataFileB16)
incidentQueueList.append(incidentDataFileC16)
incidentQueueList.append(incidentDataFileD16)
incidentQueueList.append(incidentDataFileE16)
incidentQueueList.append(incidentDataFileF16)
incidentQueueList.append(incidentDataFileG16)

incidentQueueList.append(incidentDataFileA17)
incidentQueueList.append(incidentDataFileB17)
incidentQueueList.append(incidentDataFileC17)
incidentQueueList.append(incidentDataFileD17)
incidentQueueList.append(incidentDataFileE17)
incidentQueueList.append(incidentDataFileF17)
incidentQueueList.append(incidentDataFileG17)

incidentQueueList.append(incidentDataFileA18)
incidentQueueList.append(incidentDataFileB18)
incidentQueueList.append(incidentDataFileC18)
incidentQueueList.append(incidentDataFileD18)
incidentQueueList.append(incidentDataFileE18)
incidentQueueList.append(incidentDataFileF18)
incidentQueueList.append(incidentDataFileG18)

incidentData = []
crashRemoveColumnValue = []
crashRemoveColumnIndex = []

removePersonColumnFile = "//Users//danielmejia//Documents//Ph.D.//CrashRemoveColumns.csv"

primePersonDataFileA14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 A//TEX Public Incidents 2014 A PrimaryPerson.csv"
primePersonDataFileB14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 B//TEX Public Incidents 2014 B PrimaryPerson.csv"
primePersonDataFileC14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 C//TEX Public Incidents 2014 C PrimaryPerson.csv"
primePersonDataFileD14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 D//TEX Public Incidents 2014 D PrimaryPerson.csv"
primePersonDataFileE14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 E//TEX Public Incidents 2014 E PrimaryPerson.csv"
primePersonDataFileF14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 F//TEX Public Incidents 2014 F PrimaryPerson.csv"

primePersonDataFileA15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 A//TEX Public Incidents 2015 A PrimaryPerson.csv"
primePersonDataFileB15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 B//TEX Public Incidents 2015 B PrimaryPerson.csv"
primePersonDataFileC15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 C//TEX Public Incidents 2015 C PrimaryPerson.csv"
primePersonDataFileD15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 D//TEX Public Incidents 2015 D PrimaryPerson.csv"
primePersonDataFileE15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 E//TEX Public Incidents 2015 E PrimaryPerson.csv"
primePersonDataFileF15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 F//TEX Public Incidents 2015 F PrimaryPerson.csv"
primePersonDataFileG15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 G//TEX Public Incidents 2015 G PrimaryPerson.csv"

primePersonDataFileA16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 A//TEX Public Incidents 2016 A PrimaryPerson.csv"
primePersonDataFileB16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 B//TEX Public Incidents 2016 B PrimaryPerson.csv"
primePersonDataFileC16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 C//TEX Public Incidents 2016 C PrimaryPerson.csv"
primePersonDataFileD16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 D//TEX Public Incidents 2016 D PrimaryPerson.csv"
primePersonDataFileE16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 E//TEX Public Incidents 2016 E PrimaryPerson.csv"
primePersonDataFileF16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 F//TEX Public Incidents 2016 F PrimaryPerson.csv"
primePersonDataFileG16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 G//TEX Public Incidents 2016 G PrimaryPerson.csv"

primePersonDataFileA17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 A//TEX Public Incidents 2017 A PrimaryPerson.csv"
primePersonDataFileB17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 B//TEX Public Incidents 2017 B PrimaryPerson.csv"
primePersonDataFileC17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 C//TEX Public Incidents 2017 C PrimaryPerson.csv"
primePersonDataFileD17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 D//TEX Public Incidents 2017 D PrimaryPerson.csv"
primePersonDataFileE17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 E//TEX Public Incidents 2017 E PrimaryPerson.csv"
primePersonDataFileF17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 F//TEX Public Incidents 2017 F PrimaryPerson.csv"
primePersonDataFileG17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 G//TEX Public Incidents 2017 G PrimaryPerson.csv"

primePersonDataFileA18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 A//TEX Public Incidents 2018 A PrimaryPerson.csv"
primePersonDataFileB18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 B//TEX Public Incidents 2018 B PrimaryPerson.csv"
primePersonDataFileC18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 C//TEX Public Incidents 2018 C PrimaryPerson.csv"
primePersonDataFileD18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 D//TEX Public Incidents 2018 D PrimaryPerson.csv"
primePersonDataFileE18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 E//TEX Public Incidents 2018 E PrimaryPerson.csv"
primePersonDataFileF18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 F//TEX Public Incidents 2018 F PrimaryPerson.csv"
primePersonDataFileG18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 G//TEX Public Incidents 2018 G PrimaryPerson.csv"

primePersonQueueList = list(())
primePersonQueueList.append(primePersonDataFileA14)
primePersonQueueList.append(primePersonDataFileB14)
primePersonQueueList.append(primePersonDataFileC14)
primePersonQueueList.append(primePersonDataFileD14)
primePersonQueueList.append(primePersonDataFileE14)
primePersonQueueList.append(primePersonDataFileF14)

primePersonQueueList.append(primePersonDataFileA15)
primePersonQueueList.append(primePersonDataFileB15)
primePersonQueueList.append(primePersonDataFileC15)
primePersonQueueList.append(primePersonDataFileD15)
primePersonQueueList.append(primePersonDataFileE15)
primePersonQueueList.append(primePersonDataFileF15)
primePersonQueueList.append(primePersonDataFileG15)

primePersonQueueList.append(primePersonDataFileA16)
primePersonQueueList.append(primePersonDataFileB16)
primePersonQueueList.append(primePersonDataFileC16)
primePersonQueueList.append(primePersonDataFileD16)
primePersonQueueList.append(primePersonDataFileE16)
primePersonQueueList.append(primePersonDataFileF16)
primePersonQueueList.append(primePersonDataFileG16)

primePersonQueueList.append(primePersonDataFileA17)
primePersonQueueList.append(primePersonDataFileB17)
primePersonQueueList.append(primePersonDataFileC17)
primePersonQueueList.append(primePersonDataFileD17)
primePersonQueueList.append(primePersonDataFileE17)
primePersonQueueList.append(primePersonDataFileF17)
primePersonQueueList.append(primePersonDataFileG17)

primePersonQueueList.append(primePersonDataFileA18)
primePersonQueueList.append(primePersonDataFileB18)
primePersonQueueList.append(primePersonDataFileC18)
primePersonQueueList.append(primePersonDataFileD18)
primePersonQueueList.append(primePersonDataFileE18)
primePersonQueueList.append(primePersonDataFileF18)
primePersonQueueList.append(primePersonDataFileG18)

personData = []
removePersonColumnValue = []
removePersonColumnIndex = []


secPersonDataFileA14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 A//TEX Public Incidents 2014 A Person.csv"
secPersonDataFileB14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 B//TEX Public Incidents 2014 B Person.csv"
secPersonDataFileC14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 C//TEX Public Incidents 2014 C Person.csv"
secPersonDataFileD14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 D//TEX Public Incidents 2014 D Person.csv"
secPersonDataFileE14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 E//TEX Public Incidents 2014 E Person.csv"
secPersonDataFileF14 = rawDataPrefix + "TEX Incidents 2014//TEX Incidents 2014 F//TEX Public Incidents 2014 F Person.csv"

secPersonDataFileA15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 A//TEX Public Incidents 2015 A Person.csv"
secPersonDataFileB15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 B//TEX Public Incidents 2015 B Person.csv"
secPersonDataFileC15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 C//TEX Public Incidents 2015 C Person.csv"
secPersonDataFileD15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 D//TEX Public Incidents 2015 D Person.csv"
secPersonDataFileE15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 E//TEX Public Incidents 2015 E Person.csv"
secPersonDataFileF15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 F//TEX Public Incidents 2015 F Person.csv"
secPersonDataFileG15 = rawDataPrefix + "TEX Incidents 2015//TEX Incidents 2015 G//TEX Public Incidents 2015 G Person.csv"

secPersonDataFileA16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 A//TEX Public Incidents 2016 A Person.csv"
secPersonDataFileB16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 B//TEX Public Incidents 2016 B Person.csv"
secPersonDataFileC16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 C//TEX Public Incidents 2016 C Person.csv"
secPersonDataFileD16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 D//TEX Public Incidents 2016 D Person.csv"
secPersonDataFileE16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 E//TEX Public Incidents 2016 E Person.csv"
secPersonDataFileF16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 F//TEX Public Incidents 2016 F Person.csv"
secPersonDataFileG16 = rawDataPrefix + "TEX Incidents 2016//TEX Incidents 2016 G//TEX Public Incidents 2016 G Person.csv"

secPersonDataFileA17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 A//TEX Public Incidents 2017 A Person.csv"
secPersonDataFileB17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 B//TEX Public Incidents 2017 B Person.csv"
secPersonDataFileC17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 C//TEX Public Incidents 2017 C Person.csv"
secPersonDataFileD17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 D//TEX Public Incidents 2017 D Person.csv"
secPersonDataFileE17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 E//TEX Public Incidents 2017 E Person.csv"
secPersonDataFileF17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 F//TEX Public Incidents 2017 F Person.csv"
secPersonDataFileG17 = rawDataPrefix + "TEX Incidents 2017//TEX Incidents 2017 G//TEX Public Incidents 2017 G Person.csv"

secPersonDataFileA18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 A//TEX Public Incidents 2018 A Person.csv"
secPersonDataFileB18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 B//TEX Public Incidents 2018 B Person.csv"
secPersonDataFileC18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 C//TEX Public Incidents 2018 C Person.csv"
secPersonDataFileD18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 D//TEX Public Incidents 2018 D Person.csv"
secPersonDataFileE18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 E//TEX Public Incidents 2018 E Person.csv"
secPersonDataFileF18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 F//TEX Public Incidents 2018 F Person.csv"
secPersonDataFileG18 = rawDataPrefix + "TEX Incidents 2018//TEX Incidents 2018 G//TEX Public Incidents 2018 G Person.csv"


secPersonQueueList = list(())
secPersonQueueList.append(secPersonDataFileA14)
secPersonQueueList.append(secPersonDataFileB14)
secPersonQueueList.append(secPersonDataFileC14)
secPersonQueueList.append(secPersonDataFileD14)
secPersonQueueList.append(secPersonDataFileE14)
secPersonQueueList.append(secPersonDataFileF14)

secPersonQueueList.append(secPersonDataFileA15)
secPersonQueueList.append(secPersonDataFileB15)
secPersonQueueList.append(secPersonDataFileC15)
secPersonQueueList.append(secPersonDataFileD15)
secPersonQueueList.append(secPersonDataFileE15)
secPersonQueueList.append(secPersonDataFileF15)
secPersonQueueList.append(secPersonDataFileG15)

secPersonQueueList.append(secPersonDataFileA16)
secPersonQueueList.append(secPersonDataFileB16)
secPersonQueueList.append(secPersonDataFileC16)
secPersonQueueList.append(secPersonDataFileD16)
secPersonQueueList.append(secPersonDataFileE16)
secPersonQueueList.append(secPersonDataFileF16)
secPersonQueueList.append(secPersonDataFileG16)

secPersonQueueList.append(secPersonDataFileA17)
secPersonQueueList.append(secPersonDataFileB17)
secPersonQueueList.append(secPersonDataFileC17)
secPersonQueueList.append(secPersonDataFileD17)
secPersonQueueList.append(secPersonDataFileE17)
secPersonQueueList.append(secPersonDataFileF17)
secPersonQueueList.append(secPersonDataFileG17)

secPersonQueueList.append(secPersonDataFileA18)
secPersonQueueList.append(secPersonDataFileB18)
secPersonQueueList.append(secPersonDataFileC18)
secPersonQueueList.append(secPersonDataFileD18)
secPersonQueueList.append(secPersonDataFileE18)
secPersonQueueList.append(secPersonDataFileF18)
secPersonQueueList.append(secPersonDataFileG18)

secPersonData = []
removeSecPersonColumnValue = []
removeSecPersonColumnIndex = []


# Reads all of the items from the CSV files
def read_files(list_queue, data_store):
    while list_queue:

        temp_file = list_queue.pop(0)
        # print(temp_file)
        with open(temp_file, "rb") as currentFile:
            reader = csv.reader(currentFile)
            for row in reader:
                # print(row)
                data_store.append(row)
    return data_store


# Sets the unwanted columns
def remove_column_values(remove_column_file, data_store):
    with open(remove_column_file, "rb") as remove_column:
        reader = csv.reader(remove_column)
        for row in reader:
            for column in row:
                data_store.append(column)
            # print(value)
    return data_store


# Determines unwanted column indices
def remove_column_index(column_values, index_data_store, full_data):
    for i in column_values:
        index_remove = 0
        for j in full_data[0]:
            if i == j:
                index_data_store.append(index_remove)
                break
            index_remove += 1
    return index_data_store


# Sets data that is unwanted for removal
def remove_unwanted_data(full_data_set, remove_index):
    temp_data_set = list(full_data_set)
    full_data_set = []
    for i in range(len(temp_data_set)):
        tempRow = temp_data_set[i]
        for j in remove_index:
            tempRow[j] = "*REMOVE*"
        full_data_set.append(tempRow)
    return full_data_set


# Creates the file without the unwanted data
def create_csv_file(file_name, full_data_set):
    # Creates a new file with all data
    file = open(file_name+".csv", "w+")
    iteration_number = 0
    for dataSet in full_data_set:
        for data_point in dataSet:
            if data_point == "Crash_ID" and iteration_number != 0:
                break
            elif data_point == "*REMOVE*":
                continue
            file.write(data_point)
            file.write(",")
        file.write("\n")
        # print(iteration_number)
        iteration_number += 1
    file.close()


# Creates a new file with all numerical data
def create_numerical_csv_file(file_name, full_data_set):
    file = open(file_name + ".csv", "w+")
    iteration_number = 0
    for dataSet in full_data_set:
        for data_point in dataSet:
            if data_point == "Crash_ID" and iteration_number != 0:
                break
            elif data_point == "*REMOVE*":
                continue

            current_data_point = data_point

            if current_data_point == "SUN":
                data_point = "0"
            elif current_data_point == "MON":
                data_point = "1"
            elif current_data_point == "TUE":
                data_point = "2"
            elif current_data_point == "WED":
                data_point = "3"
            elif current_data_point == "THU":
                data_point = "4"
            elif current_data_point == "FRI":
                data_point = "5"
            elif current_data_point == "SAT":
                data_point = "6"
            elif current_data_point == "Y":
                data_point = "1"
            elif current_data_point == "N":
                data_point = "0"
            elif ":" in current_data_point and current_data_point not in "MM:":
                data_point = parse_time(current_data_point)

            file.write(data_point)
            file.write(",")
        file.write("\n")
        iteration_number += 1
    file.close()


# Parses time inputs
def parse_time(input_time):
    current_time = input_time.split(":")
    minutes = current_time[1].split(" ")
    updated_time = ""
    if len(minutes) == 2:
        parsed_hour = int(current_time[0])

        if parsed_hour < 12 and minutes[1] == "PM":
            parsed_hour += 12
            updated_hour = str(parsed_hour)
        else:
            updated_hour = str(parsed_hour)

        if parsed_hour == 12 and minutes[1] == "AM":
            updated_hour = "00"

        if parsed_hour < 10:
            updated_hour = "0"+str(parsed_hour)

        updated_time = updated_hour+":"+minutes[0]
    return updated_time


print("Accidents to CSV")
incidentData = read_files(incidentQueueList,incidentData)
crashRemoveColumnValue = remove_column_values(removeIncidentColumnFile, crashRemoveColumnValue)
crashRemoveColumnIndex = remove_column_index(crashRemoveColumnValue, crashRemoveColumnIndex, incidentData)
incidentData = remove_unwanted_data(incidentData, crashRemoveColumnIndex)
create_csv_file(allAccidentsCSVFile, incidentData)
create_numerical_csv_file(numericalCSVFile, incidentData)
print("Accidents to CSV Complete")


print("Persons to CSV")
personData = read_files(primePersonQueueList, personData)
removePersonColumnValue = remove_column_values(removePersonColumnFile, removePersonColumnValue)
removePersonColumnIndex = remove_column_index(removePersonColumnValue, removePersonColumnIndex, personData)
personData = remove_unwanted_data(personData, removePersonColumnIndex)
create_csv_file(primaryPersonsCSVFile, personData)
print("Persons to CSV Complete")


print("Secondary Persons to CSV")
secPersonData = read_files(secPersonQueueList, secPersonData)
removeSecPersonColumnValue = remove_column_values(removePersonColumnFile, removeSecPersonColumnValue)
removeSecPersonColumnIndex = remove_column_index(removeSecPersonColumnValue, removeSecPersonColumnIndex, secPersonData)
secPersonData = remove_unwanted_data(secPersonData, removeSecPersonColumnIndex)
create_csv_file(secondaryPersonsCSVFile, secPersonData)
print("Secondary Persons to CSV Complete")


print("File Combine")
filenames = []
filenames.append(primaryPersonsCSVFile+".csv")
filenames.append(secondaryPersonsCSVFile+".csv")
# filenames.append("AllAccidentsNumerical.csv")
combined_csv = pd.concat([pd.read_csv(f) for f in filenames])
combined_csv.to_csv((completePersonsCSVFile+".csv"), index=False)
print("File Combine Complete")


endTime = time.time()
localTime = time.asctime(time.localtime(time.time()))
totalTime = (endTime-startTime)/60
print("End Time Seconds: ", startTime)
print("Total Time: ", totalTime)
print("Local Time: ", localTime)

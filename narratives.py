# -*- coding: utf-8 -*-
#########################################
# Author = Daniel Mejia                 #
# Email = "dmmejia2@miners.utep.edu     #
# Copyright = Copyright 2019            #
# The University of Texas at El Paso    #
# License = Common Creative License     #
#########################################

import csv
import pymongo
from pymongo import MongoClient
import pprint as pp
import codecs

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

db = client.accidents
collection = db.event
narrative_lookup_file = "//Users//danielmejia//Documents//Ph.D.//NarrativeLookup.csv"

query = collection.find({"Crash_ID": "15127925"})


# Reads all of the items from the CSV files
def read_file(narrative_file, data_store):
        with codecs.open(narrative_file, "rb", encoding="utf-8-sig") as currentFile:
            reader = csv.reader(currentFile)
            for row in reader:
                # print(row)
                data_store.append(row)
            return data_store


for results in query:
    del results['_id']
    # print(results)
    # pp.pprint(results)
    # print(results['CompositeIndex'])


lookup_table = list(())
lookup_table = read_file(narrative_lookup_file, lookup_table)

for value in lookup_table:
    if value[0] == "Active_School_Zone_Fl":
        if value[1] == results['Active_School_Zone_Fl']:
            active_school_zone = value[2]

    if value[0] == "At_Intrsct_Fl":
        if value[1] == results['At_Intrsct_Fl']:
            intersection = value[2]

    if value[0] == "City_ID":
        if value[1] == results['City_ID']:
            city = value[2]

    if value[0] == "Cmv_Involv_Fl":
        if value[1] == results['Cmv_Involv_Fl']:
            cmv = value[2]

    if value[0] == "Cnty_ID":
        if value[1] == results['Cnty_ID']:
            county = value[2]

    if value[0] == "Crash_Fatal_Fl":
        if value[1] == results['Crash_Fatal_Fl']:
            crash_fatal = value[2]

    if value[0] == "Harm_Evnt_ID":
        if value[1] == results['Harm_Evnt_ID']:
            harm_event = value[2]

    if value[0] == "Light_Cond_ID":
        if value[1] == results['Light_Cond_ID']:
            light = value[2]

    if value[0] == "Obj_Struck_ID":
        if value[1] == results['Obj_Struck_ID']:
            obj_struck = value[2]

    if value[0] == "Road_Constr_Zone_Fl":
        if value[1] == results['Road_Constr_Zone_Fl']:
            construction_zone = value[2]

    if value[0] == "Road_Constr_Zone_Wrkr_Fl":
        if value[1] == results['Road_Constr_Zone_Fl']:
            construction_worker = value[2]

    if value[0] == "Road_Type_ID":
        if value[1] == results['Road_Type_ID']:
            road_type = value[2]

    if value[0] == "Rr_Relat_Fl":
        if value[1] == results['Rr_Relat_Fl']:
            rail = value[2]

    if value[0] == "Schl_Bus_Fl":
        if value[1] == results['Schl_Bus_Fl']:
            bus = value[2]

    if value[0] == "Surf_Cond_ID":
        if value[1] == results['Surf_Cond_ID']:
            surface = value[2]

    if value[0] == "Thousand_Damage_Fl":
        if value[1] == results['Thousand_Damage_Fl']:
            damage = value[2]

    if value[0] == "Wthr_Cond_ID":
        if value[1] == results['Wthr_Cond_ID']:
            weather = value[2]


crash_id = results['Crash_ID'];
crash_date = results['Crash_Date']
crash_time = results['Crash_Time']
composite_index = str(results['CompositeIndex'])
lat = str(results['Latitude'])
long = str(results['Longitude'])
serious_count = str(results['Sus_Serious_Injry_Cnt'])
nonincap_count = str(results['Nonincap_Injry_Cnt'])
no_injury_count = str(results['Non_Injry_Cnt'])
unknown_count = str(results['Unkn_Injry_Cnt'])
death_count = str(results['Death_Cnt'])


de_narrative_string =  "The following traffic crash occurred.\n"\
                        "The traffic crash has a Crash_ID of " + crash_id +".\n"\
                        "The crash occurred in " + city + " located in "+ county +" county Texas on "+crash_date+" at "+ crash_time + ". \n"\
                        "The coordinates of the crash are: (" +lat+","+long+").\n"\
                        "The crash occurred on a "+ road_type +" roadway.\n"\
                        "The crash has a Critical Composite Index of: "+composite_index+".\n"\
                        "Was the crash fatal: " + crash_fatal +".\n"\
                        "The crash involved a harmful event including, but not limited to hitting a: "+harm_event+".\n"\
                        "The vehicle " + obj_struck + ".\n"\
                        "The light conditions were reported as: " + light + ".\n"\
                        "The weather conditions were reported to be " + weather +".\n"\
                        "The surface conditions were reported to be " + surface + ".\n"\
                        "Was the crash in an construction zone: " + construction_zone + ".\n"\
                        "Was the crash around construction workers "+ construction_worker + ".\n"\
                        "Was the crash in an active school zone: " + active_school_zone + ".\n"\
                        "Was the crash involve a school bus: " + bus + ".\n"\
                        "Was the crash at an intersection: " + intersection + ".\n"\
                        "Was the crash at railroad: " + rail + ".\n"\
                        "Was a CMV involved: " + cmv + ".\n"\
                        "Did the crash involve at least $1000 in damages: "+damage + ".\n"\
                        "The crash had a total of: " + death_count + " deaths.\n"\
                        "The crash had a total of: " + serious_count + " serious injuries.\n"\
                        "The crash had a total of: " + nonincap_count + " non-incapacitating injuries.\n"\
                        "The crash had a total of: " + no_injury_count + " non-injuries.\n"\
                        "The crash had a total of: " + unknown_count + " unknown injuries.\n"\



nde_narrative_string =  "The following traffic crash occurred.\n"\
                        "The traffic crash has a Crash_ID of " + crash_id +".\n"\
                        "The crash occurred in " + city + " located in "+county+" county Texas on "+ crash_date +" at "+ crash_time + ". \n"\
                        "The crash has a Critical Composite Index of: "+composite_index+".\n"\
                        "Was the crash fatal: " + crash_fatal+ ".\n"\
                        "The light conditions were reported as: "+light+".\n"\
                        "The weather conditions were reported to be " + weather+".\n"\
                        "The surface conditions were reported to be " + surface+".\n"\
                        "Did the crash involve at least $1000 in damages: " + damage + ".\n"\
                        "The crash had a total of: " + death_count + " deaths.\n"\
                        "The crash had a total of: " + serious_count + " serious injuries.\n"\
                        "The crash had a total of: " + nonincap_count + " non-incapacitating injuries.\n"\
                        "The crash had a total of: " + no_injury_count + " non-injuries.\n"\
                        "The crash had a total of: " + unknown_count + " unknown injuries.\n"\


print("Domain Expert")
print(de_narrative_string)
print("")

print("Non-Domain Expert")
print(nde_narrative_string)

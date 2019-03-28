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
import time

start_time = time.time()
local_time = time.asctime(time.localtime(time.time()))
print("Start Time Seconds: ", start_time)
print("Local Time: ", local_time)

weighted_column_file = "//Users//danielmejia//Documents//Ph.D.//ColumnWeightsPython4.csv"
weight_list = list(())
crash_indices = list(())
crash_metrics = list(())
composite_metric_csv_file = "CompositeCrashMetrics2014-2018-FULLFOUR"
json_crashes_file = "AllCrashes2014-2018-JSONLD.json"
context_value = "http://schema.org/"


# Creates the csv file
def create_metric_csv_file(file_name, full_data_set):
    # Creates a new file with all data
    file = open(file_name+".csv", "w+")
    file.write("Crash_ID,CompositeSum,CompositeIndex,NormalizedIndex,")
    file.write("\n")
    for data_set in full_data_set:
        for ind_data_point in data_set:
            file.write(str(ind_data_point))
            file.write(",")
        file.write("\n")
    file.close()


with open(weighted_column_file, "rb") as current_file:
    reader = csv.reader(current_file)
    for row in reader:
        weight_list.append(row)
        # print(row[0])


print("Creating Metrics")
with open(json_crashes_file) as f:
    data = json.load(f)
    max_possible = 1
    for data_point in data:
        composite_sum = 0
        # print(data_point)
        for weight_item in weight_list:
            try:
                if weight_item[0] == "MAX":
                    max_possible = float(weight_item[2])

                elif weight_item[0] == "Crash_Time":
                    temp_hour = data_point[weight_item[0]]
                    temp_hour = temp_hour.split(":")[0]
                    weight_temp_hour = weight_item[1]
                    weight_temp_hour = weight_temp_hour.split(":")[0]
                    hour_diff = int(temp_hour)-int(weight_temp_hour)

                    if hour_diff < 3 and hour_diff >= 0:
                        composite_sum += int(weight_item[2])

                elif "Injry" in weight_item[0] or "Death_Cnt" in weight_item[0]:
                    composite_sum += int(data_point[weight_item[0]]) * int(weight_item[2])

                elif data_point[weight_item[0]] == weight_item[1]:
                    composite_sum += int(weight_item[2])

            except KeyError as err:
                err
        composite_index = float(float(composite_sum)/float(max_possible)) * 100
        # print(data_point["Crash_ID"])
        # print("COMPOSITE SUM: ", composite_sum)
        # print("COMPOSITE INDEX: ", composite_index)
        try:
            current_crash = list((data_point["Crash_ID"], composite_sum, composite_index,))
            crash_indices.append(current_crash)
        except KeyError as err:
            err

print("Metric Creation Complete")

min_value = float('inf')
max_value = float('-inf')
for crash in crash_indices:
    min_value = min(min_value, crash[1])
    max_value = max(max_value, crash[1])


for crash in crash_indices:
    cSum = crash[1]
    normalization = float(float(cSum-min_value)/float(max_value-min_value))*100
    current_crash = list((crash[0], crash[1], crash[2], normalization))
    crash_metrics.append(current_crash)


print("Metric to CSV")
create_metric_csv_file(composite_metric_csv_file, crash_metrics)
print("Metric to CSV Complete")

print("Metric to JSON-LD")
csv_metric_file = open(composite_metric_csv_file+".csv", 'r')
json_metric_file = open(composite_metric_csv_file+'.json', 'w')
with open(composite_metric_csv_file+".csv", "rb") as current_file:
    reader = csv.reader(current_file)
    first_line = next(reader)
    field_names = first_line
    reader = csv.DictReader(csv_metric_file, field_names)
    next(reader)
    json_metric_file.write("[")
    for row in reader:
        del row['']
        row["@context"] = context_value
        row["@type"] = "Metric"
        row["@id"] = row["Crash_ID"]
        row["CompositeSum"] = float(row["CompositeSum"])
        row["CompositeIndex"] = float(row["CompositeIndex"])
        row["NormalizedIndex"] = float(row["NormalizedIndex"])
        json.dump(row, json_metric_file, indent=4, sort_keys=True)
        json_metric_file.write(',\n')
    json_metric_file.write("{}]")

print("Metric to JSON-LD Complete")

end_time = time.time()
local_time = time.asctime(time.localtime(time.time()))
total_time = (end_time-start_time)/60
print("End Time Seconds: ", start_time)
print("Total Time: ", total_time)
print("Local Time: ", local_time)


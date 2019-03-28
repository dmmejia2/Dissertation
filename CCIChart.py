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
from pprint import pprint
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

start_time = time.time()
local_time = time.asctime(time.localtime(time.time()))
print("Start Time Seconds: ", start_time)
print("Local Time: ", local_time)


json_CCI = "/Users/danielmejia/PycharmProjects/IncidentImplementation/CompositeAccidentMetrics2014-2018-FULLFOUR.json"
context_value = "http://schema.org/"
minor_count = 0
moderate_count = 0
major_count = 0
severe_count = 0
with open(json_CCI) as f:
    data = json.load(f)
    for values in data:
        try:
            cci = values["CompositeIndex"]
            if 0 <= cci <= 20:
                minor_count += 1
            if 20 < cci <= 40:
                moderate_count += 1
            if 40 < cci <= 50:
                major_count += 1
            if 50 < cci:
                severe_count += 1
        except KeyError as e:
            print("Error", e)


total = minor_count + moderate_count + major_count + severe_count
print("minor", minor_count)
print("moderate", moderate_count)
print("major", major_count)
print("severe", severe_count)



def autopct_generator(limit):
    """Remove percent on small slices."""
    def inner_autopct(pct):
        return ('%.2f%%' % pct) if pct > limit else ''
    return inner_autopct

x = np.arange(4)
cci_values = [minor_count, moderate_count, major_count, severe_count]

labels = 'Minor', 'Moderate', 'Major', 'Severe'
sizes = [minor_count, moderate_count, major_count, severe_count]
explode = (0, 0, 0, 0)
# only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct=autopct_generator(7),radius=1800, shadow=True, startangle=90)
ax1.axis('equal')

plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 12},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)
# Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
fig1.savefig('/Users/danielmejia/PycharmProjects/IncidentImplementation/CCIRatioFullFour.png')




end_time = time.time()
local_time = time.asctime(time.localtime(time.time()))
total_time = (end_time-start_time)/60
print("End Time Seconds: ", start_time)
print("Total Time: ", total_time)
print("Local Time: ", local_time)

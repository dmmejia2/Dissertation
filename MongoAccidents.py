#from MongoConnect import MongoConnect

import pymongo
from pymongo import MongoClient
import pprint as pp
import json

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

db = client.accidents
collection = db.all


query = collection.aggregate([

   {
      "$lookup":
         {
            "from": "people",
            "localField": "Crash_ID",
            "foreignField": "Crash_ID",
            "as": "people"
        }
   },
   {"$match": {"Crash_ID": "15127925"}}

]);

jsonAccidentFile = open("/Applications/XAMPP/htdocs/IncidentImplementPHD/QueryJSON.json", 'w')

jsonAccidentFile.write("[")
for results in query:
    del results['_id']
    print(len(results['people']))
    if results['people'] is not None:
        for people in results['people']:
            del people['_id']

    # pp.pprint(results)
    # print("")
    json.dump(results, jsonAccidentFile, indent=4, sort_keys=True)
    jsonAccidentFile.write(',\n')
jsonAccidentFile.write("{}]")

# pp.pprint(query.count())



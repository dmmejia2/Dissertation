from datetime import datetime
from elasticsearch import Elasticsearch
import json
from pprint import pprint

'''
es = Elasticsearch()
print("HELLO WORLD")
es.indices.create(index='my-index', ignore=400)

for i in range(0,5):
    es.index(index="mytest", doc_type="_doc", body={"any": "data", "timestamp": i})

res = es.search(index="mytest", doc_type="_doc", body={"query": {"match_all": {}}})
print(res)

'''

es = Elasticsearch()
es.indices.create(index="accidents", ignore=400)

with open("CompositeAccidentMetrics.json") as f:
    data = json.load(f)

    for dataPoint in data:
        #del dataPoint['']
        #print(dataPoint)
        #pprint(dataPoint)
        es.index(index="accidents", id=dataPoint["Crash_ID"], doc_type="_doc", body=dataPoint)
        #pprint(dataPoint)
print("DONE")
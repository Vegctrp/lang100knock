import gzip
import json
import pymongo

outfile="./068result.txt"

client=pymongo.MongoClient('localhost', 27017)
db = client["database064"]
co = db["collection064"]

with open(outfile,"w") as out:
    for i,values in enumerate(co.find({"tags.value":"dance"},sort=[("rating.count",pymongo.DESCENDING)])):
        if i<10:
            print(values,file=out,end="\n\n")
import gzip
import json
import pymongo

client=pymongo.MongoClient('localhost', 27017)
db = client["database064"]
co = db["collection064"]

for i in co.find({"name":"Queen"}):
    print(i)
    print("############################################")


"""
mongo

show dbs
use database064
db.collection064.find({name:'Queen'});
"""
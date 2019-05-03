import gzip
import json
import pymongo

client=pymongo.MongoClient('localhost', 27017)
db = client["database064"]
co = db["collection064"]

artist_oname=input("input : ")

for values in co.find({"aliases.name":artist_oname}):
    print(values)
    print("############################################")

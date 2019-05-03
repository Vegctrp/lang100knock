import gzip
import json
import pymongo

infile="../data/artist.json.gz"
outfile="./064result.txt"

client=pymongo.MongoClient('localhost', 27017)
db = client["database064"]
co = db["collection064"]

buffer_size=10000

with gzip.open(infile,"rt") as gzipreader:
    with open(outfile,"w") as out:
        buffer=[]
        for i,inline in enumerate(gzipreader):
            injson=json.loads(inline)
            print(injson,file=out)
            buffer.append(injson)
            if i%buffer_size==0:
                co.insert_many(buffer)
                print(i)
                buffer=[]
        print("###",len(buffer),i%buffer_size)
        if len(buffer)>0:
            co.insert_many(buffer)
            print(len(buffer))

co.create_index([('name', pymongo.ASCENDING)])
co.create_index([('aliases.name', pymongo.ASCENDING)])
co.create_index([('tags.value', pymongo.ASCENDING)])
co.create_index([('rating.value', pymongo.ASCENDING)])

for i in co.find({"name":"Shabba Ranks"}):
    print(i)
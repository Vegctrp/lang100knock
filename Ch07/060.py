import redis
import gzip
import json

infile="../data/artist.json.gz"
outfile="./060result.txt"
artist_json_out="./artist_json_out.txt"

pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
db = redis.StrictRedis(connection_pool=pool)
"""
db.set("a","b")
print(db.get("a").decode())
"""
with gzip.open(infile,"rt") as gzipreader:
    with open(outfile,"w") as out,open(artist_json_out,"w") as jout:
        for inline in gzipreader:
            injson=json.loads(inline)
            print(injson,file=jout)
            if "name" in injson:
                key=injson.get("name","#")+"\t"+str(injson.get("id",-1))
                value=injson.get("area","#")
                print(key,value,file=out)
                db.set(key.encode(),value.encode())

print(db.get("Shabba Ranks	37082"))
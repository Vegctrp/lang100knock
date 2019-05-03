import redis
import gzip
import json

infile="../data/artist.json.gz"
outfile="./063result.txt"

pool = redis.ConnectionPool(host="localhost", port=6379, db=1)
db = redis.StrictRedis(connection_pool=pool)

with gzip.open(infile,"rt") as gzipreader:
    with open(outfile,"w") as out:
        for inline in gzipreader:
            injson=json.loads(inline)
            if "name" in injson:
                key=injson.get("name","#")+"\t"+str(injson.get("id",-1))
                value=injson.get("tags",[])
                print(key,str(value),file=out)
                db.set(key.encode(),str(value).encode())

print(db.get("Shabba Ranks	37082"))
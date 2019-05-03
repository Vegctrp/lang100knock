import redis

pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
db = redis.StrictRedis(connection_pool=pool)

outfile="062result.txt"

num=0

with open(outfile,"w") as out:
    for key in db.scan_iter():
        if db.get(key).decode()=="Japan":
            print(key,file=out)
            num+=1

print(num)
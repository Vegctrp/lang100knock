import redis

pool = redis.ConnectionPool(host="localhost", port=6379, db=1)
db = redis.StrictRedis(connection_pool=pool)

artist_name=input("input : ")

matching=artist_name+"\t*"
for key in db.scan_iter(match=matching):
    print(key.decode(),db.get(key).decode())
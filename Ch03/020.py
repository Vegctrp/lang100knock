import gzip
import json

ingzip="../data/jawiki-country.json.gz"

with gzip.open(ingzip,"rt") as gzipreader:
    for inline in gzipreader:
        injson=json.loads(inline)
        if(injson["title"]=="イギリス"):
            print(injson["text"])
import gzip
import json
import re

ingzip="../data/jawiki-country.json.gz"

with gzip.open(ingzip,"rt") as gzipreader:
    for inline in gzipreader:
        injson=json.loads(inline)
        if(injson["title"]=="イギリス"):
            wiki_england_json=injson

linelist=wiki_england_json["text"].split("\n")
pattern=r"(?:ファイル|File):(.+?)\|"
repatter=re.compile(pattern)

for line in linelist:
    match=repatter.findall(line)
    if len(match)!=0:
        print(match[0])
import gzip
import json
import re

ingzip="../data/jawiki-country.json.gz"

with gzip.open(ingzip,"rt") as gzipreader:
    for inline in gzipreader:
        injson=json.loads(inline)
        if(injson["title"]=="イギリス"):
            wiki_england_json=injson

text=wiki_england_json["text"].split("\n")
pattern=r"^\|(.+?)\s=\s(.+?)$"
repatter=re.compile(pattern)

dictionary={}
count=0

for line in text:
    match=repatter.findall(line)
    if len(match)!=0:
        dictionary[match[0][0]]=match[0][1]
        count+=1

print(dictionary)
print(len(dictionary))
print(count)
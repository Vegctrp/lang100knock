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
pattern=r"^(=+)\s?(.+?)\s?=+$"
repatter=re.compile(pattern)

"""
match=repatter.findall(wiki_england_json["text"])
for i in match:
    print(i)
"""

for line in linelist:
    match=repatter.findall(line)
    if len(match)!=0:
        print(str(len(match[0][0])-1)+" "+match[0][1])
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

emphasize=r"(\'{2,5})([^\']+?)(\1)"
pat_emphasize=re.compile(emphasize)
internal_link=r"(?<!(?:#REDIRECT ))\[\[(?!Category:)(?:[^\|]+?\|)??([^\|]+?)\]\]"
pat_internal_link=re.compile(internal_link)

for line in text:
    match=repatter.findall(line)
    if len(match)!=0:
        key=pat_emphasize.sub(r"\2",match[0][0])
        value=pat_emphasize.sub(r"\2",match[0][1])
        key=pat_internal_link.sub(r"\1",key)
        value=pat_internal_link.sub(r"\1",value)
        dictionary[key]=value
        count+=1

print(dictionary)
print(len(dictionary))
print(count)
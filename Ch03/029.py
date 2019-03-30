import gzip
import json
import re
import requests

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

file=r"\[\[(.+?)\|.+?\|.+?\]\]"
pat_file=re.compile(file)

def crop(text):
    text=pat_file.sub(r"\1",text)
    return text

for line in text:
    match=repatter.findall(line)
    if len(match)!=0:
        key=crop(match[0][0])
        value=crop(match[0][1])
        dictionary[key]=value
        count+=1

print(dictionary["国旗画像"])

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles":"File:"+dictionary["国旗画像"],
    "iiprop":"url",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

#print(DATA)
print(DATA["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
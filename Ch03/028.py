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
external_link=r"\[(.+?)\]"
pat_external_link=re.compile(external_link)
file=r"\[\[(?:ファイル|File):(.+?)\|.+?\|(.+?)\]\]"
pat_file=re.compile(file)
language=r"\{\{lang\|(?:.+?)\|(.+?)\}\}"
pat_language=re.compile(language)
html_tag=r"\<(.+?)\>"
pat_html_tag=re.compile(html_tag)

def crop(text):
    text=pat_emphasize.sub(r"\2",text)
    text=pat_internal_link.sub(r"\1",text)
    text=pat_file.sub(r"\1 \2",text)
    text=pat_language.sub(r"\1",text)
    text=pat_html_tag.sub(r"",text)
    text=pat_external_link.sub(r" \1",text)
    return text

for line in text:
    match=repatter.findall(line)
    if len(match)!=0:
        key=crop(match[0][0])
        value=crop(match[0][1])
        dictionary[key]=value
        count+=1

for element in dictionary:
    print(element+" "+dictionary[element])
print(len(dictionary))
print(count)
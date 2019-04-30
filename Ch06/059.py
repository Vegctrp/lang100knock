import xml.etree.ElementTree as Etree
import re

infile="../data/nlp.txt.xml"
outfile="./059result.txt"

xml=Etree.parse(infile)
root=xml.getroot()

pattern=r"^\s?\(([A-Z]*?)\s(\(.*)\)\s?$"
bottom=r"^\s?\(([A-Z]*)\s([a-zA-Z]*)\)\s?$"
repatter=re.compile(pattern)
bottom_finder=re.compile(bottom)

def printNP_from_psr(pt):
    bottom_find=bottom_finder.findall(pt)
    if len(bottom_find)==1:
        if bottom_find[0][0]=="NP":
            print("###"+bottom_find[0][1],file=out)
        return [bottom_find[0][1]]
    match=repatter.findall(pt)
    print(match)
    if len(match)==1:
        phrase_type=match[0][0]
        phrase_elements=match[0][1]
        phrase_element=""
        depth=0
        surfaces=[]
        for char in phrase_elements:
            phrase_element+=char
            if char=="(":
                depth+=1
            elif char==")":
                depth-=1
                if depth==0:
                    slist=printNP_from_psr(phrase_element)
                    surfaces.extend(slist)
                    phrase_element=""
        if phrase_type=="NP":
            print(" ".join(surfaces),file=out)
        return surfaces
    return []

num=0
with open(outfile,"w") as out:
    for parse in root.iter("parse"):
        pt=parse.text
        printNP_from_psr(pt)
import xml.etree.ElementTree as Etree

infile="../data/nlp.txt.xml"
outfile="./054result.txt"

xml=Etree.parse(infile)
root=xml.getroot()

sentences=root[0][1]

with open(outfile,"w") as out:
    for sentence in sentences:
        for token in sentence[0]:
            print(token[0].text+"\t"+token[1].text+"\t"+token[4].text,file=out)
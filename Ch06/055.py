import xml.etree.ElementTree as Etree

infile="../data/nlp.txt.xml"
outfile="./055result.txt"

xml=Etree.parse(infile)
root=xml.getroot()

sentences=root[0][1]

with open(outfile,"w") as out:
    for sentence in sentences:
        for token in sentence[0]:
            if token[5].text=="PERSON":
                print(token[0].text,file=out)
import re

infile="../data/nlp.txt"
outfile="./050result.txt"

with open(infile,"r") as intxt:
    str=intxt.read()
    str_d1=re.sub(r'([.;:?!])\s([A-Z])',r"\1\n\2",str)
    str_d2=re.sub(r'\n{2,}',r"\n",str_d1)

with open(outfile,"w") as out:
    print(str_d2,file=out)
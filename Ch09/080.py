import bz2
import re

infile="../data/enwiki-20150112-400-r100-10576.txt.bz2"
outfile="./080result.txt"
pattern=r"^[\.\,\!\?\;\:\)\(\]\[\'\"]*(.+?)[\.\,\!\?\;\:\)\(\]\[\"\']*$"
repatter=re.compile(pattern)

with open(outfile,"w") as out:
    with bz2.open(infile,"rb") as intxt:
        text=intxt.readlines()
        for i,wordline in enumerate(text):
            wordl=wordline.decode()
            token_list=re.split(r"\s",wordl)
            shaped_token_list=[]
            for token in token_list:
                match=repatter.findall(token)
                if len(match)!=0:
                    shaped_token_list.append(match[0])
            print(" ".join(shaped_token_list),file=out)
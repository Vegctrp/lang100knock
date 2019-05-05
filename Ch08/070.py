import tarfile
import json
import codecs
import random

negfile="../data/rt-polaritydata/rt-polarity.neg"
posfile="../data/rt-polaritydata/rt-polarity.pos"
outfile="./sentiment.txt"

with open(outfile,"w") as out:
    with codecs.open(negfile,"r",encoding="utf-8",errors='ignore') as negtxt,codecs.open(posfile,"r",encoding="utf-8",errors='ignore') as postxt:
        neglist=negtxt.readlines()
        poslist=postxt.readlines()
        outlist=[]
        for neg in neglist:
            outlist.append("-1 "+neg)
        for pos in poslist:
            outlist.append("+1 "+pos)
        random.shuffle(outlist)
        for o in outlist:
            print(o,file=out,end="")
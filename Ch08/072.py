import re
import codecs
from stemming.porter2 import stem

negfile="../data/rt-polaritydata/rt-polarity.neg"
posfile="../data/rt-polaritydata/rt-polarity.pos"
outfile="./072result.txt"

use_stopword=["./stopword1.txt","stopword2.txt"]
pattern=re.compile(r"[a-zA-Z']+")

def make_StopWordList(swlist):
    stopword_list=[]
    for file in use_stopword:
        with open(file) as s:
            swlist=pattern.findall(s.read())
            swlist_lower=[stopword.lower() for stopword in swlist]
            stopword_list.extend(swlist_lower)
    stopword_list=list(set(stopword_list))
    return stopword_list

stopword_list=make_StopWordList(use_stopword)

def isStop(word,stopwordlist=stopword_list):
    return word.lower() in stopword_list

def make_reviewWordList():
    with codecs.open(negfile,"r",encoding="utf-8",errors='ignore') as negtxt,codecs.open(posfile,"r",encoding="utf-8",errors='ignore') as postxt:
        neg=negtxt.read()
        pos=postxt.read()
        sentences=neg+" "+pos
        match=pattern.findall(sentences)
        return match

def make_featureWordList(reviewWordList):
    wordlist_ws=[]
    for word in reviewWordList:
        if not (isStop(word) or word==""):
            wordlist_ws.append(stem(word))
    featureWordList=list(set(wordlist_ws))
    return featureWordList


#########################################################################################
featureWordList=make_featureWordList(make_reviewWordList())

with open(outfile,"w") as out:
    for word in featureWordList:
        print(word,file=out)
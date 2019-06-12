import re
import codecs
from stemming.porter2 import stem
import numpy as np
import pickle

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

with open("073-074reg.bin","rb") as reg:
    theta=pickle.load(reg)
with open("073-074wordlist.bin","rb") as wl:
    featureWordList=pickle.load(wl)

print(np.shape(theta))
print(len(featureWordList))

sentence=input("input sentence... : ")
word_list=pattern.findall(sentence)
stem_list=[stem(word) if not isStop(word) else "." for word in word_list]

score=0
for st in stem_list:
    if st==".":
        continue
    elif st in featureWordList:
        score += theta[featureWordList.index(st)+1]
        print(st,theta[featureWordList.index(st)+1])
    else:
        continue

p=1.0/(1.0+np.exp(-score))

print("score :",score)
if score>0:
    print("+1",p)
else:
    print("-1",p)
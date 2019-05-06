import re
import codecs
from stemming.porter2 import stem
import numpy as np

negfile="../data/rt-polaritydata/rt-polarity.neg"
posfile="../data/rt-polaritydata/rt-polarity.pos"
sentiment_file="./sentiment.txt"
outfile="./073result.txt"

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

def make_matrix(featureWordList):
    feature_vecs=[]
    point_vec=[]
    with open(sentiment_file,"r") as sent:
        for line in sent.readlines():
            point=line[0]
            word_list=pattern.findall(line)
            stem_list=[stem(word) if not isStop(word) else "." for word in word_list]
            stem_set=set(stem_list)
            line_vector=[1 if feature in stem_set else 0 for feature in featureWordList]
            feature_vecs.append(line_vector)
            if point=="+":
                point_vec.append("1")
            else:
                point_vec.append("0")
    feature_mat=np.array(feature_vecs,dtype=float)
    point_mat=np.array(point_vec,dtype=float)
    return feature_mat,point_mat,feature_vecs,point_vec

class LogisticRegression():
    def __init__(self,matx,maty,learning_rate,epoch):
        self.trainx=matx
        self.trainy=maty
        #self.theta=np.random.rand(self.trainx.shape[1]+1)
        self.theta=np.zeros(self.trainx.shape[1]+1)
        self.learning_rate=learning_rate
        self.epoch=epoch

    def set_testdata(self,matx,maty):
        self.testx=matx
        self.testy=maty

    def standardize(self):
        mu=self.trainx.mean()
        sigma=self.trainx.std()
        self.trainx=(self.trainx-mu)/sigma

    def add_x0(self):
        x0=np.ones([self.trainx.shape[0],1])
        self.trainx=np.hstack([x0,self.trainx])

    def shapingx(self):
        self.standardize()
        self.add_x0()

    def sigmoid(self,x):
        return 1.0/(1.0+np.exp(-np.dot(x,self.theta)))

    def update_theta(self):
        grad=np.dot(self.trainy-self.sigmoid(self.trainx),self.trainx)/int(np.shape(self.trainy)[0])
        new_theta=self.theta+self.learning_rate*grad
        self.theta=new_theta

    def cost(self):
        m=self.trainx.shape[0]
        h=self.sigmoid(self.trainx)
        j=1/m*np.sum(-self.trainy*np.log(h)-(np.ones(m)-self.trainy)*np.log(np.ones(m)-h))
        return j

    def learning(self):
        for i in range(self.epoch):
            self.update_theta()
            print(i,self.cost())

#########################################################################################
featureWordList=make_featureWordList(make_reviewWordList())
feature_mat,point_mat,feature_vec,point_vec=make_matrix(featureWordList)

lll=LogisticRegression(feature_mat,point_mat,30,900)
#lll.shapingx()
lll.add_x0()
lll.learning()
theta=lll.theta
with open(outfile,"w") as out:
    for i,tt in enumerate(theta.tolist()):
        if i==0:
            print(tt,file=out)
        else:
            print(featureWordList[i-1],tt,file=out)

with open("./073param.txt","w") as paramfile:
    print(",".join(str(num) for num in theta.tolist()),file=paramfile)

with open("./ans.txt","w") as ans:
    for x,y in zip(feature_vec,point_vec):
        x.insert(0,1)
        fv=np.array(x).reshape(1,12088)
        predict=np.dot(fv,theta)
        print(predict,y,file=ans)
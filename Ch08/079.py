import re
import codecs
from stemming.porter2 import stem
import numpy as np
import pickle
import matplotlib.pyplot as plt

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

def make_matrix(featureWordList,i):
    feature_vecs=[]
    point_vec=[]
    test_feature_vec=[]
    test_point_vec=[]
    with open(sentiment_file,"r") as sent:
        length=len(sent.readlines())

    with open(sentiment_file,"r") as sent:
        for k,line in enumerate(sent.readlines()):
            #if length/5*i<=k and length/5*(i+1)>k:
            #    test_sent.append(line)
            #else:
            point=line[0]
            word_list=pattern.findall(line)
            stem_list=[stem(word) if not isStop(word) else "." for word in word_list]
            stem_set=set(stem_list)
            line_vector=[1 if feature in stem_set else 0 for feature in featureWordList]
            if length/5*i<=k and length/5*(i+1)>k:
                test_feature_vec.append(line_vector)
                if point=="+":
                    test_point_vec.append("1")
                else:
                    test_point_vec.append("0")
            else:
                feature_vecs.append(line_vector)
                if point=="+":
                    point_vec.append("1")
                else:
                    point_vec.append("0")
    feature_mat=np.array(feature_vecs,dtype=float)
    point_mat=np.array(point_vec,dtype=float)
    test_feature_mat=np.array(test_feature_vec,dtype=float)
    test_point_mat=np.array(test_point_vec,dtype=float)
    print(np.shape(feature_mat))
    print(np.shape(test_feature_mat))
    return feature_mat,point_mat,test_feature_mat,test_point_mat

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
        xx0=np.ones([self.testx.shape[0],1])
        self.testx=np.hstack([xx0,self.testx])

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

    def test_cost(self):
        m=self.testx.shape[0]
        h=self.sigmoid(self.testx)
        j=1/m*np.sum(-self.testy*np.log(h)-(np.ones(m)-self.testy)*np.log(np.ones(m)-h))
        return j

    def learning(self,num):
        outx=[]
        outy_test=[]
        outy_train=[]
        for i in range(self.epoch):
            self.update_theta()
            traincost=self.cost()
            testcost=self.test_cost()
            outx.append(i+1)
            outy_train.append(traincost)
            outy_test.append(testcost)
            print(str(i)+" train :"+str(traincost)+", test : "+str(testcost))
        #plt.plot(outx,outy_train,color="r",label="train")
        #plt.plot(outx,outy_test,color="b",label="test")
        #plt.legend()
        #plt.savefig("./figure"+str(num)+".png")

#########################################################################################

featureWordList=make_featureWordList(make_reviewWordList())

prec_N=[]
prec_num=[]
rec_N=[]
rec_num=[]
qrat_N=[]
qrat_num=[]

rat=[x for x in range(1,10,1)]
rat2=[x*0.1 for x in range(1,10,1)]

for i in range(5):
    feature_mat,point_mat,test_feature_mat,test_point_mat=make_matrix(featureWordList,i)

    lll=LogisticRegression(feature_mat,point_mat,10,300)
    #lll.shapingx()
    lll.set_testdata(test_feature_mat,test_point_mat)
    lll.add_x0()
    lll.learning(i)
    theta=lll.theta
    for ratio in rat:
        precision_N=0
        precision_num=0
        recall_N=0
        recall_num=0
        qrate_N=0
        qrate_num=0
        for x,y in zip(test_feature_mat,test_point_mat):
            x=np.insert(x,0,1)
            ans_label="1" if y==1.0 else "-1"
            fv=np.array(x).reshape(1,12088)
            predict=lll.sigmoid(fv)
            if predict>ratio/10:
                predict_label="1"
            else:
                predict_label="-1"
            p=predict[0]
            if predict_label=="1":
                precision_N+=1
                if ans_label=="1":
                    precision_num+=1
            if ans_label=="1":
                recall_N+=1
                if predict_label=="1":
                    recall_num+=1
            if ans_label==predict_label:
                qrate_num+=1
            qrate_N+=1
        if i==0:
            prec_N.append(precision_N)
            prec_num.append(precision_num)
            rec_N.append(recall_N)
            rec_num.append(recall_num)
            qrat_N.append(qrate_N)
            qrat_num.append(qrate_num)
        else:
            prec_N[ratio-1]+=precision_N
            prec_num[ratio-1]+=precision_num
            rec_N[ratio-1]+=recall_N
            rec_num[ratio-1]+=recall_num
            qrat_N[ratio-1]+=qrate_N
            qrat_num[ratio-1]+=qrate_num
    
prec=[]
rec=[]
qrat=[]
f1rat=[]

for i in range(9):
    answer_rate=qrat_num[i]/qrat_N[i]
    precision=prec_num[i]/prec_N[i]
    recall=rec_num[i]/rec_N[i]
    F1score=2*(precision*recall)/(precision+recall)

    print("precision : "+str(precision)+", recall : "+str(recall)+", F1score : "+str(F1score))
    prec.append(precision)
    rec.append(recall)
    qrat.append(answer_rate)
    f1rat.append(F1score)

plt.plot(rat2,prec,color="green",label="precision")
plt.plot(rat2,rec,color="blue",label="recall")
plt.plot(rat2,qrat,color="red",label="正解率")
plt.plot(rat2,f1rat,color="black",label="F1score")
plt.legend()
plt.grid(axis='both')
plt.show()
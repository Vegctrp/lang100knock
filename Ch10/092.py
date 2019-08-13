import pickle
import math

def make(matdata,indexdata,outfile):
    with open(matdata, 'rb') as f:
        dmat = pickle.load(f)
    with open(indexdata, 'rb') as f:
        word_list = pickle.load(f)
    word_dict={}
    for i,word in enumerate(word_list):
        word_dict[word]=i
    
    with open("091result.txt","r") as intxt,open(outfile,"w") as out:
        count=1
        while 1:
            if count%10==0:
                print(count)
            count+=1
            line = intxt.readline()
            if not line:
                break
            test_words = line.strip("\n").split(" ")
            if not test_words[0] in word_dict or not test_words[1] in word_dict or not test_words[2] in word_dict:
                print(" ".join(test_words),file=out,end=" ")
                print("-1",file=out)
                continue
            veca = dmat[word_dict[test_words[1]]]
            vecb = dmat[word_dict[test_words[0]]]
            vecc = dmat[word_dict[test_words[2]]]
            vec1=[]
            for a,b,c in zip(veca,vecb,vecc):
                vec1.append(a-b+c)
            word_cos_dict={}
            for word in word_dict:
                index = word_dict[word]
                vec2 = dmat[index]
                al=0
                bl=0
                ab=0
                for i,j in zip(vec1,vec2):
                    al+=i*i
                    bl+=j*j
                    ab+=i*j
                al=math.sqrt(al)
                bl=math.sqrt(bl)
                cos=ab/al/bl
                #print(word,cos)
                word_cos_dict[word]=cos
            word_cos_list = sorted(word_cos_dict.items(),key=lambda x:-x[1])
            print(" ".join(test_words),file=out,end=" ")
            print(word_cos_list[0],file=out)

make("../Ch09/085mat.dat","../Ch09/085wordindex.dat","092result1.txt")
#make("090mat.dat","090wordindex.dat","092result2.txt")
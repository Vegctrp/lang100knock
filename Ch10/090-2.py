import math

dmat=[]
word_dict={}

with open("090vec.txt","r") as intxt:
    line = intxt.readline()
    linelist= line.split(" ")
    word_num=linelist[0]
    context_num=linelist[1]
    line = intxt.readline()
    count=0
    while line:
        linelist = line.split(" ")
        word_dict[linelist[0]]=count
        del linelist[-1]
        del linelist[0]
        linelist = list(map(float,linelist))
        dmat.append(linelist)
        line = intxt.readline()
        count+=1

#print(word_dict)

# 86
print(dmat[word_dict["United_States"]])

# 87
vec1 = dmat[word_dict["United_States"]]
vec2 = dmat[word_dict["U.S"]]

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

print(cos)

# 88
vec1 = dmat[word_dict["England"]]
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

word_cos_dict = sorted(word_cos_dict.items(),key=lambda x:-x[1])

with open("./090result1.txt","w") as out:
    for i,item in enumerate(word_cos_dict):
        if i<20:
            print(item,file=out)

# 89
veca = dmat[word_dict["Spain"]]
vecb = dmat[word_dict["Madrid"]]
vecc = dmat[word_dict["Athens"]]

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

word_cos_dict = sorted(word_cos_dict.items(),key=lambda x:-x[1])

with open("./090result2.txt","w") as out:
    for i,item in enumerate(word_cos_dict):
        if i<20:
            print(item,file=out)
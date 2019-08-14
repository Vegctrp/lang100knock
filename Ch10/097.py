import pickle
import random
import math

def vec_cosine(vec1,vec2):
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
    return cos

def vec_mean(countries):
    return [sum([vecdict[country][i] for country in countries])/len(countries) for i in range(len(vecdict["United_States"]))]

with open("096vecdict.dat", 'rb') as f:
    vecdict = pickle.load(f)

country_list=[]
index=[[],[],[],[],[]]
kinddict={}

k=5
for country in vecdict:
    country_list.append(country)
    begin_cluster=random.randint(0,k-1)
    index[begin_cluster].append(country)
    kinddict[country]=begin_cluster

count=0
while 1:
    count+=1
    if count%1==0:
        print(count)
    change=0
    for country in country_list:
        cosine_list=[vec_cosine(vecdict[country],vec_mean(index[clnum])) for clnum in range(5)]
        if max(cosine_list)==cosine_list[kinddict[country]]:
            continue
        else:
            moveto=cosine_list.index(max(cosine_list))
            index[kinddict[country]].remove(country)
            index[moveto].append(country)
            kinddict[country]=moveto
            change=1
    if change==0:
        break

with open("097result.txt","w") as out:
    for i in range(5):
        for country in index[i]:
            print(str(i)+" "+str(country),file=out)
import pickle
import math

with open('085mat.dat', 'rb') as f:
    dmat = pickle.load(f)

with open('085wordindex.dat', 'rb') as f:
    word_list = pickle.load(f)

with open('085contextindex.dat', 'rb') as f:
    context_list = pickle.load(f)

word_dict={}
for i,word in enumerate(word_list):
    word_dict[word]=i

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

print(cos) # ans : 0.81683...
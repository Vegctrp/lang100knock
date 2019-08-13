from scipy import sparse
from sklearn import decomposition,feature_extraction
import pickle
import math

N=0
with open("./082result.txt","r") as intxt:
    line=intxt.readline()
    while line:
        N+=1
        line=intxt.readline()

with open('083ftc.dat', 'rb') as f:
    ftc_dict = pickle.load(f)

with open('083ft.dat', 'rb') as f:
    ft_dict = pickle.load(f)

with open('083fc.dat', 'rb') as f:
    fc_dict = pickle.load(f)

word_index=[]
word_index_for_search={}
context_index=[]
context_index_for_search={}

for tc in ftc_dict:
    ftc=ftc_dict[tc]
    if ftc_dict[tc]>=10:
        t=tc[0]
        c=tc[1]
        ft=ft_dict[t]
        fc=fc_dict[c]
        ppmi=max(0,math.log(N*ftc/ft/fc))
        if ppmi>0:
            if not t in word_index_for_search:
                word_index.append(t)
                word_index_for_search[t]=len(word_index)-1
            if not c in context_index_for_search:
                context_index.append(c)
                context_index_for_search[c]=len(context_index)-1

sparse_mat = sparse.lil_matrix((len(word_index), len(context_index)))

for tc in ftc_dict:
    ftc=ftc_dict[tc]
    if ftc_dict[tc]>=10:
        t=tc[0]
        c=tc[1]
        ft=ft_dict[t]
        fc=fc_dict[c]
        ppmi=max(0,math.log(N*ftc/ft/fc))
        if ppmi>0:
            sparse_mat[word_index_for_search[t],context_index_for_search[c]]=ppmi

print(word_index_for_search["United_States"])
for i in range(len(context_index)):
    print(sparse_mat[word_index_for_search["United_States"],i])

clf = decomposition.TruncatedSVD(300)
mat = clf.fit_transform(sparse_mat)

print(type(mat))

with open("./085mat.dat","wb") as out:
    pickle.dump(mat,out)

with open("./085wordindex.dat","wb") as out:
    pickle.dump(word_index,out)

with open("./085contextindex.dat","wb") as out:
    pickle.dump(context_index,out)

#print(mat[word_index_for_search["United_States"]])

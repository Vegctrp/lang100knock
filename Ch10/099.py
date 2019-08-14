import pickle
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
#from pandas.tools import plotting

with open("./096mat.dat", 'rb') as f:
    dmat = pickle.load(f)
with open("096wordindex.dat", 'rb') as f:
    word_list = pickle.load(f)
colormap={}
with open("097result.txt","r") as intxt:
    line=intxt.readline()
    while 1:
        line=line.strip("\n").split(" ")
        colormap[line[1]]=int(line[0])
        line=intxt.readline()
        if not line:
            break

mat_reduced = TSNE(n_components=2,random_state=0).fit_transform(dmat)

fig, ax = plt.subplots()
cmap = plt.get_cmap('Set1')
for res in zip(mat_reduced,word_list):
    ax.scatter(res[0][0],res[0][1],marker=".",c="red")
    ax.annotate(res[1], xy=(res[0][0],res[0][1]), color=cmap(colormap[res[1]]))
plt.show()
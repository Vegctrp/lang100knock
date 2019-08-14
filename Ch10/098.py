import pickle
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
#from pandas.tools import plotting

with open("./096mat.dat", 'rb') as f:
    dmat = pickle.load(f)
with open("096wordindex.dat", 'rb') as f:
    word_list = pickle.load(f)
word_dict={}
for i,word in enumerate(word_list):
    word_dict[word]=i

df=pd.DataFrame(dmat,index=word_list)
Z = linkage(df,method="ward",metric="euclidean")
dendrogram(Z,labels=word_list)
plt.title("Dedrogram")
plt.ylabel("Threshold")
plt.show()
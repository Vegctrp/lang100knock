import pickle

with open('085mat.dat', 'rb') as f:
    dmat = pickle.load(f)

with open('085wordindex.dat', 'rb') as f:
    word_list = pickle.load(f)

with open('085contextindex.dat', 'rb') as f:
    context_list = pickle.load(f)

word_dict={}
for i,word in enumerate(word_list):
    word_dict[word]=i

print(dmat[word_dict["United_States"]])
import pickle

country_list=[]
with open("../Ch09/081data.txt","r") as intxt:
    countries=intxt.readlines()
    for country in countries:
        country_tokens=country.split(" ")
        country_list.append("_".join(country_tokens).strip("\n"))

with open("./090mat.dat", 'rb') as f:
    dmat = pickle.load(f)
with open("./090wordindex.dat", 'rb') as f:
    word_list = pickle.load(f)
word_dict={}
for i,word in enumerate(word_list):
    word_dict[word]=i

ans_dict={}
for country in country_list:
    if country in word_dict:
        vec=dmat[word_dict[country]]
        ans_dict[country]=vec
        print(country)

with open("./096vecdict.dat","wb") as out:
    pickle.dump(ans_dict,out)
import pickle

fpair={}
ft={}
fc={}
N=0

def insert_dict(a,dic):
    if not (a in dic):
        dic[a]=1
    else:
        dic[a]=dic[a]+1

with open("./082result.txt","r") as intxt:
    line=intxt.readline()
    while line:
        N+=1
        eles=line.strip().split("\t")
        el1=eles[0]
        el2=eles[1]
        insert_dict((el1,el2),fpair)
        insert_dict(el1,ft)
        insert_dict(el2,fc)
        line=intxt.readline()
        if N%1000000==0:
            print("done "+str(N))

print(N)

with open("./083ftc.dat","wb") as pftc:
    pickle.dump(fpair,pftc)

with open("./083ftc.txt","w") as fftc:
    for i in fpair:
        print(str(i)+"\t"+str(fpair[i]),file=fftc)

print("tc done")

with open("./083ft.dat","wb") as pft:
    pickle.dump(ft,pft)

with open("./083ft.txt","w") as fft:
    for i in ft:
        print(str(i)+"\t"+str(ft[i]),file=fft)

print("t done")

with open("./083fc.dat","wb") as pfc:
    pickle.dump(ft,pfc)

with open("./083fc.txt","w") as ffc:
    for i in fc:
        print(str(i)+"\t"+str(fc[i]),file=ffc)

print("c done")
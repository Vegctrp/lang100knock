import pickle
import math

N=0
with open("./082result.txt","r") as intxt:
    line=intxt.readline()
    while line:
        N+=1
        line=intxt.readline()

print(N)

with open('083ftc.dat', 'rb') as f:
    ftc_dict = pickle.load(f)

with open('083ft.dat', 'rb') as f:
    ft_dict = pickle.load(f)

with open('083fc.dat', 'rb') as f:
    fc_dict = pickle.load(f)

ppmi={}

for tc in ftc_dict:
    ftc=ftc_dict[tc]
    if ftc_dict[tc]>=10:
        t=tc[0]
        c=tc[1]
        ft=ft_dict[t]
        fc=fc_dict[c]
        ppmi[tc]=max(0,math.log(N*ftc/ft/fc))

with open("084result.txt","w") as out:
    for i in ppmi:
        print(str(i)+"\t"+str(ppmi[i]),file=out)
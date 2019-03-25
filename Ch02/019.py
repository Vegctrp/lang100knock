from itertools import groupby

infile="../data/hightemp.txt"

lines=open(infile,"r").readlines()
preflist=[line.split("\t")[0] for line in lines]
preflist.sort()
result=[(pref,len(list(num))) for pref,num in groupby(preflist)]

print(result)
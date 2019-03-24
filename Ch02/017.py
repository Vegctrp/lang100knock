infile="../data/hightemp.txt"

elset=set()
with open(infile,"r") as intxt:
    for line in intxt:
        lineel=line.split("\t")
        elset.add(lineel[0])

#print(elset)
for i in elset:
    print(i)
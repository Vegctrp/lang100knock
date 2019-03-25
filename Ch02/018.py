infile="../data/hightemp.txt"

lines=open(infile,"r").readlines()
lines.sort(key=lambda line:float(line.split("\t")[2]),reverse=True)

for line in lines:
    print(line,end="")
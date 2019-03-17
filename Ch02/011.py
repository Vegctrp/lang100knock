infile="../data/hightemp.txt"
outfile="./hightemp011.txt"
count=0
with open(infile,"r") as indata:
    with open(outfile,"w") as outdata:
        for line in indata:
            print(line.replace("\t"," "),file=outdata,end="")
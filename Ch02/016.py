import sys
import math

args=sys.argv
n=int(args[1])
infile="../data/hightemp.txt"

with open(infile,"r") as intxt:
    inline=intxt.readlines()
    row=len(inline)
    row_per_outfile=math.ceil(row/n)
    for i in range(n):
        with open("./016out"+str(i+1)+".txt","w") as out:
            for j in range(row_per_outfile):
                if i*row_per_outfile+j<row:
                    print(inline[i*row_per_outfile+j],file=out,end="")
import sys

args=sys.argv
infile="../data/hightemp.txt"

with open(infile,"r") as intxt:
    for i in range(int(args[1])):
        print(next(intxt),end="")
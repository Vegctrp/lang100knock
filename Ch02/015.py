import sys

args=sys.argv
infile="../data/hightemp.txt"

with open(infile,"r") as intxt:
    inline=intxt.readlines()
    for line in inline[-int(args[1]):]:
        print(line,end="")
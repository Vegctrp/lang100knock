infile="../data/hightemp.txt"
outfile1="./col1.txt"
outfile2="./col2.txt"

with open(infile,"r") as indata:
    with open(outfile1,"w") as out1:
        with open(outfile2,"w") as out2:
            for line in indata:
                line_list=line.split("\t")
                print(line_list[0],file=out1,end="\n")
                print(line_list[1],file=out2,end="\n")

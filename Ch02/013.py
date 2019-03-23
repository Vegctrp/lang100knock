infile1="./col1.txt"
infile2="./col2.txt"
outfile="./013result.txt"

with open(infile1,"r") as txt1:
    with open(infile2,"r") as txt2:
        with open(outfile,"w") as out:
            for e1,e2 in zip(txt1,txt2):
                print(e1.rstrip()+"\t"+e2.rstrip(),file=out)
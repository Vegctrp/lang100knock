from stemming.porter2 import stem
infile="./051result.txt"
outfile="./052result.txt"

with open(infile) as intxt,open(outfile,"w") as out:
    word_list=intxt.readlines()
    for word in word_list:
        word=word.rstrip("\n")
        print(word+"\t"+stem(word),file=out)
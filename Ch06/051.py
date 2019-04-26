import re
infile="./050result.txt"
outfile="./051result.txt"

with open(infile) as intxt,open(outfile,"w") as out:
    sentences=intxt.readlines()
    for sentence in sentences:
        sentence=sentence.rstrip("\n")
        if sentence!="":
            wordlist=sentence.split(" ")
            for word in wordlist:
                word=re.sub("[^a-zA-Z]","",word)
                print(word,file=out)
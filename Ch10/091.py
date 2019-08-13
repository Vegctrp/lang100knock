# https://github.com/svn2github/word2vec/blob/master/questions-words.txt

with open("../data/questions-words.txt") as intxt, open("./091result.txt","w") as out:
    line=intxt.readline()
    while not line.strip("\n")==": family":
        line=intxt.readline()
    
    line=intxt.readline()
    print(line.strip("\n"),file=out)
    while 1:
        line=intxt.readline()
        if line[0]==":":
            break
        print(line.strip("\n"),file=out)
import random

with open("./081result.txt","r") as res, open("./082result.txt","w") as out:
    tokens_lines=res.readlines()
    for x,line in enumerate(tokens_lines):
        tokens=line.strip().split(" ")
        if len(tokens)<2:
            continue
        for i,token in enumerate(tokens):
            wid=random.randint(1,5)
            begin = max(0,i-wid)
            end = min(len(tokens)-1,i+wid)
            for j in range(begin,i):
                print(token+"\t"+tokens[j],file=out)
            for j in range(i+1,end+1):
                print(token+"\t"+tokens[j],file=out)
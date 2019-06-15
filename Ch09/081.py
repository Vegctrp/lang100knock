with open("./081data.txt","r") as intxt:
    max_length=0
    dictionary={}
    countries=intxt.readlines()
    for country in countries:
        country_tokens=country.split(" ")
        country_tokens[len(country_tokens)-1]=country_tokens[len(country_tokens)-1].strip()
        if len(country_tokens)>=2:
            if len(country_tokens)>max_length:
                max_length=len(country_tokens)
            if country_tokens[0] in dictionary:
                les=dictionary[country_tokens[0]]
                les.append((len(country_tokens)," ".join(country_tokens),"_".join(country_tokens)))
                dictionary[country_tokens[0]]=les
            else:
                dictionary[country_tokens[0]]=[(len(country_tokens)," ".join(country_tokens),"_".join(country_tokens))]

print(dictionary)

with open("./080result.txt","r") as res, open("./081result.txt","w") as out:
    tokens_lines=res.readlines()
    wait=0
    for j,line in enumerate(tokens_lines):
        outlist=[]
        tokens=line.split(" ")
        wait=0
        for i in range(len(tokens)):
            if wait>0:
                wait-=1
                continue
            if not tokens[i] in dictionary:
                outlist.append(tokens[i])
            else:
                for element in dictionary[tokens[i]]:
                    num=element[0]
                    if i+num-1<=len(tokens):
                        st=" ".join(tokens[i:i+num])
                        if element[1]==st:
                            outlist.append(element[2])
                            wait=num-1
                            print("## detect ##",element[2])
                if wait==0:
                    outlist.append(tokens[i])
        outlist[len(outlist)-1]=outlist[len(outlist)-1].strip()
        print(" ".join(outlist),file=out)
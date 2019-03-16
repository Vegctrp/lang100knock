import random

str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans=[]

for word in str.split(" "):
    if len(word)<4:
        ans.append(word)
    else:
        wordlist=[c for c in word[1:-1]]
        random.shuffle(wordlist)
        ans.append(word[0]+"".join(wordlist)+word[-1])

print(' '.join(ans))
def ngram(str, n): #return type: list
    ans=[]
    for i in range(0,len(str)-n+1):
        ans.append(str[i:i+n:1])
    return ans

str="I am an NLPer"

print(ngram(str,2)) #文字bi-gram
print(ngram(str.split(" "),2)) #単語bi-gram
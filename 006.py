def ngram(str, n): #return type: list
    ans=[]
    for i in range(0,len(str)-n+1):
        ans.append(str[i:i+n:1])
    return ans

X=set(ngram("paraparaparadise",2))
Y=set(ngram("paragraph",2))

wa=X|Y
seki=X&Y
sa=X-Y

print(wa)
print(seki)
print(sa)

if(X>={"se"}):
    print("X include se")
else:
    print("X dont include se")
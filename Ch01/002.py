str1="パトカー"
str2="タクシー"

ans=""
for ch1,ch2 in zip(str1,str2):
    ans+=ch1+ch2

print(ans)
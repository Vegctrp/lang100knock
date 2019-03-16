str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
char1=[1, 5, 6, 7, 8, 9, 15, 16, 19]
dictionary={}

for i,word in enumerate(str.split(" "),1):
    if i in char1:
        dictionary[word[0:1]]=i
    else:
        dictionary[word[0:2]]=i

print(dictionary)

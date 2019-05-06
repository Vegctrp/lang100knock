import re

#stopword1 : https://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html
#stopword2 : https://www.textfixer.com/tutorials/common-english-words.txt

with open("stopword1.txt") as s1,open("stopword2.txt") as s2:
    st1=s1.read()
    st2=s2.read()
    wlist1=re.split(r"[\n ]+",st1)
    wlist2=st2.split(",")
    word_list=[word.lower() for word in list(set(wlist1)|set(wlist2))]
    #print(word_list)

def isStop(word):
    return word.lower() in word_list

print(isStop("am"))
print(isStop("bbout"))
print(isStop("Am"))
print(isStop("SINCE"))
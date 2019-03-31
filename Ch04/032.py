#word_dictionary :
#    surface 表層形
#    base 基本形
#    pos 品詞
#    pos1 品詞細分類1

infile="./neko.txt.mecab"
outfile="./032result.txt"

novel_list=[]
with open(infile,"r") as intxt:
    lines=intxt.read()
    for sentence in lines.split("EOS"):
        if sentence!="\n":
            sentence_list=[]
            for word in sentence.split("\n"):
                if word!="":
                    word_dictionary={}
                    word_analysis=word.split("\t")[1].split(",")
                    word_dictionary["surface"]=word.split("\t")[0]
                    word_dictionary["base"]=word_analysis[6]
                    word_dictionary["pos"]=word_analysis[0]
                    word_dictionary["pos1"]=word_analysis[1]
                    sentence_list.append(word_dictionary)
            novel_list.append(sentence_list)

with open(outfile,"w") as out:
    for sentence in novel_list:
        for word in sentence:
            if word["pos"]=="動詞":
                print(word["base"],file=out)
#word_dictionary :
#    surface 表層形
#    base 基本形
#    pos 品詞
#    pos1 品詞細分類1
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='/usr/share/fonts/TakaoPGothic.ttf', size=14)
infile="./neko.txt.mecab"

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

frequency_dictionary={}
for sentence in novel_list:
    for word in sentence:
        if word["surface"] in frequency_dictionary:
            frequency_dictionary[word["surface"]]+=1
        else:
            frequency_dictionary[word["surface"]]=1
sorted_frequency_dictionary=sorted(frequency_dictionary.items(),key=lambda element:element[1],reverse=True)
plot_num=np.arange(10)
plot_data=[]
plot_label=[]
for i in range(10):
    plot_data.append(sorted_frequency_dictionary[i][1])
    plot_label.append(sorted_frequency_dictionary[i][0])
print(plot_label)
plt.bar(plot_num,plot_data,align="center")
plt.title("037")
plt.xticks(plot_num,plot_label, fontproperties=fp)
plt.xlabel("出現頻度が高い10形態素",fontproperties=fp)
plt.ylabel("出現頻度",fontproperties=fp)
plt.show()
import xml.etree.ElementTree as Etree

infile="../data/nlp.txt.xml"
outfile="./056result.txt"

xml=Etree.parse(infile)
root=xml.getroot()

sentences=root[0][1]
corefs=root[0][2]

coref_dict={}

for coref in corefs:
    representative_mention=""
    for mention in coref:
        if representative_mention=="":
            representative_mention=coref[0][4].text
            print("set : "+representative_mention)
        else:
            sentence_num=int(mention[0].text)-1
            word_start_num=int(mention[1].text)-1
            word_end_num=int(mention[2].text)-1
            mention_text=mention[4].text
            key=(sentence_num,word_start_num)
            coref_dict[key]=(representative_mention,mention_text)
            print("key : "+str(key)+" || mention : "+mention_text+" || rep : "+representative_mention)
            for i in range(word_start_num+1,word_end_num):
                key=(sentence_num,i)
                print("key : "+str(key)+" || mention : "+"\"\""+" || rep : "+"\"\"")
                coref_dict[key]=("","")

print(coref_dict)

with open(outfile,"w") as out:
    for sent_num,sentence in enumerate(sentences):
        sentence_list=[]
        for word_num,token in enumerate(sentence[0]):
            key=(sent_num,word_num)
            if key in coref_dict:
                if coref_dict[key]!=("",""):
                    sentence_list.append("###["+coref_dict[key][0]+"]###("+coref_dict[key][1]+")###")
            else:
                sentence_list.append(token[0].text)
        print(" ".join(sentence_list),file=out)
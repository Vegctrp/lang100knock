# cabocha <../data/neko.txt >./neko.txt.cabocha
infile="./neko.txt.cabocha"
outfile="./040result.txt"

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1
    
    def print_morph(self):
        print("##{} {} {} {}##".format(self.surface,self.base,self.pos,self.pos1))
    def printfile_morph(self):
        print("##{} {} {} {}##".format(self.surface,self.base,self.pos,self.pos1),file=out)

novel_list=[]
with open(infile) as intxt:
    lines=intxt.read()
    for sentence in lines.split("EOS"):
        if sentence!="\n":
            sentence_list=[]
            for morph in sentence.split("\n"):
                if morph.split(" ")[0]!="*" and morph!="":
                    morph_analysis=morph.split("\t")[1].split(",")
                    sentence_list.append(Morph(morph.split("\t")[0],morph_analysis[6],morph_analysis[0],morph_analysis[1]))
            novel_list.append(sentence_list)

for morph in novel_list[2]:
    morph.print_morph()

with open(outfile,"w") as out:
    for sentence in novel_list:
        for morph in sentence:
            morph.printfile_morph()
        print("#########################",file=out)
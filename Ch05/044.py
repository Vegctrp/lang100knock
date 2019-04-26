import CaboCha
import pydot

text=input('Input : ')

cabocha=CaboCha.Parser()
line=cabocha.parse(text).toString(CaboCha.FORMAT_LATTICE)

print(line)

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

class Chunk:
    def __init__(self):
        self.morphs=[]
        self.dst=-1
        self.srcs=[]

    def add_morph(self,morph):
        self.morphs.append(morph)

    def add_dst(self,dst):
        self.dst=dst

    def add_src(self,src):
        self.srcs.append(src)

    def print_chunk(self):
        print("Chunk : \n\tmorphs : ")
        for morph in self.morphs:
            print("\t\t",end="")
            morph.print_morph()
        print("\tdst : {}".format(self.dst))
        print("\tsrcs : { ",end="")
        for src in self.srcs:
            print(str(src)+" ",end="")
        print("}")

    def printfile_chunk(self):
        print("Chunk : \n\tmorphs : ",file=out)
        for morph in self.morphs:
            print("\t\t",end="",file=out)
            morph.printfile_morph()
        print("\tdst : {}".format(self.dst),file=out)
        print("\tsrcs : { ",end="",file=out)
        for src in self.srcs:
            print(str(src)+" ",end="",file=out)
        print("}",file=out)

    def surfaces(self):
        surfaces=""
        for morph in self.morphs:
            if morph.pos!="記号":
                surfaces+=morph.surface
        return surfaces

    def include_noun(self):
        ans=False
        for morph in self.morphs:
            if morph.pos=="名詞":
                ans=True
        return ans

    def include_verb(self):
        ans=False
        for morph in self.morphs:
            if morph.pos=="動詞":
                ans=True
        return ans

novel_list=[] #
for sentence in line.split("EOS"):
    if sentence!="\n":
        sentence_list=[] ##
        chunks=sentence.split("* ")
        for i in range(len(chunks)-1):
            a=Chunk()
            sentence_list.append(a)
        for i,chunk in enumerate(chunks):
            for morph in chunk.split("\n"):
                if morph!="":
                    if len(morph.split(" "))==4:
                        chunk_num=int(morph.split(" ")[0])
                        chunk_dst=int(morph.split(" ")[1].replace("D",""))
                        sentence_list[chunk_num].add_dst(chunk_dst)
                        if chunk_dst!=-1:
                            sentence_list[chunk_dst].add_src(chunk_num)
                    else:
                        word_analysis=morph.split("\t")[1].split(",")
                        sentence_list[i-1].add_morph(Morph(morph.split("\t")[0],word_analysis[6],word_analysis[0],word_analysis[1]))
        novel_list.append(sentence_list)

graph=[]
sentence=novel_list[0]
for chunk in sentence:
    src_str=chunk.surfaces()
    if chunk.dst!=-1:
        dst_str=sentence[chunk.dst].surfaces()
    else:
        dst_str=""
    if src_str!="" and dst_str!="":
        graph.append((src_str,dst_str))
        #print(src_str+"\t"+dst_str,file=out)
print(graph)
g=pydot.graph_from_edges(graph,directed=True)
g.write_png("044result.png")
infile="./neko.txt.cabocha"
outfile="./047result.txt"

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
    
    def get_first_verb(self):
        for morph in self.morphs:
            if morph.pos=="動詞":
                return morph
        return Morph("null","null","null","null")

    def get_last_pparticle(self): #助詞
        for morph in self.morphs[::-1]:
            if morph.pos=="助詞":
                return morph
        return Morph("null","null","null","null")

novel_list=[] #
with open(infile) as intxt:
    lines=intxt.read()
    for sentence in lines.split("EOS"):
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

with open(outfile,"w") as out:
    for sentence in novel_list:
        for num,dst_chunk_1 in enumerate(sentence):
            if len(dst_chunk_1.morphs)==2:
                if dst_chunk_1.morphs[0].pos1=="サ変接続" and dst_chunk_1.morphs[1].surface=="を":
                    dst_chunk_2=sentence[dst_chunk_1.dst]
                    verb=dst_chunk_2.get_first_verb()
                    if verb!="null":
                        predicate=dst_chunk_1.surfaces()+verb.base
                        print(predicate)
                        pps=[]
                        chunk_surfaces=[]
                        for ss1 in dst_chunk_1.srcs:
                            src_chunk_1=sentence[ss1]
                            pp=src_chunk_1.get_last_pparticle().base
                            if pp!="null":
                                if not pp in pps:
                                    pps.append(pp)
                                if not src_chunk_1.surfaces() in chunk_surfaces:
                                    chunk_surfaces.append(src_chunk_1.surfaces())
                        for ss2 in dst_chunk_2.srcs:
                            if ss2!=num:
                                src_chunk_2=sentence[ss2]
                                pp=src_chunk_2.get_last_pparticle().base
                                if pp!="null":
                                    if not pp in pps:
                                        pps.append(pp)
                                    if not src_chunk_2.surfaces() in chunk_surfaces:
                                        chunk_surfaces.append(src_chunk_2.surfaces())
                        pps.sort()
                        chunk_surfaces.sort()
                        if len(pps)!=0:
                            print(predicate+"\t"+" ".join(pps)+"\t"+" ".join(chunk_surfaces),file=out)
                        else:
                            print(predicate,file=out)
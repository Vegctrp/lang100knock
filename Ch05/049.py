infile="./neko.txt.cabocha"
outfile="./049result.txt"

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
    
    def surfaces_noun2char(self,char):
        ans=""
        use=False
        for morph in self.morphs:
            if morph.pos=="名詞":
                if not use:
                    ans+=char
            elif morph.pos!="記号":
                ans+=morph.surface
        return ans

def print_path_XY(sentence,path,isclossing):
    begin=path[0]
    end=path[-1]
    for i in path:
        if i==begin:
            if isclossing:
                print(sentence[i].surfaces_noun2char(isclossing),file=out,end="")
            else:
                print(sentence[i].surfaces_noun2char("X"),file=out,end="")
        elif i==end and not isclossing:
            #print(sentence[i].surfaces_noun2char("Y"),file=out,end="")
            print("Y",file=out,end="")
        else:
            print(sentence[i].surfaces(),file=out,end="")
        if i!=end:
            print(" -> ",file=out,end="")
    if not isclossing:
        print("",file=out)

def print_path_crossing(sentence,Xpath,Ypath,k):
    print_path_XY(sentence,Xpath,"X")
    print(" | ",file=out,end="")
    print_path_XY(sentence,Ypath,"Y")
    print(" | ",file=out,end="")
    print(sentence[k].surfaces(),file=out)

def print_path(sentence,morph):
    print(morph.surfaces(),file=out,end="")
    if morph.dst!=-1:
        print(" -> ",file=out,end="")
        print_path(sentence,sentence[morph.dst])
    else:
        print("",file=out)
    return

def detect_path(sentence,chunk_num,path):
    path.append(chunk_num)
    if sentence[chunk_num].dst!=-1:
        detect_path(sentence,sentence[chunk_num].dst,path)
    return

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
        path_dict=[]
        for chunk_num,src_chunk in enumerate(sentence):
            if src_chunk.include_noun():
                path=[]
                detect_path(sentence,chunk_num,path)
                path_dict.append(path)

        for srcX in path_dict:
            for srcY in path_dict:
                if srcX[0]<srcY[0]:
                    setX=set(srcX)
                    setY=set(srcY)
                    if setX>=setY:
                        path=setX-setY
                        path.add(srcY[0])
                        path=list(path)
                        path.sort()
                        print_path_XY(sentence,path,0)
                    else:
                        intersection=list(setX&setY)
                        intersection.sort()
                        k=intersection[0]
                        Xpath=setX-setY
                        Ypath=setY-setX
                        Xpath=list(Xpath)
                        Ypath=list(Ypath)
                        Xpath.sort()
                        Ypath.sort()
                        print_path_crossing(sentence,Xpath,Ypath,k)
        print("################",file=out)
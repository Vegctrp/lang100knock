import xml.etree.ElementTree as Etree

infile="../data/nlp.txt.xml"
outfile="./058result.txt"

xml=Etree.parse(infile)
root=xml.getroot()

num=0
with open(outfile,"w") as out:
    for dependency in root.iter("dependencies"):
        if dependency.attrib["type"]=="collapsed-dependencies":
            num+=1
            dictionary={}
            collapsed_dependencies=dependency
            for dep in collapsed_dependencies:
                if dep.attrib["type"]=="nsubj":
                    predicate=(dep[0].attrib["idx"],dep[0].text)
                    subject=(dep[1].attrib["idx"],dep[1].text)
                    if predicate in dictionary:
                        dictionary[predicate][0].append(subject)
                    else:
                        dictionary[predicate]=[[subject],[]]
                elif dep.attrib["type"]=="dobj":
                    predicate=(dep[0].attrib["idx"],dep[0].text)
                    object=(dep[1].attrib["idx"],dep[1].text)
                    if predicate in dictionary:
                        dictionary[predicate][1].append(object)
                    else:
                        dictionary[predicate]=[[],[object]]
            for key in list(dictionary.keys()):
                element=dictionary[key]
                if len(element[0])*len(element[1])!=0:
                    sub_list=[]
                    obj_list=[]
                    for sub in element[0]:
                        sub_list.append(sub[1])
                    for obj in element[1]:
                        obj_list.append(obj[1])
                    print(",".join(sub_list)+"\t"+key[1]+"\t"+",".join(obj_list),file=out)
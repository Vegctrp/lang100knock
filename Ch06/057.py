import xml.etree.ElementTree as Etree
import pydot

infile="../data/nlp.txt.xml"

xml=Etree.parse(infile)
root=xml.getroot()

num=0
for dependency in root.iter("dependencies"):
    if dependency.attrib["type"]=="collapsed-dependencies":
        num+=1
        graph=pydot.Dot(graph_type="digraph")
        collapsed_dependencies=dependency
        for dep in collapsed_dependencies:
            if dep.attrib["type"]!="punct" and dep.attrib["type"]!="root":
                idx1=dep[0].attrib["idx"]
                idx2=dep[1].attrib["idx"]
                #print(dep[0].text)
                #print(dep[1].text)
                graph.add_node(pydot.Node(idx1,label=dep[0].text))
                graph.add_node(pydot.Node(idx2,label=dep[1].text))
                graph.add_edge(pydot.Edge(idx1,idx2))
        pic_name="./057result/057result"+str(num)+".png"
        graph.write_png(pic_name)
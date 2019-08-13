
with open("092result1.txt","r") as in1:
    num=0
    correct=0
    line=in1.readline()
    while line:
        if line.strip("\n").split(" ")[-1]=="-1":
            num+=1
        else:
            predict=line.strip("\n").split(" ")[3]
            answer =line.strip("\n").split(" ")[4]
            answer =answer[2:-2]
            #print(predict,answer)
            if predict==answer:
                correct+=1
            num+=1
        line=in1.readline()

    ratio=correct/num
    print("{}/{} , ratio : {}".format(correct,num,ratio))

with open("092result2.txt","r") as in2:
    num=0
    correct=0
    line=in2.readline()
    while line:
        if line.strip("\n").split(" ")[-1]=="-1":
            num+=1
        else:
            predict=line.strip("\n").split(" ")[3]
            answer =line.strip("\n").split(" ")[4]
            answer =answer[2:-2]
            #print(predict,answer)
            if predict==answer:
                correct+=1
            num+=1
        line=in2.readline()

    ratio=correct/num
    print("{}/{} , ratio : {}".format(correct,num,ratio))
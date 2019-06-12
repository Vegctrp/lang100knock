

with open("./076ans.txt","r") as intxt:
    result_list=intxt.readlines()

precision_N=0
precision_num=0
recall_N=0
recall_num=0

for result in result_list:
    res=result.split("\t")
    ans=res[0]
    predict=res[1]
    if predict=="+1":
        precision_N+=1
        if ans=="+1":
            precision_num+=1
    
    if ans=="+1":
        recall_N+=1
        if predict=="+1":
            recall_num+=1

precision=precision_num/precision_N
recall=recall_num/recall_N

F1score=2*(precision*recall)/(precision+recall)

print("precision : "+str(precision)+", recall : "+str(recall)+", F1score : "+str(F1score))

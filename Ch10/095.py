from scipy.stats import rankdata

def make95(infile):
    predict_list=[]
    ans_list=[]
    with open(infile,"r") as intxt:
        while 1:
            line=intxt.readline()
            if not line:
                break
            line=line.strip("\n").split(" ")
            if not line[-1]=="-1":
                predict_list.append(float(line[2]))
                ans_list.append(float(line[3]))
    predict_rank=rankdata(predict_list)
    ans_rank=rankdata(ans_list)
    
    Spearman=1-6*sum([(i-j)**2 for i,j in zip(predict_rank,ans_rank)])/(len(ans_rank)**3-len(ans_rank))
    print(Spearman)

make95("./094result1.txt")
make95("./094result2.txt")
filename="../data/hightemp.txt"
count=0
with open(filename) as data:
    for line in data:
        count+=1

print(count)
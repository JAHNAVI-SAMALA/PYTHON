#MAXIMUM ELEMENT
nlist=list(map(int,input().split()))
maxNum=nlist[0]
for i in range(1,len(nlist)):
    if maxNum<nlist[i]:
        maxNum=nlist[i]
print(maxNum)

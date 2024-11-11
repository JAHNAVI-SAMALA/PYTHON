#second maximum element
nlist=list(map(int,input().split()))
fMax,sMax=nlist[0],-99999
for i in range(1,len(nlist)):
    if fMax<nlist[i]:
        sMax=fMax
        fMax=nlist[i]
    elif sMax<nlist[i]:
        sMax=nlist[i]
print(sMax)

n,k=list(map(int,input().split()))
list1=list(map(int,input().split()))
maxH=max(list1)
if(k>maxH):
    print(0)
else:
    print("no.of doses",maxH-k)

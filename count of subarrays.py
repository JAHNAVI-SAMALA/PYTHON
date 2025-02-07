nums = list(map(int,input().split()))
k = int(input())
d = {0:1}
c = 0
Sum = 0
for i in nums:
    Sum += i
    rem = Sum - k
    if(rem in d):
        c += d[rem]
    if(Sum in d):
        d[Sum] = d[Sum]+1
    else:
        d[Sum] = 1
print(c)
        

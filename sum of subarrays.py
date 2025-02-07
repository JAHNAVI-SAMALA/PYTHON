nums = list(map(int,input().split()))
d = {}
k = int(input())
max_len = 0
Sum = 0
for i in range(0,len(nums)):
    Sum += nums[i]
    if Sum == k :
        max_len = max(max_len,i+1)
    rem = Sum - k
    if rem in d:
        max_len = max(max_len,i-d[rem])
    if Sum not in d :
        d[Sum] = i
print(max_len)
    
        
 

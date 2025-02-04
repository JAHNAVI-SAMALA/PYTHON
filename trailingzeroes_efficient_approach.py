nums = list(map(int,input().split()))
i = -1
for ind in range(0,len(nums)):
    if (nums[ind] == 0):
        i = ind
        break
if(i!=-1):
    for j in range (i+1,len(nums)):
        if(nums[j]!=0):
            nums[i],nums[j] =nums[j],nums[i]
            i += 1
print(nums)

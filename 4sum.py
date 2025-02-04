def four_sum(nums,target):
    nums.sort()
    n= len(nums)
    s=set()
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if(nums[i]+nums[j]+nums[k]+nums[l] == target):
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        s.add(tuple(temp))
    ans = [list(q) for q in s]
    return ans
                        
nums = list(map(int,input().split()))
target = int(input())
print(four_sum(nums,target))

def remove_duplicates(nums):
    i = 0
    for j in range(i+1,len(nums)):
        if(nums[i] != nums[j]):
            nums[i+1] = nums[j]
            i += 1
    print(nums[0:i+1])
nums = list(map(int,input().split()))
remove_duplicates(nums)#tc:O(N),sc:O(1)
    

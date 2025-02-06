def quick(nums,low,high):
    if(low < high):
        pIndex = partition(nums,low,high)
        quick(nums,low,pIndex-1)
        quick(nums,pIndex+1,high)
def partition(nums,low,high):
    i =low
    j = high
    pivot = nums[low]
    while(i<j):
        while(nums[i] <= pivot and i<=high-1):
            i+=1
        while(nums[j]>pivot and j>=low+1):
            j-= 1
        if(i<j):
            nums[i],nums[j] = nums[i],nums[j]
    nums[low],nums[j] = nums[j],nums[low]
    return j
nums = list(map(int,input().split()))
quick(nums,0,len(nums)-1)
print(nums)

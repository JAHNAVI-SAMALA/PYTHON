def majorityElement(nums):
    element = 0
    count = 0
    for i in nums:
        if count == 0:
            element = i
        elif i == element:
            count += 1
        else:
            count += 1
    return element
nums = list(map(int,input().split()))
print(majorityElement(nums))

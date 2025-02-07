nums = list(map(int,input().split()))
n= len(nums)
for i in range (0,n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(nums[k],end = " ")
        print()

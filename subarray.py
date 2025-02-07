#to generate all subarrays from the input array
arr = list(map(int,input().split()))
for i in range (0,len(arr)):
    for j in range(i,len(arr)):
        print(arr[i : j+1],end = " ")

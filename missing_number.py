#code to find missing number in the given array using sum of n natural nums
arr=list(map(int,input().split()))
n = int(input())
def missing_num(arr,n):
    S1 = n*(n+1)// 2
    S2 = sum(arr[0:])
    missing = S1 - S2
    return missing
print(missing_num(arr,n))

arr = list(map(int,input().split()))
def insertionSort(arr):
    n = len(arr)
    for i in range(0,n):
        j=i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr
print(insertionSort(arr))

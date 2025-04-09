def check(ind,n,k,a):
    if k ==0:
        return True
    if k<0 or ind == n:
        return False
    path1 = check(ind+1,n,k-a[ind],a)
    if path1 == True:
        return True
    path2 = check(ind+1,n,k,a)
    return path1 or path2
ind = 0
n=int(input())#array size
k = int(input())#target sum
a = list(map(int,input().split()))#array
print(check(ind,n,k,a))


'''OUTPUT
3
4
1 2 3 
True

2
4
1 2
False
'''

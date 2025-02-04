row,col = map(int,input().split())
mat = []
for i in range(row):
    lst=list(map(int,input().split()))
    mat.append(lst)
print(mat)
def diagonalSum(mat):
    n = len(mat)
    Sum = 0
    for i in range(0,n):
        Sum += mat[i][i]
        if(i!=n-1-i):
            Sum += mat[i][n-1-i]
    return Sum
print(diagonalSum(mat))    

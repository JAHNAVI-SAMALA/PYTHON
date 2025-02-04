row,col = map(int,input().split())
mat = []
for i in range(row):
    lst=list(map(int,input().split()))
    mat.append(lst)
print(mat)
Sum = 0
for i in range(0,len(mat)):
    Sum += mat[i][i]
print(Sum)

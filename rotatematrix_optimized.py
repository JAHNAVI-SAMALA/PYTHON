row,col = map(int,input().split())
mat = []
for i in range(row):
    lst=list(map(int,input().split()))
    mat.append(lst)
def rotate(mat):
    n= len(mat)
    for i in range(0,n-1):
        for j in range(i+1,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for row in range(0,n):
        mat[row] = mat[row][::-1]
    print(mat)
rotate(mat)

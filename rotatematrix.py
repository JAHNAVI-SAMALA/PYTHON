row,col = map(int,input().split())
mat = []
for i in range(row):
    lst=list(map(int,input().split()))
    mat.append(lst)
def rotate(mat):
    n = len(mat)
    dup = [[0]*n for i in range(n)]#t.c. O(N**2) s.c. O(N**2)
    for i in range(n):
        for j in range(n):
            dup[j][n-1-i] = mat[i][j]
    for i in range(0,n):
        for j in range(0,n):
            mat[i][j] = dup[i][j]
    print(mat)
rotate(mat)

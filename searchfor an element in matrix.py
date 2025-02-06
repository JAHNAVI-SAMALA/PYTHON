row,col = map(int,input().split())
mat = []
for i in range(row):
    lst = list(map(int,input().split()))
    mat.append(lst)
target = int(input())
"""for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        if(mat[i][j]==x):
            print("YES")"""
def searchMatrix(mat):
    sr = 0
    er = len(mat)-1
    sc = 0
    ec = len(mat[0])-1
    while(sr <=er and ec >= 0):
        if(mat[sr][ec] == target):
            return True
        elif(mat[sr][ec]< target):
            sr += 1
        elif(mat[sr][ec] > target):
            ec -= 1
    return False
print(searchMatrix(mat))
               

row,col = map(int,input().split())
mat = []
for i in range(row):
    lst = list(map(int,input().split()))
    mat.append(lst)
def spiralOrder(mat):
    n= len(mat)
    m = len(mat[0])
    sr = 0
    er = n-1
    sc = 0
    ec = m-1
    ans = []
    while(sc <= er and sc <= ec):
        for i in range(sc,ec+1):
            ans.append(mat[sr][i])
        sr+=1
        for i in range(sr,er+1):
            ans.append(mat[i][ec])
        ec -=1
        if (sr<= er):
            for i in range(ec,sc-1,-1):
                ans.append(mat[er][i])
            er -= 1
        if sc<=ec:
            for i in range(er,sr-1,-1):
                ans.append(mat[i][sc])
            sc+= 1
    return ans
print(spiralOrder(mat))

        

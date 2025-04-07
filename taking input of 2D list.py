#taking input of a 2D list
row,col = map(int,input().split())
mat = []
for i in range(row):
    lst = list(map(int,input().split()))
    mat.append(lst)
print(mat)

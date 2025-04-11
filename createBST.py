class Node:
    def __init__(self,data):
        self.left = None
        self.val = data
        self.right = None
def createBST(arr):
    root = None
    for data in arr:
        if root == None:
            root = Node(data)
        else:
            temp = root
            while(True):
                if data<temp.val:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = Node(data)
                        break
                elif data>temp.val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = Node(data)
                        break
    return root
def preorder(root):
    if root==None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

arr = list(map(int,input().split()))
root =createBST(arr)
preorder(root)

class Node:
    def __init__(self,data):#node creation
        self.val = data
        self.next = None
def createLinkedList(arr):
    head = None
    for data in arr:
        if(head==None):
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    printLinkedlist(head)        
    #print(head.val) it prints the first node value
def printLinkedlist(head):
    temp = head
    while(temp):
        print(temp.val)
        temp = temp.next
arr = list(map(int,input().split()))
createLinkedList(arr)

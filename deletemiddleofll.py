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
    return head
def deleteMiddle(head):
        slow = head
        fast = head
        prev = None
        if head == None or head.next == None:
            return None
        while fast and fast.next: 
            prev = slow
            slow =slow.next
            fast = fast.next.next
        prev.next=slow.next
        return head
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")
arr = list(map(int, input().split()))
head = createLinkedList(arr)
head =deleteMiddle(head)
printLinkedList(head)


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
def createCycle(head, pos):#creating cycle
    if pos == -1:
        return head
    cycle_start = None
    temp = head
    i = 0
    last = None
    while temp:
        if i == pos:
            cycle_start = temp
        last = temp
        temp = temp.next
        i += 1
    if last:
        last.next = cycle_start  # Creating the cycle
    return head
#logic starts here
def hasCycle(head):
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
arr = list(map(int, input().split()))
head = createLinkedList(arr)
head = createCycle(head, 1)
print(hasCycle(head))

        

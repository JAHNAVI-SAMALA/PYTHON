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
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)

arr = list(map(int, input().split()))
head = createLinkedList(arr)

sol = Solution()
sol.middleNode(head)

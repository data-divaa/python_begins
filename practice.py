class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()



def printMiddle(ptr):
    if head == None:
        return
    slow = head
    fast = head
    while fast!= None and fast.next!=None :
        slow=slow.next
        fast=fast.next.next

    print(slow.key)


head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(89)


printList(head)
printMiddle(head)

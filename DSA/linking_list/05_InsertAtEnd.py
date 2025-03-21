class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def EndInsert(head,key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)#create a new node for new next entry
    return head


head = None
head = EndInsert(head,10)
head = EndInsert(head,20)
head = EndInsert(head,30)


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

printList(head)

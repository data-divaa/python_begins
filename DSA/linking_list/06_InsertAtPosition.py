class Node:
    def __init__(self,key):
        self.key = key
        self.next = None


def insertPos(head,pos,data):
    temp = Node(data)

    if pos == 1:
        temp.next = head
        return temp

    curr = head
    for i in range(pos - 2):
        if curr == None:
            return head
        curr = curr.next

    temp.next = curr.next
    curr.next = temp

    return head



def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


printList(head)
print("\n")

head = insertPos(head,4,45)

printList(head)

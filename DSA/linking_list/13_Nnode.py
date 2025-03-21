'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to print the Nth node from the end of
the linking list
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


def Nnode(head,n):
    if head == None:
        return
    first = head
    second = head
    for i in range(n):
        if first == None:
            return
        first = first.next

    while first != None:
        first = first.next
        second = second.next
    return second.key



def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next


head = Node(90)
head.next = Node(78)
head.next.next = Node(7)
head.next.next.next = Node(44)
head.next.next.next.next = Node(8)


printList(head)

print("the key of nth node from the end of the linked list is :",Nnode(head,3))

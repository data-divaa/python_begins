'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc -  a python program to transverse once through the linked list and
which is in non - decresing order and delete the duplicates
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()

def deldups(head):
    curr = head
    while curr != None and curr.next != None:
        if curr.key == curr.next.key:
            curr.next = curr.next.next
        else:
            curr = curr.next


head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)



printList(head)
deldups(head)
printList(head)

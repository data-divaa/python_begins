'''
Author - Data - Divaa
Date - 16 - 03 -2025
Desc - a python program to delete a node in a singly linked list given by a pointer
'''


class Node:
    def __init__(self,k):
        self.data = k
        self.next = None


def DelNode(ptr):
    temp = ptr.next # temp stores the element next to the pointer
    ptr.data = temp.data # changing the data of temp to the pointer data
    ptr.next = temp.next # skipping the pointer node


def printList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print("")


head = Node(10)
head.next = Node(24)
head.next.next = Node(89)


printList(head)

DelNode(head)

printList(head)

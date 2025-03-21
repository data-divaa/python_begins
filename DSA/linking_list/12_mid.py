'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to print the middle of a linked list
if odd print the middle and if if even print second to the middle
'''


class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


def mid(head):
    if head == None:
        return
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    print(slow.key)


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

head = Node(10)
head.next = Node(15)
head.next.next = Node(90)
head.next.next.next = Node(100)


print("Linked list:")
printList(head)


print("middle node :")
mid(head)

'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to reverse the linked list using recurvion
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def RecursionReverse01(head):

    if head == None:
        return

    if head.next == None:
        return head


    rest_head = RecursionReverse01(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None

    return rest_head

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

printList(head)

head = RecursionReverse01(head)

printList(head)

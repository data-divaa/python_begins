'''
author - Data - divaa
date = 15 -03 -2025
desc - make a python program to delete the last element of
the linked list
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def delLast(head):
    if head == None:
        return None

    if head.next == None:
        return None

    curr = head

    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head



def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print("")


head = Node(29)
head.next = Node(78)
head.next.next = Node(67)
head.next.next.next = Node(45)

print("before deleting the last of the linked list :")
printList(head)


head = delLast(head)


print("after delteing the last element of the linked last :")
printList(head)

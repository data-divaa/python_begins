'''
author - Data- Divaa
date - 15-03-2025
desc - write a python program to delete the first element of
the linking list
'''


class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


def delFirst(head):
    if head == None:
        return None
    else:
        return head.next


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print("")


head = Node(10)
head.next = Node(20)
head.next.next = Node(78)
head.next.next.next =Node(3)


print("Before removal of the first element from the linked list :")
printList(head)

head = delFirst(head)

print("after removal of the first element from the linked list :")
printList(head)

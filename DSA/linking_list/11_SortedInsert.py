'''
Author - Data - Divaa
Date - 17 -03- 2025
Desc - a python program to insert a value into a sorted linked array
'''

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


def SortedInsert(head,x):
    temp = Node(x)

    if head == None:
        return temp

    elif x < head.key:
        temp.next = head
        return temp

    else:
        curr = head

        while curr.next != None and curr.next.key <x:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)


print("before insertion :")
printList(head)

print("")

head = SortedInsert(head,35)

print("after insertion :")
printList(head)

'''
author - Data- Divaa
date - 11-03-2025
desc - a python program to define a function print the elements of a linked list
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

#defining the function
#assign head to curr and run a while loop until the list is empty
#print the curr's key and then change the curr to the upcoming element
def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

#creting the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)


#function call
printList(head)

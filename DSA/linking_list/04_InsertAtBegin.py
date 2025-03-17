'''
author - Data- Divaa
date - 12-03-2025
desc - a python program to define a function to add a new element at
the begining of a existing linked list and then return the list
'''


class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


#function define
def insertBegin(head,key):
    temp = Node(key) #create a new node temp
    temp.next = head
    return temp

head = None
head = insertBegin(head,10)
head = insertBegin(head,20)
head = insertBegin(head,30)

def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next


printList(head)

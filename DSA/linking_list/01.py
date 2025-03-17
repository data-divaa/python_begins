'''
author - Data- Divaa
date - 11-03-2025
desc - a simple program to make a linked list and print it
'''


class Node:
    def __init__(self,k):
        self.key = k
        self.next = None



#creating the linked list
head = Node(100)#head is the first kindof element in the linked list
head.next = Node(90)
head.next.next = Node(56)


#printing the printing list
print(head.key)
print(head.next.key)
print(head.next.next.key)

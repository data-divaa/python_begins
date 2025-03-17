'''
author - Data- Divaa
date - 12-03-2025
desc - take input and create a linked list
'''


class Node:
    def __init__(self,key):
        self.key = key
        self.next = None


n = int(input("enter the number of element to be inserted into a empty linked list :"))

for i in range(n):
    data = input("enter the element :")
    temp = Node(data)

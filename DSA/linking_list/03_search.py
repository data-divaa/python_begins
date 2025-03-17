'''
author - Data- Divaa
date - 12 -03-2025
desc - a python program to define a function to search a element in the linked list
if found return the index
'''



class Node:
    def __init__(self,k) :
        self.key = k
        self.next = None


#function definition
def search(head,x):
    pos = 1 #initiate pos to 1
    curr = head
    #run the loop until the last element
    while curr != None:
        if curr.key == x: #the the key of curr match with the target x
            return pos #return the position
        pos += 1 #increment the position by 1
        curr = curr.next #change the curr to the the next element
    return -1 #if not the target x is not found in the linked list then return -1

#creating the linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)

x = 20 #target

#function call
print(search(head,x))

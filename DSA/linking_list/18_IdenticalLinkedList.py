'''
Author - Data - Divaa
Date - 19 -03- 2025
Desc - a python program to check if
two linked lists are identical or not if yes return True or else False
'''

class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

def areIdentical(head1,head2):
    curr1 = head1
    curr2 = head2
    while curr1 != None and curr2 != None:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(78)
head1.next.next.next = Node(4)


head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)


print(areIdentical(head1,head2))

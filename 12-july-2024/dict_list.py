'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
a dictionary using two lists inputted by user.
'''


def dict_list(list1,list2):
    dict = {}
    # because key are immutable and list are mutable ao they had to be changed into tuple
    dict[tuple(list1)] = list2
    return dict

list1 = list(input("enter the list separted by space").split())
list2 = list(input("enter the another list separted by space").split())

print(dict_list(list1,list2))

'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
a dictionary using two lists inputted by user.
'''


def dict_list(list1,list2):
    dict1 = {}
    if len(list1) != len(list2):
        print("make sure you are entering same number of key value pair")
    else:
        for i in range(len(list1)):
            dict1[list1[i]] = list2[i]
    return dict1

list1 = list(input("list1: ").split())
list2 = list(input("list2: ").split())

print(dict_list(list1,list2))

'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
a dictionary using two lists inputted by user.
'''
import sys

def dict_list(list1,list2):
    dict1 = {}
    #iterate over both the list and form a key-value pair
    for i,j in zip(list1, list2):
        dict1[i] = j
    return dict1

list1 = list(input("Input the list containing keys : ").split())
list2 = list(input("Input the list containing values : ").split())
#input validation
if len(list1) != len(list2):
    print("Both the lists should contain the same number of elements...exiting program")
    sys.exit()

print("The new dictionary is ", dict_list(list1,list2))

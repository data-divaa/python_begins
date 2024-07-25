'''
Date - 13 - july - 2024
Author - Data-Divaa
Question -
- Write a program that takes a list from the user as input. then concat that list elements to a string and print
'''

#defining the function
def concat(lst):
    string = ''
    for i in lst:
        string = string + i
    return string


#taking inputs
lst = list(input("enter the list to be joined together(separated by space): ").split())
print("list entered looks like this : ",lst)

#calling the function
print("after joining the list looks like this: ",concat(lst))

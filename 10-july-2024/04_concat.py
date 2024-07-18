'''
Date - 13 - july - 2024
Author - Data-Divaa
Question -
- Write a program that takes a list from the user as input. then concat that list elements to a string and print
'''


# defining the function
def concat(lst):
    string = ''
    for j in lst: #every element of lst will be added to string one by one
        string = string + j
    return string

#taking input
lst = list(input("enter the list separted by space").split())

#calling function
print(concat(lst))

"""
Date - 04 - july - 2024
Author - Data-Divaa
Question -
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')


"""

def list(lst):
    return lst

def tuplee(lst):
    tup = tuple(lst)
    return tup

lst = input().split(',')

print(list(lst))
print(tuplee(lst))

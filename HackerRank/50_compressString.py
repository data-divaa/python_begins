'''
Date - 04 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a string S suppose a character c occurs consecutively
x times in the string .replace those consecutive occureence of teh character
c with (x, c) in the string
'''
import itertools
s = input("enter the string to count the apperance")
s = list(s)#we change it into list for easy access
grouped = itertools.groupby(s)
lst = [(len(list(group)),key) for key,group in grouped]
print(' '.join([f"({key}, {count})" for key,count in lst]))

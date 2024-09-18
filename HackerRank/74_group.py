'''
Date - 17 - September- 2024
Aurthur - Data-Divaa
Question -
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character  S in (read from left to right) that has consecutive repetitions.
'''

import re

#defining the function
def first_occurrence(string):
    pattern_match = re.search(r"([a-zA-Z0-9])\1+",string)
    '''
    pattern start can start with any alphanumeric it should be more than one(1+)
    '''
    if pattern_match:
        return pattern_match.group(1)#if the search comes true then print the group 1
    else:
        return -1#else return -1

#taking inputs
string = input("enter the string to check for consecutive alphanumeric occurrence")

#calling function

print("after checking",first_occurrence(string),"appears first consecutive")

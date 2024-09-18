'''
Date - 17 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a string s consisting only of digits 0-9,
commas(,) and dots (.)
your task is to complete thr regex_pattern defined below,
which will be used to re.split() all of the , and . symbols
in s.
its guaranteed that every comma and every dot in s is preceeded and followed by a digit.
'''


import re

def re_split(string):
    regex_pattern =  r'[,.]'
    print("\n".join(re.split(regex_pattern,string)))
    '''
    re.split() will break the string whenever it will
encounter either , or . according to the pattern given
    '''


#taking inputs
string = input("enter your string:")


#calling function
print("after spliting the string on , or . :")
re_split(string)

'''
Date - 16 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a string N.
yo have to verify that N is a floating point number.
'''

import re

#defining the function
def detect_float(lst):
    float_num = r'^[+-]?[0-9]*\.[0-9]+$'
    '''
    the pattern can start eith -,= or 0-9 or none tehn . 0-9 number and then end of the pattern
    '''
    result = []
    for k in lst:
        if re.search(float_num,k):
            result.append(True)
        else:
            result.append(False)
    for i in result:
        print(i)


#taking inputs
lst = []
n = int(input("enter the number of strings to check if they are float or not :"))
for i in range(n):
    lst.append(input("enter the number:"))


#calling function
detect_float(lst)

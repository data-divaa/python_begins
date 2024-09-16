'''
Date - 16 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a string N.
yo have to verify that N is a floating point number.
'''

import re


def detect_float(lst):
    float_num = r'^[+-]?[0-9]*\.[0-9]+$'
    result = []
    for k in lst:
        if re.search(float_num,k):
            result.append(True)
        else:
            result.append(False)
    for i in result:
        print(i)

lst = []
n = int(input())
for i in range(n):
    lst.append(input())

detect_float(lst)

'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
take input and print transpose and flatten of the arrays
'''

import numpy as np

def transpose_flatten(lst):
    arr = np.array(lst)
    trans = np.transpose(arr)
    flat = arr.flatten()
    print("after transpose")
    print(trans)
    print("after flatten")
    print(flat)


n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))


transpose_flatten(lst)

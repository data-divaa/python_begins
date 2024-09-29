'''
Date - 29 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a 1-D array A.
your task is to print the floor ,ceil , rint of all element of A
'''

import numpy as np
np.set_printoptions(legacy='1.13')

A_lst = list(map(float,input().split()))
A = np.array(A_lst)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))

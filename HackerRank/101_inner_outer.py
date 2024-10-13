'''
Date - 30 - September- 2024
Aurthur - Data-Divaa
Question -
you are given two arrays A and B
your task is to compute their inner an douter product
'''

import numpy as np
A = np.array(list(map(int,input().split())))
B = np.array(list(map(int,input().split())))
print(np.inner(A,B))
print(np.outer(A,B))

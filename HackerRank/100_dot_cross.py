'''
Date - 30 - September- 2024
Aurthur - Data-Divaa
Question -
you are given two array A and B.
both have dimesion n X n
your task is to compute their matrix product
'''

import numpy as np
n = int(input("enter the dimension of the arrays"))
A = np.array([list(map(int,input().split()))for i in range(n)])
B = np.array([list(map(int,input().split()))for i in range(n)])
print("the matrix product of the two arrays is:")
print(np.dot(A,B))

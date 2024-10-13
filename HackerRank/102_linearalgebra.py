'''
Date - 03 - October - 2024
Aurthur - Data-Divaa
Question -
you ar given a sqaure matrix A with dimesion n xn your task
is t find the determinant
'''

import numpy as np
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(float,input().split())))
arr = np.array(lst)
print(round(np.linalg.det(arr),2))

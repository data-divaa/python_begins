'''
Date - 29 - September- 2024
Aurthur - Data-Divaa
Question -
you are given two dimension array
your task is to perform the min functio over the axis 1 and then find the max
of that
'''

import numpy as np

n,m = map(int,input("enter the dimension of the arrays").split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

arr = np.array(lst)
min_arr = np.min(arr,axis= 1)
max_min = np.max(min_arr)

print("the maximum of the minimum out of the array(axis =1) is :"max_min)

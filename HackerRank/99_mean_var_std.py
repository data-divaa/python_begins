'''
Date - 29 - September- 2024
Aurthur - Data-Divaa
Question -
you rae two dimension array of size n x m
your task is to find :
1. the mean along axis 1
2. the var along axis 0
3. the std along axis none

'''

import numpy as np

n,m = map(int,input("enter the dimension of the array ").split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

arr = np.array(lst)

print("mean of array (axis =1):"np.mean(arr,axis = 1))
print("variance of the array(axis=0):",np.var(arr,axis = 0))
print("standrad deviation of the whole array :",round(np.std(arr),11))
#around - round an array to the given number of decimal

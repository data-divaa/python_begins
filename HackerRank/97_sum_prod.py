'''
Date - 29 - September- 2024
Aurthur - Data-Divaa
Question -
you are given 2-d array with dimension n xm
your task is to perform the sum tool axis 0 and then find the product of that result
'''

import numpy as np
n,m = map(int,input("enter the dimension of the array").split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr = np.array(lst)
sum = np.sum(arr,axis =0)
pro = 1
for i in list(sum):
    pro = pro * i

print("the product of sum of elements at axiis 0 is ",pro)

'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
you are given two intger arrays of size n x p and m x p
where n and m are rows and p is the coulmns.
your task is to concatenate the arrays along axis 0
'''

import numpy as np

n,m,p = map(int,input().split())
lst1 = []
for i in range(n):
    lst1.append(list(map(int,input().split())))
lst2 =[]
for i in range(m):
    lst2.append(list(map(int,input().split())))


def concate(lst1,lst2):
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)
    return np.concatenate((arr1,arr2))

print(concate(lst1,lst2))

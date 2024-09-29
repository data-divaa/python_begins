'''
Date - 26 - September- 2024
Aurthur - Data-Divaa
Question -
you are given two integers arrays A and B of dimension nxm
your task is to perform the following opearation:
add,subtract,multiply,intger division,mod,powr

'''
import numpy as np
n,m = map(int,input("enter the dimension of the two arrays").split())
arr1 = np.array([list(map(int,input().split()))for _ in range(n)])
arr2 = np.array([list(map(int,input().split()))for _ in range(n)])
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.floor_divide(arr1,arr2))
print(np.mod(arr1,arr2))
print(np.power(arr1,arr2))

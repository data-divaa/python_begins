'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
you are given the shape of the array in the form of space
seperated integers. each intgers representing teh size of different dimension,
your task is to print an array of the given shape and intgers
type using the tools numpy.zeros and numpy.ones

'''
import numpy as np

lst = tuple(map(int,input().split()))
z =np.zeros(lst,dtype = int)
print(z)
o= np.ones(lst,dtype= int)
print(o)

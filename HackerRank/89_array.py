'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
given a space seperated list of numbers and you have to print the reversed numpy array with the element type float

'''

import numpy

def arrays(arr):
    aa = arr[::-1]
    return numpy.array(aa,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

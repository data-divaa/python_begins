'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a space seperated list of nine integers. your task
is to convert this list into a 3 X 3 numpy array
'''

import numpy as np
import sys

arr = np.array(list(map(int,input("enter the numbers (only) space seperated").split())))
if len(arr) != 9:
    print("invalid input ---- existing the program")
    sys.exit()
print(np.reshape(arr,(3,3)))

'''
Date - 26 - September- 2024
Aurthur - Data-Divaa
Question -
your task is to print an array of szie nxm with its main diagonal
elements as 1's and 0's everywhere else
'''

import numpy as np
np.set_printoptions(legacy='1.13')
m,n= map(int,input("enter the dimension of the array(space seperated):").split())
print(np.eye(m,n))

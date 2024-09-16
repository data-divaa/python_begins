'''
Date - 16 - September- 2024
Aurthur - Data-Divaa
Question -
take input of rational numbers and print its product
'''

from fractions import Fraction
from functools import reduce


#defining the function
def product(fracs):
    t = reduce(lambda x,y : x*y,fracs)
    '''
    by lambda function the two are multiplied and
    by reduce it is first done by the first two then it follows to the rest
    '''
    return t.numerator, t.denominator


#taking inputs
fracs = []
n = int(input("enter the number of rational numbers:"))
for _ in range(n):
    fracs.append(Fraction(*map(int,input().split())))
    #here we use *map for fration to unpack arguments


#calling function
print(*product(fracs))
#here * is used to sepeatred the argumnets again

'''
Date - 12- august - 2024
Authur - Data - Divaa
Question -
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door
 mat with the following specifications:

Mat size must be N X M (N is an odd natural number,M and 3 is times N)
.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''

import sys
def doormat(n,m):
    #storing the data into the variable for easy use
    a = ".|."
    #first half
    for i in range((n-1)//2):
        #above make sures that the print goes half way of total length and make it even for desirable result
        print((a*(2*i+1)).center(m,"-"))

    #welcome part
    print(("WELCOME").center(m,"-"))

    #bottom half
    #same logic of upper half goes here but reverseing the order
    for k in range((n-1)//2-1,-1,-1):
        print((a*(2*k+1)).center(m,"-"))



#taking inputs
print("enter odd integer only")
n = int(input("enter the length of the doormat: "))
#input validation
if n % 2 == 0:
    print("invalid input ------ existing program")
    sys.exit()


print("enter the breadth which 3 times of n")
m = int(input("enter the breadth of the doormat: "))
#input validation
if n*n*n != m:
    print("invalid input ------ existing program")
    sys.exit()


#calling function
doormat(n,m)

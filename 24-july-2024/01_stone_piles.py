'''
Date - 24 - july - 2024
Author - Data-Divaa
Question -
1.	We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones.
Each pile must more stones than the previous pile but as few as possible.
Write a  Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
'''

import sys

#defining the function
def stone_pile(StonePile):
    stones = []
    if int(StonePile) % 2 == 0:# if StonePile is even then
    # in loop range starts from Stonepile and goes up to n+(2*n) so that it could go around upto desirable length with step of 2
        for i in range(int(StonePile),int(StonePile)+(2*int(StonePile)),2):
            stones.append(i)
    else:#if not this conditions follows
    #loop is same but condtion differs as it is for odd ones
        for k in range(int(StonePile),int(StonePile)+(2*int(StonePile)),2):
            stones.append(k)
    return stones


#taking inputs
print("--------ENTER INTEGER ONLY-----------")
StonePile = input("Enter the number of Stone Piles : ")
#input validation

for j in StonePile:
    #every character of StonePile changes into ascii value and then goes through the conditions
    # it was required to use as ord takes only one character
    ascii_StonePile = ord(j)
    if not(48 <= ascii_StonePile <= 57):
        print("Invalid Entry--------Exiting Program")
        sys.exit()

# showing inputs
print("------------------------------------------------------")
print("total number of stones piles = ",StonePile)


#calling function
print("number of stones in ",StonePile,"stone piles if first stone pile has ",StonePile,"is")
print(stone_pile(StonePile))

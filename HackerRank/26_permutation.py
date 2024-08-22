'''
Date - 22 - august - 2024
Authur - Data - Divaa
Question -
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
'''

from itertools import permutations

#defining the function
def permutation(string,n):
    lst = permutations(string,n)#here a list is formed of characters of string of n number
    for i in sorted(lst):#we needed to sorted it for a lexicographic order
        print(''.join(i))#these nested listed are printed as a string

#taking input
user_input = input("enter the string and number to be permutated(space seperated) :")
string,n = user_input.split()
n = int(n)

#calling the function
permutation(string,n)

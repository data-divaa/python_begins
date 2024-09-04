'''
Date - 04 - September- 2024
Aurthur - Data-Divaa
Question -
You are given a string S .
Your task is to print all possible size k replacement
combinations of the string in lexicographic sorted order.
'''
from itertools import combinations_with_replacement
s,k = input("enter the string and number for replacement combination space seperated:").split()
s = list(sorted(s))
k = int(k)
out = list(combinations_with_replacement(s,k))
for i in out:
    print(''.join(i))

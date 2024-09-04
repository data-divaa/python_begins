'''
Date - 04 - September- 2024
Aurthur - Data-Divaa
Question -
You are given a string S.
Your task is to print all possible combinations,
up to size k,
 of the string in lexicographic sorted order.
'''

from itertools import combinations
s,k = input("enter the string and number it has to upto to form combinations  space seperated").split()
k = int(k)
s = list(sorted(s))
result = []
for i in range(1,k+1):
    #here we go upto k+1 that is upto k from 1 for desirbale output
    l = list(combinations(s,i))
    result.append(l)
for k in result:
    for j in k:
        print(''.join(j))

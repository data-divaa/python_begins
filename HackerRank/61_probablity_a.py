'''
Date - 09 - September- 2024
Aurthur - Data-Divaa
Question - take a list and print the probablity of the occurenece
of the index of a
'''
from itertools import combinations
n = int(input("enter the length of list"))
lst = list(input().split())
k = int(input("number of indeices to be selected:"))
comb = list(combinations(lst,k))
result = []
for i in comb:
    if 'a' in i :
        result.append(i)
print(len(result)/len(comb))

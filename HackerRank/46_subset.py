'''
Date - 03 - September- 2024
Aurthur - Data-Divaa
Question - you are given two set A and B if
A is the subset of B print true if not print False
'''

ntc = int(input("enter the number of test case:"))
result = []
for _ in range(ntc):
    na = int(input("enter the number of elements in set A:"))
    a = set(map(int,input().split()))
    nb = int(input("enter the number of elements in set B:"))
    b = set(map(int,input().split()))

    if a.issubset(b):
        result.append("True")
    else:
        result.append("False")
for i in result:
    print(i)

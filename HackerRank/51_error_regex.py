'''
Date - 05 - September- 2024
Aurthur - Data-Divaa
Question - take a pattern and print true if it regx and if error found print false
'''



#it will not work for python3 but pypy 3
import re

n = int(input("enter the number of test cases to check it is regx or not :"))
result = []
for _ in range(n):
    s = input("enter the string :")
    try:
        re.compile(s)#if it compiles
        result.append(True)
    except re.error as e:
        result.append(False)

for i in result:
    print(i)

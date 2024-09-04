'''
Date - 03 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a set A is a strict superset of each of the
N sets. your job is to find whetehr set A is a strict superset of each of the N sets
print True if A is superset of all or else False
'''

setA = set(map(int,input("enter the main set A:").split()))
n = int(input("enter the number of sets to be compared with set A for strict supersubset"))
result = True
for _ in range(n):
    s = set(map(int,input().split()))
    #if the condition inside not() is condition true supersubset but due to not
    #it will check which is not
    if not(setA.issuperset(s) and setA != s):
        result = False

print(result)

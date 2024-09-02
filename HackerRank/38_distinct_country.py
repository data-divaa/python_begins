'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question -
Rupal has a huge collection of country stamps.
 She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
'''

n = int(input("enter the number of stamps: "))
l1 = []
for _ in range(n):
    l1.append(input("enter the name of country of the stamp:"))
s1 = set(l1)
print(len(s1))

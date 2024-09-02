'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question -
you have a non- empty set s, and you have to execute N
commands given in N lines
'''
import sys

#defining the input
n = int(input("enter the number of elements in the list: "))
ele = list(map(int,input("enter the elements of the set space seperated:").split()))
#input validations
for g in ele:
    if (g > 9) or (g < 0):
        print("error.....existing program")
        sys.exit()
s1 = set(ele)
num = int(input("enter the number of commands:"))
l = []
for _ in range(num):
    l.append(input().split())


#defining the function
def operations(l,s1):
    for i in l:
        if i[0] == "remove":
            s1.remove(int(i[1]))
        elif i[0] == "discard":
            s1.discard(int((i[1])))
        elif i[0] == "pop":
            s1.pop()
        else:
            pass
    sum = 0
    for k in s1:
        sum = sum + k
    return sum

#calling the function
print("the sum of the elements present in the set after the operation is ",operations(l,s1))

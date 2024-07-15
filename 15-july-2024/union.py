'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation union on them
'''

def union (list1,list2):
    union_list = []
    for i in range(len(list1)):
        union_list.append(list1[i])
        if union_list.count(list1[i]) != 1:
            union_list.remove(list1[i])
    for j in range(len(list2)):
        union_list.append(list2[j])
        if union_list.count(list2[j]) != 1:
            union_list.remove(list2[j])
        union_set = set(union_list)
    return union_set

list1 = list(input().split())
list2 = list(input().split())

print(union(list1,list2))

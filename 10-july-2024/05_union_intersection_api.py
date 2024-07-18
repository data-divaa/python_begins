'''
Date - 14 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operations on them ( without using API ) - union, intersection etc.
'''


def union_intersection_api(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)
    inter_set = set1.intersection(set2)
    return union_set , inter_set

list1 = list(input().split())
list2 = list(input().split())

print(union_intersection_api(list1,list2))

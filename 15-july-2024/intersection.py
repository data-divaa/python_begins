'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation intersection on them
'''


def intersection(list1,list2):
    inter_list = []
    for i in range(len(list1)):
        if list1[i] not in list2 :
            inter_list.append(list1[i])
    for j in range(len(list2)):
        if list2[j] not in list1 :
            inter_list.append(list2[j])
    inter_set = set(inter_list)
    return inter_set


list1 = list(input().split())
list2 = list(input().split())

print(intersection(list1,list2))

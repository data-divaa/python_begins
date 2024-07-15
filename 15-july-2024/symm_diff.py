'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation symmetric difference on them
'''


def symm_diff(list1,list2):
    symm_list = []
    for i in range(len(list1)):
        if list1[i] in list1 and list1[i] not in list2:
            symm_list.append(list1[i])
    for j in range(len(list2)):
        if list2[j] in list2 and list2[j] not in list1:
            symm_list.append(list2[j])
    symm_set = set(symm_list)
    return symm_set


list1 = list(input().split())
list2 = list(input().split())

print(symm_diff(list1,list2))

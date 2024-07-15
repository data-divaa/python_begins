'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation difference on them
'''

def difference(list1,list2):
    diff_list = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            diff_list.append(list1[i])
    diff_set = set(diff_list)
    return diff_set


list1 = list(input().split())
list2 = list(input().split())

print(difference(list1,list2))
